import tkinter as tk

win = tk.Tk()
win.title("Auto create letter outlook (ACLO)")
win.geometry("500x400+100+200")
win.resizable(False, False)
photo = tk.PhotoImage(file="icon.png")
win.iconphoto(False, photo)


win.mainloop()