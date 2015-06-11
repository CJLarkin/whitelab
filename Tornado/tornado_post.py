import tornado.web
import tornado.httpserver
import tornado.ioloop
import json
from image_script_copy import *

out = main('Good_pic_copy.jpg')

class img_handler(tornado.web.RequestHandler):
	def post(output):
		data = json.loads(self.request.body.decode('{}'.format(output)))
		print('Got JSON data:', data)
		return data
        #self.write({ 'got' : 'your data' })

if __name__ == '__main__':
    app = tornado.web.Application(handlers=[ tornado.web.url(r'/', img_handler(out))])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8888)
    print('Starting server on port 8888')
    tornado.ioloop.IOLoop.instance().start()
