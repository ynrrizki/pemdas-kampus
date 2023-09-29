from utils.format_number import format_number
from utils.divider import divider



#   1. ES THAI TEA MEDIUM : Rp5.000,00
#   2. ES THAI TEA LARGE  : Rp10.000,00
#   3. ES TEH RED VELVET  : Rp15.000,00
#   4. ES TEH ORIGINAL    : Rp8.000,00
#   5. ES TEH SUSU        : Rp10.000,00

#  =============================================

def show_menu(menu):

    max_menu_name_length = max(len(menu_info.name) for menu_info in menu.values())

    print("")

    for menu_id, menu_info in menu.items():
        
        price = format_number(menu_info.price)

        menu_name = menu_info.name
        
        formatted_menu_name = f"{menu_name:<{max_menu_name_length}}"

        print(f"  {menu_id}. {formatted_menu_name} : {price}")
    print("")

    divider("=")