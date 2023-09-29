# Model Menu
class Invoice:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
menu = {
    1: Invoice('ES THAI TEA MEDIUM', 5000),
    2: Invoice('ES THAI TEA LARGE', 10000),
    3: Invoice('ES TEH RED VELVET', 15000),
    4: Invoice('ES TEH ORIGINAL', 8000),
    5: Invoice('ES TEH SUSU', 10000),
}