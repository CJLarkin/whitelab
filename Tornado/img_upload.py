import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options
from tornado_cors import CorsMixin
import time
import threading
from image_script_copy import *
from database import *
from inchi_to_smiles import *
import base64, re, json
import os
from PIL import Image
import cStringIO

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = 4 - len(data) % 4
    if missing_padding:
        data += b'='* missing_padding
    return base64.decodestring(data)



define("port", default=8080, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", UploadHandler),
            (r"/DataBaseUpload", DBHandler),
            (r"/conversion", ConvHandler),
            (r"/query", QueryHandler),
            (r"/DataBaseUpdate", DBUpdateHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        self.add_header('Access-Control-Allow-Origin', '*')
        image = self.get_argument('img', '')
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        m = re.search('^data:image/([a-z]*);base64,(.*)', image)
        if(not m):
            raise ValueError('Could not read POSTed image')
        extension = '.' + m.group(1)
        fname = fname+extension
        with open(fname, "wb") as f:
            f.write(decode_base64(m.group(2)))
        out = end(fname)
        self.finish('{}'.format(json.dumps(out)))

class DBHandler(tornado.web.RequestHandler):
    def post(self):
        self.add_header('Access-Control-Allow-Origin', '*')
        args = {}
        for k in self.request.arguments:
        	args[k] = self.get_argument(k)
        print args
        db_entry = db_edit(**args)
        #db_entry = db_edit(smiles, tt, tm, vis, frag, cit)
        self.finish('{}'.format(db_entry))

class ConvHandler(tornado.web.RequestHandler):
    def post(self):
        self.add_header('Access-Control-Allow-Origin', '*')
        inchi = self.get_argument('inchi','')
        smiles = conv(inchi)
        if smiles == None:
        	self.finish(None)
        else:
        	self.finish('{}'.format(smiles))

class QueryHandler(tornado.web.RequestHandler):
    def post(self):
        self.add_header('Access-Control-Allow-Origin', '*')
        query = self.get_argument('query','')
        result = db_search(query)
        self.finish('{}'.format(json.dumps(result)))

class DBUpdateHandler(tornado.web.RequestHandler):
    def post(self):
        self.add_header('Access-Control-Allow-Origin', '*')
        args = {}
        for k in self.request.arguments:
        	args[k] = self.get_argument(k)
        db_up = db_update(**args)
        #db_up = db_update(smiles, tt, tm, vis, frag, cit)
        self.finish('{}'.format(db_up))

class MyHandler(CorsMixin, tornado.web.RequestHandler):

    # Value for the Access-Control-Allow-Origin header.
    # Default: None (no header).
    CORS_ORIGIN = '*'

    # Value for the Access-Control-Allow-Headers header.
    # Default: None (no header).
    #CORS_HEADERS = 'Content-Type'

    # Value for the Access-Control-Allow-Methods header.
    # Default: Methods defined in handler class.
    # None means no header.
    CORS_METHODS = 'POST'

    # Value for the Access-Control-Allow-Credentials header.
    # Default: None (no header).
    # None means no header.
    CORS_CREDENTIALS = True

    # Value for the Access-Control-Max-Age header.
    # Default: 86400.
    # None means no header.
    CORS_MAX_AGE = 21600

    # Value for the Access-Control-Expose-Headers header.
    # Default: None
    CORS_EXPOSE_HEADERS = 'Location, X-WP-TotalPages'

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()


