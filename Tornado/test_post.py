import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
from image_script_copy import *
from tornado.options import define, options


define("port", default=8000, help="run on the given port", type=int)

class JsonHandler(tornado.web.RequestHandler):
    """Request handler where requests and responses speak JSON."""
    def prepare(self):
        # Incorporate request JSON into arguments dictionary.
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message) # Bad Request
 
        # Set up response dictionary.
        self.response = dict()
 
    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')
 
    def write_error(self, status_code, **kwargs):
        if 'message' not in kwargs:
            if status_code == 405:
                kwargs['message'] = 'Invalid HTTP method.'
            else:
                kwargs['message'] = 'Unknown error.'
 
        self.response = kwargs
        self.write_json()
 
    def write_json(self):
        output = json.dumps(self.response)
        self.write(output)

class IndexHandler(JsonHandler):
    def get(self):
    	data = json.loads(self.request.body.decode('{}'.format(main('Good_pic_copy.jpg'))))
        greeting = self.get_argument('JSON Out', 'Hello')
        self.write(greeting + ', {}'.format(data))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()





