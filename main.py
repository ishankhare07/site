import os
import sys
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket

class WsHandler(tornado.websocket.WebSocketHandler):

	def __init__(self):
		self.unnamed = []
		self.connected = {}

	def send_message(self,sock,message):
		for client in self.connected.keys():
			if client is not sock:
				client.write_message('%s >> %s' %(self.connected[self],message))

	def open(self):
		self.unnamed.append(self)
		self.write_message('Enter your name : ')#this is a test

	def on_message(self,message):
		if self not in self.connected:
			self.connected[self] = message
			self.unnamed.remove(self)
			self.send_message(self,'Connected')
		else:
			self.send_message(self,message)
			

	def on_close(self):
		self.send_message(self, 'Disconnected')
		self.connected.pop(self)

app = tornado.web.Application([
	(r'/',WsHandler),
])

ws_server = tornado.httpserver.HTTPServer(app)
port = int(os.environ.get("PORT",5000))
ws_server.listen(port)
tornado.ioloop.IOLoop.instance().start()
