import socket
from _thread import *
import threading
import time

def thread_accept(conn_addr): 
  cliente , direccion =conn_addr
  with cliente:
			print("se conecto: ", direccion)
			while True:	
				mensj, addr =cliente.recvfrom(4096)
				if not mensj: break
				mensaje1=str(direccion[0])+":"+str(direccion[1])+" dijo: "+mensj.decode("utf-8")
				cliente.sendall(mensaje1.encode()) #no se lo envia a todos, arreglar
				#print(direccion,"dijo: ", mensj.decode()) 

HOST = ''
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
	server.bind((HOST, PORT)) 
	print("esperando..") 
	server.listen(2) #espera un conexion

	while True:
		threading.Thread(target=thread_accept, args=(server.accept(),)).start() 
		 
