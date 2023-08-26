from tkinter import *

def limpar():
    display.delete(0, END)
def inserir(valor):
    display.insert(END, valor)

window = Tk()
inp = ["+", "-", "*", "/", "9", "8", "7", "<-", "4", "5", "6", "=", "1", "2", "3", "0"]
i, j = 0

window.title("Calculadora")


display = Entry(window, font="Arial 12 bold", bg = "#F9F7FF", fg="black")
display.pack()
panel = Frame(window)
for k in inp:
    btn = Button(panel, text= k, bg="#64A5FF", width=8, height=4, border=0)
    if ()

        

panel.pack()


window.mainloop()