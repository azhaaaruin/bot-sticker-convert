# File: bot.py (Versi Paling Sederhana dan Stabil)

import os
from telegram.ext import Application, CommandHandler
from telegram.constants import Update # <-- Tambahan import untuk allowed_updates

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

    # --- KEMBALI KE BUILDER STANDAR ---
    # Kita tidak mengatur jaringan secara manual untuk menghindari error import.
    # Kita biarkan library menggunakan pengaturan default yang sudah dioptimalkan.
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Daftarkan semua handler ke aplikasi
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("cancel", cancel_outside_conversation))
    
    print("Bot v1.0 (Struktur Rapi) sedang berjalan...")
    
    # Menjalankan bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()