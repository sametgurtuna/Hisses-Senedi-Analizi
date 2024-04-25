import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

def hisse_senedi_analizi(ticker, baslangic_tarihi, bitis_tarihi):
    try:
        # Belirtilen hisse senedi sembolünün geçerli olup olmadığını kontrol et
        if not gecerli_hisse_senedi(ticker):
            sonuc_label.config(text="Geçersiz hisse senedi sembolü.")
            return

        # Belirtilen tarih aralığında hisse senedi fiyatlarını çek
        veri = yf.download(ticker, start=baslangic_tarihi, end=bitis_tarihi)

        # Eğer veri boşsa (hisse sembolü bulunamadıysa veya veri yoksa)
        if veri.empty:
            sonuc_label.config(text="Belirtilen tarihler arasında veri bulunamadı.")
            return

        # Yeni bir pencere oluştur
        grafik_penceresi = tk.Toplevel(main_window)
        grafik_penceresi.title(f'{ticker} Hisse Senedi Analizi')

        # Grafik için figür oluştur
        fig = plt.Figure(figsize=(10, 6))

        # Kapanış fiyatlarını çiz
        ax = fig.add_subplot(111)
        ax.plot(veri.index, veri['Close'], label='Kapanış Fiyatı', color='blue', linewidth=2)
        ax.set_title(f'{ticker} Hisse Senedi Fiyatları')
        ax.set_xlabel('Tarih')
        ax.set_ylabel('Kapanış Fiyatı ($)')

        # Canvas oluştur
        canvas = FigureCanvasTkAgg(fig, master=grafik_penceresi)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    except Exception as e:
        sonuc_label.config(text="Hata: " + str(e))

def gecerli_hisse_senedi(ticker):
    # yfinance kütüphanesini kullanarak hisse senedinin mevcut olup olmadığını kontrol et
    try:
        yf.Ticker(ticker).info
        return True
    except:
        return False

def analiz_yap():
    ticker = hisse_entry.get().upper()
    baslangic_tarihi = baslangic_entry.get()
    bitis_tarihi = bitis_entry.get()
    hisse_senedi_analizi(ticker, baslangic_tarihi, bitis_tarihi)

# Ana Tkinter penceresini oluştur
main_window = tk.Tk()
main_window.title("Hisse Senedi Analizi")

# Kullanıcı girişleri için etiketler ve giriş kutuları oluştur
hisse_label = tk.Label(main_window, text="Hisse Sembolu:")
hisse_label.pack()
hisse_entry = tk.Entry(main_window)
hisse_entry.pack()

baslangic_label = tk.Label(main_window, text="Başlangıç Tarihi (YYYY-MM-DD):")
baslangic_label.pack()
baslangic_entry = tk.Entry(main_window)
baslangic_entry.pack()

bitis_label = tk.Label(main_window, text="Bitiş Tarihi (YYYY-MM-DD):")
bitis_label.pack()
bitis_entry = tk.Entry(main_window)
bitis_entry.pack()

# Analiz butonunu oluştur
analiz_button = tk.Button(main_window, text="Analiz Yap", command=analiz_yap)
analiz_button.pack()

# Sonuçları göstermek için etiket oluştur
sonuc_label = tk.Label(main_window, text="")
sonuc_label.pack()

# Tkinter penceresini başlat
main_window.mainloop()
