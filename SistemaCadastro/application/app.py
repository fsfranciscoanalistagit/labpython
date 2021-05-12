from application.usuario import Usuario
from tkinter import *
"""
Estudante: Francisco Sales
Programa deve receber dados para cadastro de um usuário, através da interface gráfica e 
salvar no banco de dados, utilizando recursos existentes no python.
1-Utilizar banco de dados sqlite3 para armazenar os dados. Criar classe de conexão
2-Criar uma classe com os atributos e métodos reponsáveis pela comunicação do banco com a interface
3-Criar a interface gráfica para comunicação com o usuário
referencia:
https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956
"""

class Application:
    def __init__(self, master=None):        
        self.fonte = ("Verdana", "8")
        self.container1 = Frame(master)
        self.container1["pady"] = 5
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["pady"] = 5
        self.container2["padx"] = 20
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["pady"] = 5
        self.container3["padx"] = 20
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["pady"] = 5
        self.container4["padx"] = 20
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["pady"] = 5
        self.container5["padx"] = 20
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["pady"] = 5
        self.container6["padx"] = 20
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["pady"] = 5
        self.container7["padx"] = 20
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["pady"] = 5
        self.container8["padx"] = 20
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados: ")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbid = Label(self.container2, text="Id", font=self.fonte).pack(side=LEFT)
        self.txtid = Entry(self.container2)
        self.txtid["font"] = self.fonte
        self.txtid.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", command=self.buscarUsuario).pack(side=RIGHT)

        self.lbNome = Label(self.container3, text="Nome", font=self.fonte)
        self.lbNome.pack(side=LEFT)
        self.txtNome = Entry(self.container3)
        self.txtNome["font"] = self.fonte
        self.txtNome.pack(side=LEFT)

        self.lbTelefone = Label(self.container4, text="Telefone", font=self.fonte, width=10).pack(side=LEFT)
        self.txtTelefone = Entry(self.container4)
        self.txtTelefone["width"] = 25
        self.txtTelefone["font"] = self.fonte
        self.txtTelefone.pack(side=LEFT)

        self.lbEmail = Label(self.container5, text="Email", font=self.fonte, width=10).pack(side=LEFT)
        self.txtEmail = Entry(self.container5)
        self.txtEmail["width"] = 25
        self.txtEmail["font"] = self.fonte
        self.txtEmail.pack(side=LEFT)

        self.lbUsuario = Label(self.container6, text="Usuario", font=self.fonte, width=10).pack(side=LEFT)
        self.txtUsuario = Entry(self.container6)
        self.txtUsuario["width"] = 25
        self.txtUsuario["font"] = self.fonte
        self.txtUsuario.pack(side=LEFT)

        self.lbSenha = Label(self.container7, text="Senha", font=self.fonte, width=10).pack(side=LEFT)
        self.txtSenha = Entry(self.container7)
        self.txtSenha["width"] = 25
        self.txtSenha["font"] = self.fonte
        self.txtSenha.pack(side=LEFT)

        self.btnInserir = Button(self.container8, text="Inserir", command=self.inserir_usuario).pack(side=LEFT)
        self.btnAlterar = Button(self.container8, text="Alterar", command=self.Alterar_usuario).pack(side=LEFT)
        self.btnExcluir = Button(self.container8, text="Excluir", command=self.Excluir_usuario).pack(side=LEFT)

        self.lbMsg = Label(self.container9, text="")
        self.lbMsg["font"] = ("Verdana", "8", "italic")
        self.lbMsg.pack()


    def buscarUsuario(self):
        user = Usuario()
        user.id = self.txtid.get()

        self.lbMsg["text"] = user.select_user()

        self.txtid.delete(0, END)
        self.txtid.insert(INSERT, user.id)

        self.txtNome.delete(0, END)
        self.txtNome.insert(INSERT, user.nome)

        self.txtTelefone.delete(0, END)
        self.txtTelefone.insert(INSERT, user.telefone)

        self.txtEmail.delete(0, END)
        self.txtEmail.insert(INSERT, user.email)

        self.txtUsuario.delete(0, END)
        self.txtUsuario.insert(INSERT, user.usuario)

        self.txtSenha.delete(0, END)
        self.txtSenha.insert(INSERT, user.senha)


    def inserir_usuario(self):
        user = Usuario()
        user.nome = self.txtNome.get()
        user.telefone = self.txtTelefone.get()
        user.email = self.txtEmail.get()
        user.usuario = self.txtUsuario.get()
        user.senha = self.txtSenha.get()

        self.lbMsg["text"] = user.insert_user()
        self.Limpar_campos()

    def Alterar_usuario(self):
        user = Usuario()
        user.id = self.txtid.get()
        user.nome = self.txtNome.get()
        user.telefone = self.txtTelefone.get()
        user.email = self.txtEmail.get()
        user.usuario = self.txtUsuario.get()
        user.senha = self.txtSenha.get()

        self.lbMsg["text"] = user.update_user()
        self.Limpar_campos()


    def Excluir_usuario(self):
        user = Usuario()
        user.id = self.txtid.get()
        self.lbMsg["text"] = user.delete_user()

    def Limpar_campos(self):
        self.txtid.delete(0, END)
        self.txtNome.delete(0, END)
        self.txtTelefone.delete(0, END)
        self.txtEmail.delete(0, END)
        self.txtUsuario.delete(0, END)
        self.txtSenha.delete(0, END)


root = Tk()
Application(root)
root.mainloop()
        

