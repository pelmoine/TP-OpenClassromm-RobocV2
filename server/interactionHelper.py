# -*-coding:Utf-8 -*


"""Ce module contient les interactions avec l'utilisateur."""

import re

def demandeNomJoueur():
    """ Sauvegarde le nom du joueur dans une variable globale. """
    
    nom_joueur = input("Saisissez votre pseudo : ")
    while len(nom_joueur) < 1 :
        nom_joueur = input("Merci de réessayer, saisissez votre pseudo : ")
    
    return nom_joueur

def bienvenue():
    """ Message de bienvenue à l'utlisateur. """
    
    return "\nBienvenue sur Roboc multijoueur en ligne !! \n\
Vous etes le joueur n {}, voici vos informations de connexion : {} \n\
Lancez la partie en appuyant sur la touche 'c' quand vous le souhaitez."

def rappelDesCommandes():
    """ Affiche le rappel des commandes. """
    
    return b"Un client a lance la partie ! \n Rappel des commandes : \n \
Le robot est controlable grace a des commandes entrees au clavier :\n\n \
Q qui doit permettre de sauvegarder et quitter la partie en cours.\n \
N qui demande au robot de se deplacer vers le nord (c'est-a-dire le haut de votre ecran).\n \
E qui demande au robot de se deplacer vers l'est (c'est-a-dire la droite de votre ecran).\n \
S qui demande au robot de se deplacer vers le sud (c'est-a-dire le bas de votre ecran).\n \
O qui demande au robot de se deplacer vers l'ouest (c'est-a-dire la gauche de votre ecran).\n\n \
Chacune des directions ci-dessus suivies d'un nombre permet d'avancer de plusieurs cases (par exemple E3 pour avancer de trois cases vers l'est).\n\n\
M pour murer une porte suivie de la lettre representant la direction.\n\
P pour percer une porte dans un mur suivie de la lettre representant la direction.\n\n"

def clientStopPartie():
    """ Une des joueurs à stoppée la partie. """
    
    return "\nLe joueur n {} (info : {}) a stoppe la partie. Au revoir."

def confirmerStopPlay():
    """ Demande une confirmation à l'utilisateur lorsqu'il veut quitter ça partie. """
    
    if yesNoQuestion("Etes-vous vraiment sûr de vouloir quitter le jeu ? O/N : ") :
        return True
    print("Continuons la partie !")
    return False

def confirmerNouvellePartie():
    """ Demande une confirmation à l'utilisateur lorsqu'il veut commencer une nouvelle partie. """
    
    if yesNoQuestion("Etes-vous vraiment sûr de vouloir commencer une nouvelle partie ? \
    \nCela entrainera la suppression de votre sauvegarde sur les précédantes partie avec ce pseudo. O/N : ") :
        print("Ancienne partie supprimée. Commençons une nouvelle partie !")
        return True
    
    return False

def yesNoQuestion(question):
    """ Fonction générique utilisée pour les yes no question à l'utilisateur """
    confirmation = ''
    yes_no_rex = re.compile("^[oOyYnN]{1}$")    
    while not yes_no_rex.match(confirmation):
        confirmation = input(question)
        if confirmation.lower() == 'o' or confirmation.lower() == 'y' :
            return True
        else :
            return False

def reprendrePartie():
    """ Demdande si l'utilisateur souhaire reprendre ou continuer la partie"""
    return yesNoQuestion("Voulez-vous reprendre votre partie ? O/N : ")

def mauvaiseStartLettre():
    """ Mauvaise lettre pour commencer. """
    return (b"Mauvaise lettre, pour commencer la partie veuillez entrer la lettre 'c'")

def joueurGagnePartie(clients_connectes, connexion_avec_client,infos_connexion):
    """ Un joueur a gagné la partie. """
    return "le joueur {} ({}) a trouve la sortie, il a gagne.".format(clients_connectes.index(connexion_avec_client),infos_connexion)

def aurevoir():
    return "fin"

def erreurSaisie():
    return "Erreur de saisie, merci de vous référer au rappel des commandes. \n"