# -*-coding:Utf-8 -*


import socket
import select
from server.carteHelper import carteHelper
from server import interactionHelper
import re
from server.carte import Carte

# Définition des variables globales au fichier 
MOUVEMENT_REX = re.compile("^[nsoeNSOE]{1}[0-9]*$")
MURER_PERCER_REX = re.compile("^[mpMP]{1}[nsoeNSOE]{1}$")
HOTE = ''
PORT = 12800

def sendAll(players, message):
    """ Fonction permettant d'envoyer un message à tous les joueurs. """
    
    for player in players:
        player.send(message)
 
def sendAllLabyrinthe(labyrinthe, players):
    """ Fonction permettant d'envoyer le labyrinthe personnalisé par joueur. """
    for player in players:
        player.send(labyrinthe.displayToByteArray(player.getpeername()))   
        
def choixCarteServer():
    """ On charge les cartes existantes, puis on les affiche et enfin on return le choix de l'utilisteur. """ 
    
    cartes= carteHelper.chargementCartes()
    carteHelper.afficheLabyrinthes(cartes)
    return (carteHelper.choixCartes(cartes))


def getLabyrintheFromChoixCarte(choix_carte):
    """ On charge les cartes et selectionne celle passée en paramètre. """
    
    cartes= carteHelper.chargementCartes()    
    return cartes[choix_carte-1].labyrinthe
    

def startServer():
    # Sélection de la carte à jouer et définition du labyrinthe
    choix_carte = choixCarteServer()
    labyrinthe = getLabyrintheFromChoixCarte(choix_carte) 
    
    # Connexion de la socket.
    connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_principale.bind((HOTE, PORT))
    connexion_principale.listen(5)
    print("Le serveur écoute à présent sur le port {}".format(PORT))
    
    quitter = False
    win = False
    clients_connectes = []
    partie_start = False
    while not quitter and not win:
        
        #coute de la connexion_principale en lecture pour ajouter les nouveaux clients
        connexions_demandees, wlist, xlist = select.select([connexion_principale],[], [], 0.05)
        
        for connexion in connexions_demandees:
            connexion_avec_client, infos_connexion = connexion.accept()
            # On ajoute le socket connecté à la liste des clients
            clients_connectes.append(connexion_avec_client)
            # Création du joueur
            labyrinthe.createJoueur(clients_connectes.index(connexion_avec_client),infos_connexion)
            message_bienvenue = interactionHelper.bienvenue().format(clients_connectes.index(connexion_avec_client),infos_connexion)
            connexion_avec_client.send(message_bienvenue.encode())
            
        # On écoute la liste des clients connectés
        # Les clients renvoyés par select sont ceux devant être lus (recv)
        clients_a_lire = []
        try:
            clients_a_lire, wlist, xlist = select.select(clients_connectes,
                    [], [], 0.05)
        except select.error:
            pass
        else: 
            
            for client in clients_a_lire: 
                msg_recu = client.recv(1024)
                msg_recu = msg_recu.decode()
                infos_connexion = client.getpeername()
            
                # si le serveur reçoit la lettre 'q' alors on arrête la partie            
                if msg_recu.lower() == "q":
                    message_client_stop_partie = interactionHelper.clientStopPartie().format(clients_connectes.index(connexion_avec_client),infos_connexion)
                    sendAll(clients_connectes, message_client_stop_partie.encode())
                    sendAll(clients_connectes, b"fin")
                    quitter = True
                # si le server reçoit la lettre c alors on commence la partie avec les joeurs connectés
                if not partie_start and msg_recu.lower() == "c":
                    sendAll(clients_connectes,interactionHelper.rappelDesCommandes())
                    sendAllLabyrinthe(labyrinthe, clients_connectes)
                    partie_start = True
                    break
                # si le server reçoit une autre lettre que 'c' et que la partie n'est pas commencé
                if not partie_start and msg_recu.lower() != "c":
                        client.send(interactionHelper.mauvaiseStartLettre())
                if partie_start:
                    
                    #Si je recois un mouvement compréhensible alors je déplace le robot
                    if MOUVEMENT_REX.match(msg_recu) :
                        is_moved = labyrinthe.move(msg_recu,infos_connexion)
        
                        if labyrinthe.sortieTrouvee(infos_connexion) :
                            sendAll(clients_connectes,interactionHelper.joueurGagnePartie(clients_connectes, connexion_avec_client,infos_connexion).encode())
                            
                            sendAll(clients_connectes, interactionHelper.aurevoir().encode())
                            sendAll(clients_connectes, b"fin")
                            win = True
                        else :
                            client.send(is_moved + labyrinthe.displayToByteArray(infos_connexion))
                    
                    elif MURER_PERCER_REX.match(msg_recu):
                        is_murer_percer = labyrinthe.murerPercer(msg_recu,infos_connexion)
                        client.send(is_murer_percer + labyrinthe.displayToByteArray(infos_connexion))
                        
                    else:
                        client.send(interactionHelper.erreurSaisie().encode())                
                        
    print("Fermeture des connexions")
    
    for client in clients_connectes:
        client.close()
    
    connexion_principale.close()
