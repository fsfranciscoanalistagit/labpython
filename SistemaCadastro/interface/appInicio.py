from tkinter import *

class Application0:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeira mensagem")
        self.msg["font"] = ("verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1, width=5)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        #self.sair["command"] = self.widget1.quit
        #self.sair.bind("<Button-1>", self.mudar_texto)
        self.sair["command"] = self.mudar_texto
        self.sair.pack(side=RIGHT)

    #def mudar_texto(self, event):
    def mudar_texto(self):
        if self.msg["text"] == "Primeira mensagem":
            self.msg["text"] = "Recebeu um click"
        else:
            self.msg["text"] = "Primeira mensagem"

#root0 = Tk()
#Application0(root0)
#root0.mainloop()

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeirocontainer = Frame(master)
        self.primeirocontainer["pady"] = 10
        self.primeirocontainer.pack()
        
        self.segundocontainer = Frame(master)
        self.segundocontainer["padx"] = 20
        self.segundocontainer.pack()

        self.terceirocontainer = Frame(master)
        self.terceirocontainer["padx"] = 20
        self.terceirocontainer.pack()

        self.quartocontainer = Frame(master)
        self.quartocontainer["pady"] = 20
        self.quartocontainer.pack()

        self.titulo = Label(self.primeirocontainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundocontainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nomeLabel["width"] = 8

        self.nome = Entry(self.segundocontainer)
        self.nome["font"] = self.fontePadrao
        self.nome["width"] = 20
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceirocontainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senhaLabel["width"] = 8

        self.senha = Entry(self.terceirocontainer)
        self.senha["font"] = self.fontePadrao
        self.senha["width"] = 20
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartocontainer)
        self.autenticar["font"] = ("Calibri", "10", "bold")
        self.autenticar["text"] = "Autenticar"
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificar_senha
        self.autenticar.pack()

        self.mensagem = Label(self.quartocontainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificar_senha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "Admin" and senha == "123":
            self.mensagem.config(text="Autenticado!", fg="green")
        else:
            self.mensagem.config(text="Erro na Autenticação!", fg="red")



root = Tk()
Application(root)
root.mainloop()
        
