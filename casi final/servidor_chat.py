import socket
from _thread import *
import threading



def thread_accept(conn_addr,directions): 
  cliente , direccion =conn_addr
  with cliente:
			print("se conecto: ", direccion)
			directions.append(direccion) #hacer if weones de q no se conecte la misma direccion ?
				
			while True:	
				if not mensj: break
				if  mensj.decode()== "quit()":
					directions.remove(direccion) #si se va se saca de la lista
					print(direccion, " salio")

				for i in directions:
					if i== direccion:
						pass
					else:
						cliente.sendto(mensj,i) #no se lo envia a todos, arreglar
						print("sendto ", i)
				 

directions=[]
HOST = ''
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server: 
	server.bind((HOST, PORT)) 
	print("esperando..") 
	server.listen(2) #espera un conexion

	while True:
		threading.Thread(target=thread_accept, args=(server.accept(),directions)).start() 
		 


#hay q guardar la direccion de todos los q se conectan a un lista y cuando se desconecte sacarlos de la lista
#y luego se manda a el mensaje a todos menos al q lo envio. se hace con un if 
