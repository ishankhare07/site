import os
import sys
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket
import json

unnamed = []
connected = {}

class WsHandler(tornado.websocket.WebSocketHandler):

	def send_message(self,sock,message):
		for client in connected.keys():
			if client is not sock:
				client.write_message('%s >> %s' %(connected[self],message))

	def open(self):
		unnamed.append(self)
		self.write_message('Enter your name : ')#this is a test

	def on_message(self,message):
		if self not in connected:
			connected[self] = message
			unnamed.remove(self)
			self.send_message(self,'Connected')
		else:
			self.send_message(self,message)
			

	def on_close(self):
		self.send_message(self, 'Disconnected')
		connected.pop(self)

class ListHandler(tornado.websocket.WebSocketHandler):
	def open(self):
		self.write_message('acknowledged')

	def on_message(self,message):
		try:
			if message.strip() == 'get':
				self.write_message(json.dumps(connected.keys()))
		except e:
			self.write_message('error detected %s' %e)

app = tornado.web.Application([
	(r'/',WsHandler),
	(r'/connected',ListHandler)
])

ws_server = tornado.httpserver.HTTPServer(app)
port = int(os.environ.get("PORT",5000))
ws_server.listen(port)
tornado.ioloop.IOLoop.instance().start()
