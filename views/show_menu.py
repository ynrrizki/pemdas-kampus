from utils.format_number import format_number
from utils.divider import divider

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