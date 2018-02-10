import socket
import select
import sys
from threading import Thread


   
hote = "localhost"
port = 12800

connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_avec_serveur.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))

msg_recu = ""
msg_envoye = ""
class Afficheur(Thread):
   def __init(self):
      Thread.__init(self)
      
   def run(self):
      global msg_recu
      while msg_recu != b"fin" :
         servers_a_lire, wlist, xlist = select.select([connexion_avec_serveur], [], [], 0.02)        
         msg_recu = connexion_avec_serveur.recv(1024)
         print(msg_recu.decode())
         if msg_recu == b"fin":
            break     
      
class Envoyeur(Thread):
   def __init(self):
      Thread.__init(self)
      
   def run(self):
      global msg_envoye
      global msg_recu
      
      while msg_recu != b"fin":
         msg_envoye = input("")
         msg_envoye = msg_envoye.encode()
         connexion_avec_serveur.send(msg_envoye)
         if  msg_recu == b"fin":
            break
         
def startClient():
   afficheur = Afficheur()
   envoyeur = Envoyeur()
   
   afficheur.start()
   envoyeur.start()
   
   afficheur.join()
   envoyeur.join()
   
   connexion_avec_serveur.close()
   
   