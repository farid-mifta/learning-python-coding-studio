import tkinter as tk

window = tk.Tk()
window.title("app GUI")
window.geometry("300x200")

#Label 1
label_1 = tk.Label(window, text="Label 1")
label_1.pack()
#buton 1
button = tk.Button(window, text="Button)
button.pack()
#label 2
label_2 = tk.Label(window, text="Label 2")
label_2.pack()
window.mainloop()