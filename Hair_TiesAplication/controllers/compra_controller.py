from tornado.web import RequestHandler

from models.compra_model import Compra
from models.tiaras_model import Tiara


class Index(RequestHandler):

    def get(self):
        compras = Compra.get_compras()
        self.render('index.html', compras=compras)

class Nova(RequestHandler ):

    def get(self):
        tiaras = Tiara.get_tiaras()
        self.render('nova.html', tiaras=tiaras)

    def post(self):
        nome = self.get_argument('produto', None)
        #preco = self.get_argument('preco', None)
        preco = Tiara.get_preco(nome)
        comprador = self.get_argument('comprador', None)

        compra = Compra(nome=nome, preco=preco, comprador=comprador)
        compra.comprar()

        self.redirect('/')

class Cancela(RequestHandler):

    def get(self, id):
        compra = Compra.get_compra(id)
        compra.cancelar()

        self.redirect('/')