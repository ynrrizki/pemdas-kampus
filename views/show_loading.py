from utils.loader import Loader
import time
from utils.divider import divider

def show_loading():
    divider("-")
    with Loader(" Sedang memproses...", " Invoice Berhasil Dibuat"):
        time.sleep(2)  # Atur waktu sesuai kebutuhan