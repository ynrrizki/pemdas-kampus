from view.show_menu import show_menu
from view.show_welcome import show_welcome
from view.show_invoice import show_invoice
from view.show_form import show_form
from views.show_loading import show_loading
from models.menu import menu

def cli_screen():
    # Section Welcome
    show_welcome()    
    # Section Menu    
    show_menu(menu)
    # Section Form Input 
    form_result = show_form(menu)
    # cek hasil form input, apabila pilihan menu valid
    # Section Invoice baru dapat ditampilkan 
    show_loading()
    if (form_result['hash_menu']):
        show_invoice(
            form_result['menu']['name'], 
            form_result['order']['name'], 
            form_result['purchase_amount'], 
            form_result['menu']['price'], 
            form_result['order']['total'],
            form_result['order']['discount']
        )

def main():
    # Set Loop untuk Stop dan Melanjutkan Program
    program_loop = "y"    
    while program_loop.lower() == "y":             
        cli_screen() # fungsi screen program cli
        program_loop = input(" Mau pesan lagi? Ketik (Y/N) : ").lower()    
        
if __name__ == "__main__":
    # Run your all Program
    main()

# Hasil Tampilan
#  =============================================
#         Selamat Datang di Esteh
#                 Esteh🍵
#  =============================================

#   1. ES THAI TEA MEDIUM : Rp5.000,00
#   2. ES THAI TEA LARGE  : Rp10.000,00
#   3. ES TEH RED VELVET  : Rp15.000,00
#   4. ES TEH ORIGINAL    : Rp8.000,00
#   5. ES TEH SUSU        : Rp10.000,00

#  =============================================
#  - Nama Lengkap: Yanto
#  - Masukkan nomor menu yang Anda inginkan: 5
#  - Jumlah yang ingin dibeli: 2
#  ---------------------------------------------
#  Tanggal         :  2023-09-28 05:23:07.821744
#  Menu            :  ES TEH SUSU
#  nama            :  Yanto
#  Jumlah Pesanan  :  2
#  Harga           :  Rp10.000,00
#  ---------------------------------------------
#  Total Pembayaran: Rp20.000,00
#  ---------------------------------------------
#  Mau pesan lagi? Pilih Y jika ya, pilih N jika tidak (Y/N):


# [Dokumentasi]
# Klasifikasi Tampilan Berdasarkan function

# 1. show_welcome

#  =============================================
#         Selamat Datang di Esteh
#                 Esteh🍵
#  =============================================

# 2. show_menu


#   1. ES THAI TEA MEDIUM : Rp5.000,00
#   2. ES THAI TEA LARGE  : Rp10.000,00
#   3. ES TEH RED VELVET  : Rp15.000,00
#   4. ES TEH ORIGINAL    : Rp8.000,00
#   5. ES TEH SUSU        : Rp10.000,00

#  =============================================

# 3. show_form

#  - Nama Lengkap: Yanto
#  - Masukkan nomor menu yang Anda inginkan: 5
#  - Jumlah yang ingin dibeli: 2
#  ---------------------------------------------

# 4. show_invoice

#  Tanggal         :  2023-09-28 05:23:07.821744
#  Menu            :  ES TEH SUSU
#  nama            :  Yanto
#  Jumlah Pesanan  :  2
#  Harga           :  Rp10.000,00
#  ---------------------------------------------
#  Total Pembayaran: Rp20.000,00
#  ---------------------------------------------