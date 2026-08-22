from tornado import ioloop
from tornado import httpserver
from tornado.web import Application

from controllers.compra_controller import Index, Nova, Cancela
from models.tiaras_model import Tiara

class RunApp(Application):

    def __init__(self):
        handlers = [
            ('/', Index),
            ('/compra/nova', Nova),
            (r'/compra/cancel/(\d+)', Cancela)
        ]

        settings = dict(
            debug = True,
            template_path = 'views',
            static_path = 'static',
        )

        tiara = Tiara()
        tiara.data_tiaras()

        Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    http_server = httpserver.HTTPServer(RunApp())
    http_server.listen(4000)
    ioloop.IOLoop.instance().start()