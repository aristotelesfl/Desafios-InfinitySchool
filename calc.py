from tkinter import *

def limpar():
    display.delete(0, END)
def inserir(valor):
    display.insert(END, valor)

window = Tk()
inp = ["+", "-", "*", "/", "9", "8", "7", "<-", "4", "5", "6", "=", "1", "2", "3", "0"]
i, j = 0, 0

window.title("Calculadora")


display = Entry(window, font="Arial 12 bold", bg = "#F9F7FF", fg="black")
display.pack()
panel = Frame(window)
panel.pack()
for k in inp:
    Button(panel, text= k, bg="#64A5FF", width=8, height=4, border=0, command=lambda txt=k: inserir(txt)).grid(row=i, column=j)
    j += 1
    if j>3:
        j = 0
        i += 1
        




window.mainloop()
