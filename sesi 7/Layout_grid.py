import tkinter as tk

window = tk.Tk()
window.title("Layout Grid")

# Label dan Entry dalam grid
tk.Label(window, text="Nama:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(window).grid(row=0, column=1, padx=5, pady=5)

tk.Label(window, text="Umur:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(window).grid(row=1, column=1, padx=5, pady=5)

tk.Button(window, text="Simpan").grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
