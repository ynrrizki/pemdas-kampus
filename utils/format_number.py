import locale 

locale.setlocale(locale.LC_NUMERIC, 'id_ID')

def format_number(number: int):
    return 'Rp' + locale.format_string("%.2f", number, grouping=True)