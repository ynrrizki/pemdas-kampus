
#  - Nama Lengkap : Yanto
#  - Nomor menu (pisah dengan koma jika lebih dari 1) : 1,2
#  - Jumlah ES THAI TEA MEDIUM yang ingin dibeli: 3
#  - Jumlah ES THAI TEA LARGE yang ingin dibeli: 3
#  ---------------------------------------------

def discount_calculate(price, purchase_amount):
    if (purchase_amount >= 3):
        discount = price * 0.1
    else:
        discount = 0

    return discount


def order_calculate(list_menu, menu_choice, order_name, payment_method):
    # Dapatkan nama dan harga menu berdasarkan pilihan menu
    menu = list_menu.get(menu_choice)

    if menu:
        menu_name = menu.name
        menu_price = menu.price
        purchase_amount = int(
            input(f" - Jumlah {menu.name} yang ingin dibeli: "))
        price = menu_price * purchase_amount
        order_price_total = {
            'price': price,
            'after_ppn': (menu_price * purchase_amount) * 0.1
        }

        return {
            'hash_menu': True,
            'menu': {
                'name': menu_name,
                'price': menu_price,
            },
            'order': {
                'name': order_name,
                'total': order_price_total,
            },
            'payment_method': payment_method,
            'purchase_amount': purchase_amount,
        }
    else:
        print(" Pilihan menu tidak valid.")
        return {'hash_menu': False}


def show_form(list_menu):
    order_name = input(" - Nama Lengkap : ")
    payment_method = input(
        " - Pilih Metode Pembayaran CASH/DEBIT : ")
    debit_options = ["BCA", "CIMB NIAGA", "BNI", "BRI", "BANK MEGA"]
    index = 0
    if (payment_method.lower() == "debit"):
        for debit_option in debit_options:
            index = index + 1
            print(f"   > {index}. {debit_option}")
        choose_option_debit = int(input(" - Pilih Opsi Debit (numerik) : "))
        if (choose_option_debit == 1):
            payment_method = "BCA"
        elif (choose_option_debit == 2):
            payment_method = "CIMB NIAGA"
        elif (choose_option_debit == 3):
            payment_method = "BNI"
        elif (choose_option_debit == 4):
            payment_method = "BRI"
        elif (choose_option_debit == 5):
            payment_method = "BANK MEGA"
        else:
            payment_method = "CASH"

    menu_choices = input(
        " - Nomor menu (pisah dengan koma jika lebih dari 1) : ")
    menu_numbers = menu_choices.split(',')

    ordered_menus = []

    for menu_number in menu_numbers:
        menu_number = int(menu_number.strip())
        order_result = order_calculate(
            list_menu, menu_number, order_name, payment_method)
        if order_result['hash_menu']:
            ordered_menus.append(order_result)

    return ordered_menus
