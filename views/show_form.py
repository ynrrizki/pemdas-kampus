
#  - Nama Lengkap: Yanto
#  - Masukkan nomor menu yang Anda inginkan: 5
#  - Jumlah yang ingin dibeli: 2
#  ---------------------------------------------

def order_calculate(list_menu, menu_choice, order_name): 
    # Dapatkan nama dan harga menu berdasarkan pilihan menu
    menu = list_menu.get(menu_choice)
    
    if menu:
        menu_name = menu.name
        menu_price = menu.price
        purchase_amount = int(input(" - Jumlah yang ingin dibeli: "))
        order_discount_total = discount_calculate(menu, purchase_amount)     
        order_price_total = {
            'before_discount': menu_price * purchase_amount,
            'after_discount': (menu_price * purchase_amount) - order_discount_total
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
                'discount': order_discount_total
                
            },
            'purchase_amount': purchase_amount,
        }
    else:
        print(" Pilihan menu tidak valid.")
        return {'hash_menu': False}

def discount_calculate(menu, purchase_amount):
    if (purchase_amount >= 3):
        discount = menu.price * 0.1
    else:
        discount = 0
    
    return discount    
    

def show_form(list_menu):
    order_name = input(" - Nama Lengkap : ")
    
    while True:
        menu_choice = input(" - Masukkan nomor menu : ")
        
        # Cek apakah input adalah angka
        if menu_choice.isdigit():
            menu_choice = int(menu_choice)
            break
        else:
            print(" Hanya ada pilihan 1-5. Silakan coba lagi.")
    
    return order_calculate(list_menu, menu_choice, order_name)
