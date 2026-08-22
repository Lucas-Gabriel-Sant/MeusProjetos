from Hair_TiesAplication.db import _executar

class Compra:

    def __init__(self, nome, preco, comprador, id = None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.comprador = comprador
        print(id, nome, preco, comprador)

        #se a tabela produtos não existir, crie-a
        query = 'CREATE TABLE IF NOT EXISTS compras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL, comprador TEXT)'
        _executar(query)

    def comprar(self):
        print(self.nome, self.preco, self.comprador)
        query = f"INSERT INTO compras (nome, preco, comprador) VALUES ('{self.nome}', {float(self.preco)}, '{self.comprador}')"
        _executar(query)

    def cancelar(self):
        query = f"DELETE FROM compras WHERE id={int(self.id)}"
        _executar(query)

    @staticmethod
    def get_compras():
        query = "SELECT * FROM compras"
        compras = _executar(query)
        return compras

    @staticmethod
    def get_compra(id):
        query = f"SELECT id, nome, preco, comprador FROM compras WHERE id={int(id)}"
        compra = _executar(query)[0]
        compra = Compra(id=compra[0], nome=compra[1], preco=compra[2], comprador=compra[3])

        return compra