import socket

address='127.0.0.1'
port= 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: 
	cliente.connect((address,port))
	while  True:
		mensaje=input("Ingrese su mensaje: ") # se deberia elegir un nick cuando se entra al server
		cliente.send(mensaje.encode()) 
		if mensaje=="quit()": break
		data=cliente.recv(4096) #recive sus propios mensaje, no de todos
		print(data.decode())
