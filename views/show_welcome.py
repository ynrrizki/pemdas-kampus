from utils.divider import divider

#  =============================================
#         Selamat Datang di Esteh
#                 Esteh🍵
#  =============================================
def show_welcome():
    # divider("=")
    # print("        Selamat Datang di Esteh          ")
    # print("                Esteh🍵                  ")
    # divider("=")
    welcome_text = "Selamat Datang di Esteh"
    esteh_text = "Esteh🍵"
    divider("=")

    # Menghitung panjang teks dan lebar garis pembatas
    welcome_length = len(welcome_text)
    esteh_length = len(esteh_text)
    divider_width = 65  # Lebar garis pembatas

    # Menghitung jumlah spasi yang diperlukan di sebelah kiri dan kanan teks selamat datang
    welcome_left_padding = (divider_width - welcome_length) // 2
    welcome_right_padding = divider_width - welcome_length - welcome_left_padding

    # Menghitung jumlah spasi yang diperlukan di sebelah kiri dan kanan teks Esteh
    esteh_left_padding = (divider_width - esteh_length) // 2
    esteh_right_padding = divider_width - esteh_length - esteh_left_padding

    # Mencetak teks selamat datang dengan spasi di sekitarnya
    print(" " * welcome_left_padding + welcome_text + " " * welcome_right_padding)

    # Mencetak teks Esteh dengan spasi di sekitarnya
    print(" " * esteh_left_padding + esteh_text + " " * esteh_right_padding)

    divider("=")