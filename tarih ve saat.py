import tkinter as tk
from datetime import datetime

def update_time():
    # Şu anki tarih ve zamanı al
    now = datetime.now()

    # Tarih ve saat formatlarını ayarla
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d %a")

    # Label'lara tarih ve saatleri yazdır
    time_label.config(text=current_time)
    date_label.config(text=current_date)

    # Fonksiyonu 1 saniyede bir tekrar çağır
    root.after(1000, update_time)

# Ana pencereyi oluştur
root = tk.Tk()
root.title("Clock")

# Pencereyi ortala
root.geometry("300x150")
root.configure(bg="black")

# Tarih etiketi
date_label = tk.Label(root, text="", font=("Courier", 16), fg="cyan", bg="black")
date_label.pack(pady=10)

# Saat etiketi
time_label = tk.Label(root, text="", font=("Courier", 32, "bold"), fg="cyan", bg="black")
time_label.pack()

# Zamanı güncelleyen fonksiyonu çağır
update_time()

# Uygulamayı başlat
root.mainloop()
