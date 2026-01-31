import tkinter as tk

window = tk.Tk()
window.title("Form Sederhana")
window.geometry("300x150")
#fuction
def sapa ():
    nama = entry.get()
    # print(f"halo{nama}")
    label_hasil.config(text=f"Halo {nama}")
#label
label = tk.Label(window, text="Masukan Nama:")
label.pack()
#Entry
entry = tk.Entry(window)
entry.pack()
#buton
tombol = tk.Button(window, text="Sapa Saya", command=sapa)
tombol.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()
window.mainloop()
