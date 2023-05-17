import socket, os, time

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) # creo socket

dir_socket = input("Introduzca la dirección del servidor: ") 
puerto = input("Introduzca el puerto del servidor: ")
if not dir_socket:
    dir_socket = 'localhost'
if not puerto:
    puerto = '16013'
try:
    ss.bind((dir_socket, int(puerto)))
except:
    print("Error al asignar una dirección al servidor")

while True:  
    data, dirc = ss.recvfrom(1024)
    pid = os.fork()
    if pid: # padre, proceso servidor. 
        continue
    else: # hijo, proceso que gestiona el hijo
        print("El cliente" , dirc , "ha pedido la hora")
        tiempo = time.ctime(time.time())
        ss.sendto(tiempo.encode('utf8'),dirc)
        
        ss.close()
        print("El cliente" , dirc , "ha cerrado conexión")
        exit()
