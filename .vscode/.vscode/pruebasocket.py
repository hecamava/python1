from socket import *

puerto = 1
conectado = None

while puerto <= 65535:
     try:
       try:
           s = socket(AF_INET, SOCK_STREAM, 0) 
       except:
           print('Error: No se puede abrir este socket. ')      
           break
       s.connect(('localhost',puerto))

      #  s.connect(('localhost',puerto))
       conectado = True
     except Exception:
         conectado = False 
     finally:

            if conectado and puerto != s.getsockname()[1]:
                print('El puerto {} esta activo.'.format(puerto))

                puerto +=1
                s.close()