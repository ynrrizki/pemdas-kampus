import datetime
from utils.divider import divider
from utils.format_number import format_number
from utils.format_date import format_date
from models.invoice import Invoice

#  Tanggal         :  2023-09-28 05:23:07.821744
#  Menu            :  ES TEH SUSU
#  nama            :  Yanto
#  Jumlah Pesanan  :  2
#  Harga           :  Rp10.000,00
#  ---------------------------------------------
#  Total Pembayaran: Rp20.000,00
#  ---------------------------------------------



def show_invoice(menu_name, order_name, purchase_amount, price, total, discount): 
    date_now = datetime.datetime.now()
    divider("-")
    invoices = {
        1: Invoice('Tanggal', format_date(date_now)),
        2: Invoice('Menu', menu_name),
        3: Invoice('Nama', order_name),
        4: Invoice('Jumlah Pesanan', purchase_amount),
        5: Invoice('Harga Satuan', format_number(price)),
        6: Invoice('Total Pembayaran', format_number(total['before_discount'])),
        7: Invoice('Diskon', format_number(discount)),
        8: Invoice('Total Harus Dibayar', format_number(total['after_discount'])),
    }
    max_invoice_name_length = max(len(invoice_info.name) for invoice_info in invoices.values())
    for invoice_id, invoice_info in invoices.items():
        if(invoice_id == 6): 
            divider("-")
        print(f" {invoice_info.name:<{max_invoice_name_length}} : {invoice_info.description}")
        if(invoice_id == 8): 
            divider("-")
    # print(f" Tanggal             : {dateNow}")
    # print(f" Menu                : {menu_name}")
    # print(f" nama                : {order_name}")
    # print(f" Jumlah Pesanan      : {purchase_amount}")
    # print(f" Harga Satuan        : {format_number(price)}")
    # divider("-")
    # print(f" Total Pembayaran    : {format_number(total['before_discount'])}")
    # print(f" Diskon              : {format_number(discount)}")
    # print(f" Total Harus Dibayar : {format_number(total['after_discount'])}")
    # divider("-")