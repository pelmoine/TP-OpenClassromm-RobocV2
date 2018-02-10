# -*-coding:Utf-8 -*


"""Ce module contient les fonctions liées au carte."""

# class object contenant des méthodes associées
from server.carte import Carte
import os
import re

CARTE_DIRECTORY = "./resources/cartes/"

def chargementCartes():
    """ Charge les carte et initialise les labyrinthe """
    
    cartes = []
    listcarte = os.listdir(CARTE_DIRECTORY)
    for nom_fichier in listcarte :
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join(CARTE_DIRECTORY, nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                cartes.append(Carte(nom_carte,contenu))
                
    return cartes

def chargementCarte(nom_fichier):
    """ Chargement de la carte associée au nom du fichier et initialise le labyrinthe associé à cette carte"""
    
    for nom_fichier_carte in os.listdir("cartes"):
        if nom_fichier_carte.endswith(".txt") and nom_fichier_carte == nom_fichier:
            chemin = os.path.join("cartes", nom_fichier_carte)
            nom_carte = nom_fichier_carte[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                return Carte(nom_carte,contenu) 
                

def choixCartes(cartes):
    """ Permet à l'utilisateur d'effectuer le choix d'un labyrinthe."""
    
    choix_carte = 0
    while choix_carte <= 0 or choix_carte>len(cartes) :
        choix_carte = input(" veuillez entrer un chiffre entre 1 et {}, afin de selectionner un labyrinthe : ".format(len(cartes)))
        rex = re.compile("^[0-9]*$")
        if not rex.match(choix_carte) :
            choix_carte = 0
        else :
            choix_carte = int(choix_carte)
            
    return choix_carte


def afficheLabyrinthes(cartes):
    """ Affiche la liste des labyrinthes existants. """
    
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
        print(carte.labyrinthe.display())
