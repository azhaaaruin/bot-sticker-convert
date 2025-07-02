# File: bot.py (versi Manajer dengan Peningkatan Jaringan)
# Tugasnya hanya mendaftarkan semua handler dari file lain dan menjalankan bot.

import os
from telegram.ext import Application, CommandHandler
from telegram.request import Request # <-- IMPORT BARU untuk mengatur jaringan

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

    # --- PENINGKATAN JARINGAN ---
    # Kita buat bot lebih "sabar" saat mencoba terhubung ke Telegram.
    # Waktu tunggu koneksi dan baca dinaikkan menjadi 10 detik.
    request = Request(connect_timeout=10.0, read_timeout=10.0)
    
    # Masukkan pengaturan jaringan baru ke dalam Application Builder
    application = Application.builder().token(TELEGRAM_TOKEN).request(request).build()
    
    # Daftarkan semua handler ke aplikasi
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status_command))
    application.add_handler(CommandHandler("cancel", cancel_outside_conversation))
    
    print("Bot v1.0 (Struktur Rapi) sedang berjalan...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()