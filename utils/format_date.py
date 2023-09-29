
def format_date(date):
    nama_bulan = [
        "Januari", "Februari", "Maret", "April",
        "Mei", "Juni", "Juli", "Agustus",
        "September", "Oktober", "November", "Desember"
    ]

    # Mendapatkan hari, bulan, dan tahun
    hari = date.day
    bulan = date.month - 1  # Mengurangi 1 karena indeks dimulai dari 0
    tahun = date.year

    return f"{hari}, {nama_bulan[bulan]} {tahun}"