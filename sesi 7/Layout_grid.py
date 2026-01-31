import tkinter as tk

window = tk.Tk()
window.title ("app Gui")
window.geometry("300x200")

#label
label_nama = tk.Label(window, text="Nama: ")
label_nama.grid(row=0, column = 0)

entry_nama = tk.entry(window)
entry_nama.grid(row = 0, colomn = ` `)
