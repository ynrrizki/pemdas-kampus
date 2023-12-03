from views.show_title import show_title

from views.show_menu import show_menu

from views.show_invoice import show_invoice

from views.show_loading import show_loading

from views.show_form import show_form

from models.menu import menu
import os


# TODO: membersihkan screen terminal

def clear_screen():

    try:

        os.system('clear')

    except:

        os.system('cls')


# TODO: screen untuk cli system

def cli_screen():

    # Section Welcome
    show_title("Selamat Datang di Esteh")

    # Section Menu
    show_menu(menu)

    # Section Form Input

    form_results = show_form(menu)

    # Section Loading Dijalankan Sebelum Hasil invoice

    show_loading()

    # clear screen
    clear_screen()

    # Section Welcome
    show_title("Invoice")

    # cek hasil form input, apabila pilihan menu valid

    # Section Invoice baru dapat ditampilkan

    show_invoice(form_results)


# TODO: perulangan screen

def loop_screen():

    program_loop = "y"

    while program_loop.lower() == "y":
        clear_screen()
        cli_screen()

        print('')

        program_loop = input(" Mau pesan lagi? Ketik (Y/N) : ").lower()
    clear_screen()


def main():
    loop_screen()


if __name__ == "__main__":

    # Run your all Program
    main()
