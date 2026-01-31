import tkinter as tk

gui = tk.Tk()
gui.title("App GUI")
gui.geometry("400x300")

button_1 = tk.Button(gui, text="Tombol di posisi x=30, y=50")
button_1.place(x=30, y = 50) 

button_2 = tk.Button(gui, text="Tombol di posisi x=150, y=120")
button_2.place(x=150, y = 120)

gui.mainloop()
