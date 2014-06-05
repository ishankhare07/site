import websocket,threading,select,sys			
print 'Enter Ctrl+] to close'
ws = websocket.create_connection('ws://aqueous-bayou-7324.herokuapp.com/')
input = [sys.stdin,ws]
while 1:
	read_input,i,j = select.select(input,[],[])
	for x in read_input:
		if x is ws:
			print ws.recv()
		elif x is sys.stdin:
			data = sys.stdin.readline()[:-1]
			if data == '\x1d':
				ws.close()
				print 'Exiting...'
				exit()
			ws.send(data)
		else:
			continue
ws.close()
