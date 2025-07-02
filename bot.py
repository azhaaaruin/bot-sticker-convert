# File: bot.py (versi Manajer)
# Tugasnya hanya mendaftarkan semua handler dari file lain dan menjalankan bot.

import os
from telegram.ext import Application, CommandHandler

# Memanggil "departemen-departemen" kita
from src.conversation import conv_handler # Alur konversi
from src.commands import help_command, status_command, cancel_outside_conversation # Perintah sederhana

# --- FUNGSI UTAMA (MAIN) ---
def main() -> None:
    """Fungsi utama untuk menjalankan bot dan mendaftarkan semua handler."""
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
    if not TELEGRAM_TOKEN:
        print("FATAL ERROR: TELEGRAM_TOKEN is not set!")
        return

    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Daftarkan semua handler ke aplikasi
    application.add_handler(conv_handler) # <-- Handler utama untuk percakapan
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("cancel", cancel_outside_conversation))
    
    print("Bot v1.0 (Struktur Rapi) sedang berjalan...")
    application.run_polling()


if __name__ == "__main__":
    main()