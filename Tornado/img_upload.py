import tornado.httpserver, tornado.ioloop, tornado.options, tornado.web, os.path, random, string
from tornado.options import define, options
from tornado_cors import CorsMixin
import time
import threading
from image_script_copy import *
import base64
import os
from PIL import Image
import cStringIO


define("port", default=8888, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", UploadHandler)
        ]
        tornado.web.Application.__init__(self, handlers)

class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        image = self.get_argument('img', '')
        #img_recovered = base64.decodestring(image)
        #file1 = self.request.files['img_recovered'][0]
        #original_fname = file1['filename']
        #extension = os.path.splitext(original_fname)[1]
        fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
        #final_filename = fname+extension
        #output_file = open("uploads/" + final_filename, 'w')
        #output_file.write(file1['body'])
        #output_file.close()
        #print 'recieved post'
        self.add_header('Access-Control-Allow-Origin', '*')
        #pic = cStringIO.StringIO()
        #image_string = cStringIO.StringIO(base64.b64decode(image))
        #image = Image.open(image_string)
        #image.save(pic, image.format)
        #pic.seek(0)
        f = open("{}.txt".format(fname), "wb")
        f.write(image)
        f.close()
        f.open('r')
        img = base64.b64decode(f.read())
        #with open("{}.jpg".format(fname),"wb") as f:
            #f.write(base64.decodestring(img))
        #image = 'uploads/{}'.format(final_filename)
        out = end(img)
        #self.finish('{}'.format(out))

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


