from application.banco import Banco

class Usuario(object):
    def __init__(self, id="", nome="", telefone="", email="", usuario="", senha=""):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insert_user(self):
        banco = Banco()
        try:
           c = banco.conexao.cursor()
           #c.execute("insert into usuarios( nome, telefone, email, usuario, senha) values('"
           #          + self.nome + "','" + self.telefone + "','" + self.email + "','" +
           #          self.usuario + "','" + self.senha + "')")

           c.execute("insert into usuarios(nome, telefone, email, usuario, senha) values(?, ?, ?, ?, ?)",
                     (self.nome, self.telefone, self.email, self.usuario, self.senha))

           banco.conexao.commit()
           c.close()
           return "Usuário cadastrado com sucesso!"
        except:
           return"Falha ao enviar o usuário"

    def update_user(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            #c.execute("update usuarios set nome = '" + self.nome + "', telefone ='" + self.telefone +
            #          "',email= '" + self.email + "', usuario = '" + self.usuario + "', senha = '" +
            #          self.senha + "' where id = " + self.id + " ")
            #c.execute(f"update usuarios set nome = '{self.nome}', telefone ='{self.telefone}',email= '{self.email}', "
            #          f"usuario = '{self.usuario}', senha = '{self.senha}' where id = {self.id}")

            c.execute(f"update usuarios set nome = ?, telefone = ?, email= ?, "
                      f"usuario = ?, senha = ? where id = ? ",
                      (self.nome, self.telefone, self.email, self.usuario, self.senha, self.id))

            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Falha ao atualizar o usuário: {e}"

    def delete_user(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute(f"delete from usuarios where id = {self.id}")
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Erro ao excluir usuário! {e}"

    def select_user(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("select * from usuarios where id = ?", (self.id))

            for linha in c:
                self.id = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            resp = "Sem registro!" if not self.nome else "Busca realizada com sucesso!"

            c.close()
            return resp
        except Exception as e:
            return f"Falha na busca do usuário! {e}"

if __name__ == '__main__':
    user = Usuario()
    user.id = 2
    user.nome = "Adriana Araujo"
    user.telefone = "3232-2255"
    user.email = "adriana@adriana.com.br"
    user.usuario = "Adriana"
    user.senha = "123"
    print("==" * 20)
    print(user.select_user())
    print("==" * 20)
    #print(user.id, user.nome, user.telefone, user.email, user.usuario, user.senha)
    print()