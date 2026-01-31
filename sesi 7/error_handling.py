import tkinter as tk
from tkinter import messagebox # untukm pop eror

window = tk.Tk()
window.title("eror handling Demo")

def hitung ():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        hasil = a /b
        label_hasil.config(text=f"Hasil: {hasil}")
    except ValueError:
        messagebox.showerror("input salah", "Harap Masukan Angka Yang valid")
    except ZeroDivisionError:
        messagebox.showerror("error matematika", "Tidaka Bisa Membagi dengan nol")        
# input angka
entry1 = tk.Entry(window, width=20)
entry1.pack(pady=5)

entry2 = tk.Entry(window, width=20)
entry2.pack(pady=5)

#button  hitung
button = tk.Button(window, text="Hitung", command=hitung)
button.pack(pady=5)

#label hasil
label_hasil = tk.Label(window, text ="masukan 2 angka lalu klik")
label_hasil.pack(pady=5)

window.mainloop()