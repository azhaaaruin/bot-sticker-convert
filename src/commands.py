# File: src/commands.py
# Diperbarui untuk menampilkan status antrian

import datetime
import psutil
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode

from .translations import TRANSLATIONS

# Variabel ini kita pindahkan ke sini karena status command membutuhkannya
BOT_VERSION = "1.0"
BOT_START_TIME = datetime.datetime.now()

# --- FUNGSI HELPER ---
def get_text(key, lang_code='en'):
    if lang_code is None: lang_code = 'en'
    return TRANSLATIONS.get(lang_code, TRANSLATIONS['en']).get(key, f"_{key}_")

# --- FUNGSI-FUNGSI COMMAND ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan pesan bantuan."""
    lang = context.user_data.get('lang', 'en')
    await update.message.reply_text(get_text('help', lang), parse_mode=ParseMode.HTML)

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menampilkan status bot: waktu aktif, RAM, dan proses aktif."""
    lang = context.user_data.get('lang', 'en')
    
    uptime = datetime.datetime.now() - BOT_START_TIME
    uptime_str = str(uptime).split('.')[0]
    ram_usage = psutil.virtual_memory().percent
    
    # Mengimpor variabel dari file conversation.py untuk mendapatkan status antrian
    try:
        from .conversation import CURRENT_CONVERSIONS, MAX_CONCURRENT_USERS
        active_processes = CURRENT_CONVERSIONS
        max_processes = MAX_CONCURRENT_USERS
    except ImportError:
        active_processes = 'N/A'
        max_processes = 'N/A'

    status_text = get_text('bot_status', lang).format(
        uptime=uptime_str,
        ram_usage=ram_usage,
        active_processes=active_processes,
        max_processes=max_processes,
        version=BOT_VERSION
    )
    
    await update.message.reply_text(status_text, parse_mode=ParseMode.HTML)

async def cancel_outside_conversation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Fungsi cancel yang bisa dipanggil di luar percakapan."""
    lang = context.user_data.get('lang', 'en')
    await update.message.reply_text(get_text('nothing_to_cancel', lang))