from Hair_TiesAplication.tiarasdb import _executar

class Tiara:

    def __init__(self):

        #se a tabela produtos não existir, crie-a
        query = 'CREATE TABLE IF NOT EXISTS tiaras (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, preco REAL)'
        _executar(query)

        query = 'DELETE FROM tiaras'
        _executar(query)
        query = 'DELETE FROM sqlite_sequence WHERE name="tiaras"'
        _executar(query)

    def data_tiaras(self):
        query = f"INSERT INTO tiaras (nome, preco) VALUES ('Laço JB', 45.0), ('Laço Butterfly', 30.0), ('Laço Moana', 40.0), ('Laço Stith', 35.0), ('Tiara Urso', 25.0)"
        _executar(query)

    @staticmethod
    def get_preco(nome):
        query= f"SELECT preco FROM tiaras WHERE nome='{nome}'"
        tiara = _executar(query)[0]

        return tiara[0]

    @staticmethod
    def get_tiaras():
        query = "SELECT * FROM tiaras"
        tiaras = _executar(query)
        return tiaras

    @staticmethod
    def get_tiara(id):
        query = f"SELECT id, nome, preco FROM tiaras WHERE id={int(id)}"
        tiara = _executar(query)[0]
        tiara = Tiara()

        return tiara