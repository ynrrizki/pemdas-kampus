# Model Menu
class Menu:
    def __init__(self, name, price, qty_purchase_bonus = 0):
        self.name = name
        self.price = price
        self.qty_purchase_bonus = qty_purchase_bonus
        
menu = {
    1: Menu('ES THAI TEA MEDIUM', 5000),
    2: Menu('ES THAI TEA LARGE', 10000),
    3: Menu('ES TEH RED VELVET', 15000),
    4: Menu('ES TEH ORIGINAL', 8000),
    5: Menu('ES TEH SUSU', 10000),
}