import datetime
from utils.divider import divider
from utils.format_number import format_number
from utils.format_date import format_date
from models.invoice import Invoice
from views.show_form import discount_calculate


def show_invoice(form_results):
    date_now = datetime.datetime.now()
    invoices = {
        1: Invoice('Tanggal', format_date(date_now)),
        2: Invoice('Nama', form_results[0]['order']['name']),
        3: Invoice('Metode Pembayaran', form_results[0]['payment_method']),
    }
    max_invoice_name_length = max(len(invoice_info.name)
                                  for invoice_info in invoices.values())
    for invoice_id, invoice_info in invoices.items():
        print(
            f" {invoice_info.name:<{max_invoice_name_length}} : {invoice_info.description}")

    total_results = []
    total_before_discount = 0
    total_discount = 0
    total_after_discount = 0
    total_ppn = 0
    total_price = 0
    total_purchase_amount = 0
    for form_result in form_results:
        if (form_result['hash_menu']):
            total_result = show_invoice_tile(
                form_result['menu']['name'],
                form_result['order']['name'],
                form_result['purchase_amount'],
                form_result['menu']['price'],
                form_result['order']['total']
            )
            total_results.append(total_result)
            total_purchase_amount += total_result['purchase_amount']
            total_price += total_result['price']
            total_ppn += total_result['after_ppn']
    divider('-')

    filter_price_ppn = total_price + total_ppn
    invoices = {
        1: Invoice('Total Pembayaran', format_number(total_price)),
        2: Invoice('Total Diskon', format_number(discount_calculate(filter_price_ppn, total_purchase_amount))),
        3: Invoice('Total Kena PPN (10%)', format_number(total_ppn)),
        4: Invoice('Total Harus Dibayar', format_number(filter_price_ppn - discount_calculate(filter_price_ppn, total_purchase_amount))),
    }

    max_invoice_name_length = max(len(invoice_info.name)
                                  for invoice_info in invoices.values())

    for invoice_id, invoice_info in invoices.items():
        print(
            f" {invoice_info.name:<{max_invoice_name_length}} : {invoice_info.description}")


def show_invoice_tile(menu_name, order_name, purchase_amount, price, total):
    divider("-")
    invoices = {
        1: Invoice('Menu', menu_name),
        3: Invoice('Jumlah Pesanan', purchase_amount),
        4: Invoice('Harga Satuan', format_number(price)),
        5: Invoice('PPN (10%)', format_number(total['after_ppn'])),
    }
    max_invoice_name_length = max(len(invoice_info.name)
                                  for invoice_info in invoices.values())
    for invoice_id, invoice_info in invoices.items():
        print(
            f" {invoice_info.name:<{max_invoice_name_length}} : {invoice_info.description}")

    return {
        # "before_discount": total['before_discount'],
        # "discount": discount,
        # "after_discount": total['after_discount'],
        "price": total['price'],
        "purchase_amount": purchase_amount,
        "after_ppn": total['after_ppn']
    }
