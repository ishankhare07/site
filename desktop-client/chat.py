import thread,select,os,urllib2
from gi.repository import Gtk

class handler:
	def __init__(self,b):
		self.count = 0
		self.recv_count = 0
		self.running = True
		self.ws = websocket.create_connection('ws://aqueous-bayou-7324.herokuapp.com/')
		self.thread = thread.start_new_thread(self.backend,(self.ws,))
		self.buffer = ''
		self.builder = b
		self.entry = self.builder.get_object('entry1')

	def backend(self,ws):
		while self.running:
			read_backend,i,j = select.select([ws],[],[])
			for x in read_backend:
				if x is ws:
					try:
						msg = ws.recv()
						if self.recv_count:
							msg = '\n' + msg
						self.recv_count += 1
						self.show(msg)
					except:
						continue

	def on_delete(self,*args):
		self.ws.close()
		self.running = False
		os.system('rm websocket.py websocket.pyc')
		Gtk.main_quit(*args)

	def on_button1_clicked(self,button):
		text = self.entry.get_text()
		if text:
			self.ws.send(text)
			if self.count:
				text = '\nYou >> ' + text
			self.count += 1
			self.show(text)
			self.entry.set_text('')

	def show(self,t):
		self.buffer += t
		view = self.builder.get_object('textview')
		view.get_buffer().set_text(self.buffer)

if not os.path.isfile('chat.glade'):
	gui = urllib2.urlopen('https://dl.dropboxusercontent.com/u/83647303/chat.glade').read()
	f = open(os.getcwd()+ "/chat.glade" , 'w').write(gui)
if not os.path.isfile('websocket.py'):
	w = urllib2.urlopen('https://dl.dropboxusercontent.com/u/83647303/websocket.py').read()
	f = open(os.getcwd()+ "/websocket.py" , 'w').write(w)

import websocket
builder = Gtk.Builder()
builder.add_from_file('chat.glade')
builder.connect_signals(handler(builder))
window = builder.get_object('window1')
window.show_all()
Gtk.main()
