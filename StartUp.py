from tkinter import *

root = Tk()
root.geometry('300x300')
frame_login = Frame(root)
frame_login.pack(expand='yes')
Entry(frame_login, font=('fira code', 10), width=10).pack()
Button(frame_login, text='Host').pack()
Button(frame_login, text='Join').pack()
root.mainloop()
