from tkinter import *
from tkinter import messagebox
import tkinter as tk


def help():
    MsgBox = tk.messagebox.askquestion('Exit App', 'Отримати допомогу?')
    if MsgBox == 'no':
        tk.messagebox.showinfo('Help', 'З поверненням!')
    else:
        from main4 import webview

def ExitApp():
    MsgBox = tk.messagebox.askquestion('Exit App', 'Ви бажаєте вийти?')
    if MsgBox == 'yes':
        window.destroy()
    else:
        tk.messagebox.showinfo('Welcome Back', 'З поверненням!')


def click_button2():
    messagebox.askyesno("Generator", "Ви бажаєте вийти?")
def click_button1():
    messagebox.showwarning("Generator", "Запуск CMD...")
    messagebox.askokcancel("Gemerator", "Щоб користуватися программою перемістіться в CMD")
    from main2 import start



window = Tk()
window.title("Генератор Паролів!")
window.geometry('435x150')

lbl = Label(window, text="ГЕНЕРАТОР", fg="black", font=("Arial Bold", 20))
lbl2 = Label(window, text="Для того, щоб ваші персональні дані", fg="red", font=("Arial Bold", 10))
lbl3 = Label(window, text="залишалися в безпеці необхідно продумувати", fg="red", font=("Arial Bold", 10))
lbl4 = Label(window, text=" надійні паролі для захисту ваших акаунтів!", fg="red", font=("Arial Bold", 10))
lbl5 = Label(window, text=" Генератор паролів (secure password generator)", fg="red", font=("Arial Bold", 10))
lbl.grid(column=1, row=0)
lbl2.grid(column=1, row=1)
lbl3.grid(column=1, row=2)
lbl4.grid(column=1, row=3)
lbl5.grid(column=1, row=4)
btn = Button(window, text="ГЕНЕРАЦІЯ", bg="red", fg="white", width=20, command=click_button1)
btn2 = Button(window, text="ВИХІД", bg="green", fg="white", width=20, command=ExitApp)
btn3 = Button(window, text="ДОПОМОГА", bg="blue", fg="white", width=20, command=help)
btn.grid(column=0, row=1)
btn3.grid(column=0, row=2)
btn2.grid(column=0, row=3)

window.mainloop()
