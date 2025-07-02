# File: src/conversation.py
# Diimplementasikan progres real-time dengan Popen

import os
import subprocess
import logging
import asyncio
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
from telegram.constants import ParseMode
from telegram.error import BadRequest

from .translations import TRANSLATIONS

# --- KONFIGURASI & LOGIC ---
logger = logging.getLogger(__name__)

# Menghapus variabel lama, kita akan memanggil modul secara langsung
# CONVERTER_SCRIPT = "sticker-convert" 
PLATFORMS_NEEDING_TOKEN = ['discord', 'kakaotalk']
MAX_CONCURRENT_USERS = 2
CURRENT_CONVERSIONS = 0

SELECT_LANG, SELECT_PLATFORM, SELECT_OUTPUT_TYPE, AWAIT_TOKEN, AWAIT_URL = range(5)

def get_text(key, lang_code='en'):
    if lang_code is None: lang_code = 'en'
    return TRANSLATIONS.get(lang_code, TRANSLATIONS['en']).get(key, f"_{key}_")

# Fungsi start, select_lang, select_platform, receive_token, select_output_type tidak berubah
# ... (Salin semua fungsi dari 'start' hingga 'select_output_type' dari panduan sebelumnya ke sini) ...
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    keyboard = [[InlineKeyboardButton("English", callback_data="en"), InlineKeyboardButton("Bahasa Indonesia", callback_data="id")]]
    await update.message.reply_text(get_text('choose_lang', 'en'), reply_markup=InlineKeyboardMarkup(keyboard))
    return SELECT_LANG

async def select_lang(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = query.data
    context.user_data['lang'] = lang
    
    platforms = [
        [InlineKeyboardButton("Line", callback_data="line"), InlineKeyboardButton("KakaoTalk", callback_data="kakaotalk")],
        [InlineKeyboardButton("Discord", callback_data="discord"), InlineKeyboardButton("Signal", callback_data="signal")],
        [InlineKeyboardButton("WhatsApp", callback_data="whatsapp"), InlineKeyboardButton("Band", callback_data="band")],
        [InlineKeyboardButton("Viber", callback_data="viber"), InlineKeyboardButton("OGQ", callback_data="ogq")],
    ]
    
    await query.edit_message_text(
        get_text('welcome', lang),
        reply_markup=InlineKeyboardMarkup(platforms),
        parse_mode=ParseMode.HTML
    )
    return SELECT_PLATFORM

async def select_platform(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get('lang', 'en')
    platform = query.data
    context.user_data['platform'] = platform
    
    if platform in PLATFORMS_NEEDING_TOKEN:
        await query.edit_message_text(text=get_text('request_token', lang), parse_mode=ParseMode.HTML)
        return AWAIT_TOKEN
    else:
        keyboard = [
            [InlineKeyboardButton(get_text('output_sticker', lang), callback_data="sticker")],
            [InlineKeyboardButton(get_text('output_emoji', lang), callback_data="emoji")],
        ]
        await query.edit_message_text(
            text=get_text('choose_output', lang).format(platform=platform.upper()),
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode=ParseMode.HTML
        )
        return SELECT_OUTPUT_TYPE

async def receive_token(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get('lang', 'en')
    context.user_data['token'] = update.message.text
    
    platform = context.user_data.get('platform', 'Unknown')
    keyboard = [
        [InlineKeyboardButton(get_text('output_sticker', lang), callback_data="sticker")],
        [InlineKeyboardButton(get_text('output_emoji', lang), callback_data="emoji")],
    ]
    await update.message.reply_text(
        text=get_text('token_received', lang).format(platform=platform.upper()),
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode=ParseMode.HTML
    )
    return SELECT_OUTPUT_TYPE

async def select_output_type(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get('lang', 'en')
    context.user_data['output_type'] = query.data
    
    platform = context.user_data.get('platform', 'platform')
    output_name = get_text('output_sticker', lang) if query.data == "sticker" else get_text('output_emoji', lang)
    
    await query.edit_message_text(
        text=get_text('request_url', lang).format(output_name=output_name, platform=platform.upper()),
        parse_mode=ParseMode.HTML
    )
    return AWAIT_URL

async def receive_url(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Fungsi inti dengan progres real-time."""
    global CURRENT_CONVERSIONS
    lang = context.user_data.get('lang', 'en')

    if CURRENT_CONVERSIONS >= MAX_CONCURRENT_USERS:
        await update.message.reply_text(get_text('bot_busy', lang), parse_mode=ParseMode.HTML)
        return ConversationHandler.END

    CURRENT_CONVERSIONS += 1
    logger.info(f"Proses baru dimulai. Total proses aktif: {CURRENT_CONVERSIONS}")
    
    progress_message = await update.message.reply_text(get_text('progress_start', lang), parse_mode=ParseMode.HTML)
    last_message = ""

    try:
        user_url = update.message.text
        chat_id = update.message.chat_id
        
        platform = context.user_data.get('platform')
        output_type = context.user_data.get('output_type')
        token = context.user_data.get('token')
        
        if not platform or not output_type:
            await progress_message.edit_text("Error: session expired. Please /start again.")
            return ConversationHandler.END

        preset = "telegram_emoji" if output_type == 'emoji' else "telegram"
        output_dir = os.path.join("converted_output", str(chat_id))
        os.makedirs(output_dir, exist_ok=True)
        
        # Mengubah cara pemanggilan skrip menjadi pemanggilan modul (-m)
        # Ini lebih stabil dan portabel daripada memanggil skrip secara langsung.
        command = [
            "python3", "-m", "sticker_convert", platform, "download", user_url,
            "--output", output_dir, "--preset", preset, "--steps", "16", "--processes", "1"
        ]
        if token: command.extend(["--token", token])

        logger.info(f"Executing command: {' '.join(command)}")
        
        # Menggunakan Popen untuk membaca output secara real-time
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, encoding='utf-8')

        for line in iter(process.stdout.readline, ''):
            logger.info(f"Engine output: {line.strip()}")
            new_message = ""
            # Mencari kata kunci di output engine
            if "Found" in line:
                count = re.search(r'Found (\d+)', line)
                if count:
                    new_message = get_text('progress_found', lang).format(count=count.group(1))
            elif "Downloading" in line:
                progress = re.search(r'(\d+)/(\d+)', line)
                if progress:
                    new_message = get_text('progress_downloading', lang).format(current=progress.group(1), total=progress.group(2))
            elif "Converting" in line:
                progress = re.search(r'(\d+)/(\d+)', line)
                if progress:
                    new_message = get_text('progress_converting', lang).format(current=progress.group(1), total=progress.group(2))
            
            # Hanya edit pesan jika ada progres baru, untuk menghindari spam ke API Telegram
            if new_message and new_message != last_message:
                try:
                    await progress_message.edit_text(new_message, parse_mode=ParseMode.HTML)
                    last_message = new_message
                    await asyncio.sleep(1) # Beri jeda sedikit
                except BadRequest as e:
                    if "Message is not modified" not in str(e):
                        logger.error(f"Gagal mengedit pesan: {e}")

        process.stdout.close()
        return_code = process.wait()

        if return_code != 0:
            await progress_message.edit_text(get_text('error', lang).format(error_message="Proses gagal, cek log server."), parse_mode=ParseMode.HTML)
        else:
            await progress_message.edit_text(get_text('progress_finished', lang), parse_mode=ParseMode.HTML)
            hasil_konversi = sorted(os.listdir(output_dir))
            if not hasil_konversi:
                await update.message.reply_text(get_text('no_files', lang))
            else:
                for filename in hasil_konversi:
                    filepath = os.path.join(output_dir, filename)
                    try:
                        await update.message.reply_document(document=open(filepath, "rb"))
                    finally:
                        if os.path.exists(filepath): os.remove(filepath)
                
                await update.message.reply_text(get_text('success', lang).format(count=len(hasil_konversi)))
                guide_title_key = 'guide_emoji_title' if output_type == 'emoji' else 'guide_sticker_title'
                guide_body_key = 'guide_emoji_body' if output_type == 'emoji' else 'guide_sticker_body'
                await update.message.reply_text(
                    f"<b>{get_text(guide_title_key, lang)}</b>\n\n{get_text(guide_body_key, lang)}",
                    parse_mode=ParseMode.HTML
                )

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        await progress_message.edit_text(get_text('unexpected_error', lang).format(e=e))
    
    finally:
        CURRENT_CONVERSIONS -= 1
        logger.info(f"Proses selesai. Sisa proses aktif: {CURRENT_CONVERSIONS}")
        context.user_data.clear()
        return ConversationHandler.END


async def cancel_in_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    lang = context.user_data.get('lang', 'en')
    await update.message.reply_text(get_text('cancelled', lang))
    context.user_data.clear()
    return ConversationHandler.END

# --- Handler Utama untuk Percakapan ---
conv_handler = ConversationHandler(
    entry_points=[CommandHandler("start", start)],
    states={
        SELECT_LANG: [CallbackQueryHandler(select_lang)],
        SELECT_PLATFORM: [CallbackQueryHandler(select_platform)],
        AWAIT_TOKEN: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_token)],
        SELECT_OUTPUT_TYPE: [CallbackQueryHandler(select_output_type)],
        AWAIT_URL: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_url)],
    },
    fallbacks=[CommandHandler("cancel", cancel_in_conversation)],
)