import tkinter as tk

window = tk.Tk()
window. title("Label")
window.geometry("300x200")

# label 
label = tk.Label(window, text="Sapa Saya")
label.pack()

window.mainloop()