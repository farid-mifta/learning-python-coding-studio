import tkinter as tk # import library tkinter

window = tk.Tk()
window.title("App GUI")

# Label 1
label_1 = tk.Label(window, text="Label 1")
label_1.pack()

# button 1
button_1 = tk.Button(window, text="Button")
button_1.pack()

# Label 2
label_2 = tk.Label(window, text="Label 2")
label_2.pack()

window.mainloop()
