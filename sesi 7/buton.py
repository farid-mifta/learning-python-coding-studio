import tkinter as tk

def sapa():
    print("hallo teman teman")
window = tk.Tk()
window.title("Program Sapa")
window.geometry("300x150")

label = tk.Label(window, text="app Saya")
label.pack(padx=5)

tombol = tk.Button(window, text="Klik Saya", command=sapa)
tombol.pack()

window.mainloop()
