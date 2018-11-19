'''
python 3.5

comentarios para q no se me olvide , hay dos archivos serv1 y cli1
en serv se conectan todos los clientes gracias a listen y accept
para q hayan multiples clientes a la vez se usa thread se hace q una funcion sea un thread
y asi se puede utilizar de forma paralela cada vez q se conecta un cliente

arreglar de quien dijo q la direccion es la misma asi q no se deberia mostrar
'''

import socket
from _thread import *
import threading
import time

def thread_accept(conn_addr): # conn_addr es lo q se recibe del argumento de Thread
  cliente , direccion =conn_addr
  with cliente:
			print("se conecto: ", direccion)
			while True:	
				mensj, addr =cliente.recvfrom(4096)#recibe el mensaje de alguiem
				if not mensj: break
				mensaje1=str(direccion[0])+":"+str(direccion[1])+" dijo: "+mensj.decode("utf-8")
				#cliente.sendall(mensaje1.encode())
				print(direccion,"dijo: ", mensj.decode()) # se escribe el chat en el server, hay q cambiarlo para q cada cliente tenga el chat


HOST = ''
PORT = 50007

#diferencia de versiones 3.5 es mas webiado
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: #aqui se crea el socket
	server.bind((HOST, PORT)) #guarda la direccion
	print("esperando..") 
	server.listen(2) #espera un conexion

	while True:
		threading.Thread(target=thread_accept, args=(server.accept(),)).start() # se hace thread la funcion, en el argumento se dice q hacer
		
		#cliente, direccion =server.accept()#acepta al man q se une
		 
'''
#todo esto esta en la funcion 
		with cliente:
			print("se conecto: ", direccion)

			while True:	
				mensj, addr =cliente.recvfrom(4096)#recibe el mensaje de alguiem
				if not mensj:
					#print_lock.release()
					break
				mensaje1=str(direccion[0])+":"+str(direccion[1])+" dijo: "+mensj.decode("utf-8")
				#cliente.sendall(mensaje1.encode())
				print(direccion,"dijo: ", mensj)
				#ss="hola {}".format(direccion)
				#cliente.send(ss.encode()) #saluda al vato q le envio un mesaje
'''			
			#cliente.close()

