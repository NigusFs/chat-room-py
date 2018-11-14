import socket
from _thread import *
import threading

def thread_rec(a):
	print(a.decode())

address='127.0.0.1'
port= 5000


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente: 
	cliente.connect((address,port))
	
	while  True:

		mensaje=input("Ingrese su mensaje: ") # se deberia elegir un nick cuando se entra al server
		cliente.send(mensaje.encode()) 
		threading.Thread(target=thread_rec, args=(cliente.recv(4096), )).start()
		if not mensaje:
			cliente.send("quit()".encode) 
			break
		if mensaje=="quit()": break
