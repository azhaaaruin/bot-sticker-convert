# File: src/translations.py
# Ditambahkan teks untuk progres real-time

TRANSLATIONS = {
    'en': {
        # ... (semua teks dari 'choose_lang' hingga 'bot_busy' tetap sama) ...
        'choose_lang': "Please choose your language:",
        'welcome': (
            "Welcome! This bot helps you convert stickers from various platforms to be Telegram-compatible, powered by the `sticker-convert` engine.\n\n"
            "👇 <b>Supported Platforms & Requirements:</b>\n"
            "• <b>Line</b>: Supported\n"
            "• <b>KakaoTalk</b>: Supported (needs 'auth_token' for animated)\n"
            "• <b>Discord</b>: Supported (Requires Token)\n"
            "• <b>Signal</b>: Supported\n"
            "• <b>WhatsApp</b>: Supported (usually via 3rd party web links)\n"
            "• <b>Band</b>: Supported\n"
            "• <b>Viber</b>: Supported\n"
            "• <b>OGQ</b>: Supported\n\n"
            "Please select a platform to start:"
        ),
        'help': (
            "<b>Bot Help</b>\n\n"
            "This bot helps you convert sticker packs from other platforms into a Telegram-compatible format.\n\n"
            "<b>How to use:</b>\n"
            "1. Use the /start command to begin.\n"
            "2. Choose your language.\n"
            "3. Select the platform the stickers are from.\n"
            "4. Choose whether you want to create a Sticker Pack or Custom Emojis.\n"
            "5. If required, provide a token.\n"
            "6. Send the sticker pack link when prompted.\n\n"
            "The bot will then send you the converted files, which you can forward to the @Stickers bot to create your pack.\n\n"
            "<b>Available Commands:</b>\n"
            "/start - Begin a new conversion.\n"
            "/help - Show this help message.\n"
            "/status - Show the bot's current status.\n"
            "/cancel - Cancel the current operation."
        ),
        'bot_status': (
            "<b>Bot Status</b>\n\n"
            "🟢 <b>State</b>: Online\n"
            "⏳ <b>Uptime</b>: {uptime}\n"
            "💾 <b>RAM Usage</b>: {ram_usage}%\n"
            "🔄 <b>Active Processes</b>: {active_processes} / {max_processes}\n"
            "⚙️ <b>Version</b>: {version}"
        ),
        'bot_busy': (
            "🚧 <b>Bot is Currently Busy</b> 🚧\n\n"
            "Sorry, all processing slots are currently in use. Please try again in a few moments."
        ),
        'choose_output': "✅ Platform: <b>{platform}</b>\n\nNow, what would you like to create?",
        'output_sticker': "Sticker (for Packs)",
        'output_emoji': "Custom Emoji",
        'request_url': "✅ Great! You chose to create <b>{output_name}</b> from <b>{platform}</b>.\n\nPlease send the sticker pack URL or ID.\n\nType /cancel to stop.",
        'request_token': "This platform requires a token. Please send your token first.\n\nType /cancel to stop.",
        'token_received': "✅ Token received. Now, what would you like to create from <b>{platform}</b>?",
        'url_received': "✔️ Link received. Starting conversion with preset <b>{preset}</b>. Please wait...",
        
        # --- TEKS PROGRES BARU ---
        'progress_start': "Starting process...",
        'progress_found': "🔍 Found {count} items...",
        'progress_downloading': "📥 Downloading: {current}/{total}",
        'progress_converting': "⚙️ Converting: {current}/{total}",
        'progress_finished': "✅ Process finished! Sending files now...",

        'success': "Success! All {count} items have been sent.",
        'error': "Sorry, an error occurred during conversion.\n\n<code>{error_message}</code>",
        'no_files': "Conversion finished, but no files were produced. The link might be invalid or the pack empty.",
        'timeout': "Sorry, the conversion process took too long and was stopped. Please try with a smaller pack.",
        'unexpected_error': "An unexpected error occurred: {e}",
        'guide_sticker_title': "✅ <b>Sticker Pack Guide</b> ✅",
        'guide_sticker_body': "Forward the files above to @Stickers and follow these steps:\n1. Send /newpack.\n2. Choose sticker type (Static/Video).\n3. Give your pack a name.\n4. <b>Forward</b> a file from me when prompted.\n5. Send one matching emoji.\n6. Repeat for all stickers.\n7. Send /publish and set a short name for your pack's link.",
        'guide_emoji_title': "✅ <b>Custom Emoji Guide</b> ✅",
        'guide_emoji_body': "Forward the files above to @Stickers and follow these steps:\n1. Send /newemojipack.\n2. Choose emoji type (Static/Video).\n3. Give your emoji pack a name.\n4. <b>Forward</b> a file from me when prompted.\n5. Send one matching emoji as a shortcut.\n6. When done, send /publish.",
        'cancelled': "Process cancelled. Send /start to begin again.",
        'nothing_to_cancel': "There is no active operation to cancel."
    },
    'id': {
        # ... (semua teks dari 'choose_lang' hingga 'bot_busy' tetap sama) ...
        'choose_lang': "Silakan pilih bahasa Anda:",
        'welcome': (
            "Selamat datang! Bot ini membantu Anda mengonversi stiker dari berbagai platform agar kompatibel dengan Telegram, ditenagai oleh engine `sticker-convert`.\n\n"
            "👇 <b>Platform & Persyaratan yang Didukung:</b>\n"
            "• <b>Line</b>: Didukung\n"
            "• <b>KakaoTalk</b>: Didukung (butuh 'auth_token' untuk animasi)\n"
            "• <b>Discord</b>: Didukung (Membutuhkan Token)\n"
            "• <b>Signal</b>: Didukung\n"
            "• <b>WhatsApp</b>: Didukung (biasanya via link web pihak ketiga)\n"
            "• <b>Band</b>: Didukung\n"
            "• <b>Viber</b>: Didukung\n"
            "• <b>OGQ</b>: Didukung\n\n"
            "Silakan pilih platform untuk memulai:"
        ),
        'help': (
            "<b>Bantuan Bot</b>\n\n"
            "Bot ini membantu Anda mengonversi paket stiker dari platform lain ke format yang kompatibel dengan Telegram.\n\n"
            "<b>Cara menggunakan:</b>\n"
            "1. Gunakan perintah /start untuk memulai.\n"
            "2. Pilih bahasa Anda.\n"
            "3. Pilih platform asal stiker.\n"
            "4. Pilih apakah Anda ingin membuat Paket Stiker atau Emoji Kustom.\n"
            "5. Jika diperlukan, berikan token.\n"
            "6. Kirim link paket stiker saat diminta.\n\n"
            "Bot akan mengirimkan Anda file yang telah dikonversi, yang dapat Anda teruskan ke bot @Stickers untuk membuat paket Anda.\n\n"
            "<b>Perintah yang Tersedia:</b>\n"
            "/start - Memulai konversi baru.\n"
            "/help - Menampilkan pesan bantuan ini.\n"
            "/status - Menampilkan status bot saat ini.\n"
            "/cancel - Membatalkan operasi yang sedang berjalan."
        ),
        'bot_status': (
            "<b>Status Bot</b>\n\n"
            "🟢 <b>Keadaan</b>: Online\n"
            "⏳ <b>Waktu Aktif</b>: {uptime}\n"
            "💾 <b>Penggunaan RAM</b>: {ram_usage}%\n"
            "🔄 <b>Proses Aktif</b>: {active_processes} / {max_processes}\n"
            "⚙️ <b>Versi</b>: {version}"
        ),
        'bot_busy': (
            "🚧 <b>Bot Sedang Sibuk</b> 🚧\n\n"
            "Maaf, semua slot pemrosesan sedang digunakan. Silakan coba lagi beberapa saat."
        ),
        'choose_output': "✅ Platform: <b>{platform}</b>\n\nSekarang, Anda ingin membuat apa?",
        'output_sticker': "Stiker (untuk Pack)",
        'output_emoji': "Emoji Kustom",
        'request_url': "✅ Siap! Anda memilih untuk membuat <b>{output_name}</b> dari <b>{platform}</b>.\n\nSilakan kirimkan link atau ID dari pack stiker tersebut.\n\nKetik /batal untuk membatalkan.",
        'request_token': "Platform ini membutuhkan token. Silakan kirimkan token Anda terlebih dahulu.\n\nKetik /batal untuk membatalkan.",
        'token_received': "✅ Token diterima. Sekarang, Anda ingin membuat apa dari <b>{platform}</b>?",
        'url_received': "✔️ Link diterima. Memulai proses konversi dengan preset <b>{preset}</b>. Mohon tunggu...",

        # --- TEKS PROGRES BARU ---
        'progress_start': "Memulai proses...",
        'progress_found': "🔍 Ditemukan {count} item...",
        'progress_downloading': "📥 Mengunduh: {current}/{total}",
        'progress_converting': "⚙️ Mengonversi: {current}/{total}",
        'progress_finished': "✅ Proses selesai! Mengirim file sekarang...",

        'success': "Berhasil! Semua {count} item telah terkirim.",
        'error': "Maaf, terjadi kesalahan saat konversi.\n\n<code>{error_message}</code>",
        'no_files': "Konversi selesai, tapi tidak ada file yang dihasilkan. Link mungkin tidak valid atau pack kosong.",
        'timeout': "Maaf, proses konversi terlalu lama dan terpaksa dihentikan. Coba dengan pack yang lebih kecil.",
        'unexpected_error': "Terjadi kesalahan tak terduga: {e}",
        'guide_sticker_title': "✅ <b>Panduan Menambahkan Stiker</b> ✅",
        'guide_sticker_body': "Teruskan (forward) file di atas ke @Stickers dan ikuti langkah ini:\n1. Kirim /newpack.\n2. Pilih jenis stiker (Statis/Video).\n3. Beri nama pack Anda.\n4. <b>Forward</b> file dari bot ini saat diminta.\n5. Kirim satu emoji yang sesuai.\n6. Ulangi untuk semua stiker.\n7. Kirim /publish dan atur nama pendek untuk link pack Anda.",
        'guide_emoji_title': "✅ <b>Panduan Menambahkan Emoji Kustom</b> ✅",
        'guide_emoji_body': "Teruskan (forward) file di atas ke @Stickers dan ikuti langkah ini:\n1. Kirim `/newemojipack`.\n2. Pilih jenis emoji (Statis/Video).\n3. Beri nama pack emoji Anda.\n4. <b>Forward</b> file dari bot ini saat diminta.\n5. Kirim satu emoji yang sesuai sebagai shortcut.\n6. Jika sudah, kirim `/publish`.",
        'cancelled': "Proses dibatalkan. Kirim /start untuk memulai lagi.",
        'nothing_to_cancel': "Tidak ada operasi aktif untuk dibatalkan."
    }
}