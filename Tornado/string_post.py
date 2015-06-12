import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from image_script_copy import *

from tornado.options import define, options
#define("port", default=8000, help="run on the given port", type=int)

class IndexHndlr(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', '')
        self.out = out
        self.write(greeting + '{}'.format(self.out))

def main1(out):
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHndlr)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

# if __name__ == "__main__":
# 	main1()