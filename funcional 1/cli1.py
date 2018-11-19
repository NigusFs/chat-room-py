'''
 es la mas simple, tiene q ejecutar primero serv1

'''

import socket



address='127.0.0.1' # la direccion
port= 50007 # el puerto del server



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: # se crea el socket para q haya conexion entre weas
	cliente.connect((address,port))#cliente, con esto te conectas al server
	while  True:
		mensaje=input("ingrese su mensaje: ")
		cliente.send(mensaje.encode()) # se envia el mensaje al sever
		if mensaje=="quit()": break
		

		#data = cliente.recv(1024) #sendall en server
		#print(data.decode())
		
	#s.close()
	
