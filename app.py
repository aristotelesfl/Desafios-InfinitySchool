from tkinter import *
from tkinter import messagebox
from tkinter import ttk

agenda = []

def updateTable():
    for i in table.get_children():
        table.delete(i)

    for i in agenda:
        table.insert("", END, values=(i["Nome"], i["Telefone"], i["Categoria"]))

def tableClique(event):
    contato_selecionado = table.selection()
    if not contato_selecionado:
        return
    index = table.index(contato_selecionado)
    contato = agenda[index]
    limparCampos()
    name.insert(0,contato["Nome"])
    telefone.insert(0,contato["Telefone"])
    cb_categoria.set(contato["Categoria"])


def adicionarContato()->None:
    nome = name.get()
    tel = telefone.get()        
    cat = cb_categoria.get()
    contato = {
        "Nome": nome,
        "Telefone": tel,
        "Categoria": cat
    }
    agenda.append(contato)
    messagebox.showinfo("Adicionado!","Contato adicionado")
    limparCampos()
    updateTable()

def editarContato()->None:
    contato_selecionado = table.selection()
    if not contato_selecionado:
        return
    index = table.index(contato_selecionado)
    agenda[index] = {
        "Nome": name.get(),
        "Telefone": telefone.get(),
        "Categoria": cb_categoria.get()
    }
    updateTable()
    limparCampos()

def deletarContatos()->None:
    contato_selecionado = table.selection()
    if not contato_selecionado:
        return
    index = table.index(contato_selecionado)
    del agenda[index]
    limparCampos()
    updateTable()


def limparCampos():
    name.delete(0, END)
    telefone.delete(0, END)
    cb_categoria.delete(0, END)

window = Tk()

window.title("Agenda Telefonica")

label_name = Label(window, text="Nome:")
label_name.grid(row=0, column=0)

name = Entry(window, width=27)
name.grid(row=0, column=1)

label_tel = Label(window, text="Telefone:")
label_tel.grid(row=1, column=0)

telefone = Entry(window, width=27)
telefone.grid(row=1, column=1)

label_categoria = Label(window, text="Categorias: ")
label_categoria.grid(row=2, column=0)

categorias = ["Amigos", "Familia", "Trabalho"]
cb_categoria = ttk.Combobox(window, values=categorias)
cb_categoria.grid(row=2, column=1)

bot_adc= Button(window, text="adicionar", bg="white", command=adicionarContato)
bot_adc.grid(row=3, column=0)

bot_edit= Button(window, text="editar", bg="white", command=editarContato)
bot_edit.grid(row=3, column=1)

bot_del= Button(window, text="excluir", bg="white", command=deletarContatos)
bot_del.grid(row=3, column=2)

table = ttk.Treeview(window, columns=("Nome", "Telefone", "Categoria"), show="headings")
table.heading("Nome", text="Nome")
table.heading("Telefone", text="Telefone")
table.heading("Categoria", text="Categoria")
table.bind("<ButtonRelease-1>", tableClique)
table.grid(row=4, columnspan=3)




window.mainloop()