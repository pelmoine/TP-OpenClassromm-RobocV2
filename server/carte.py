# -*-coding:Utf-8 -*
from server.labyrinthe import Labyrinthe

"""Ce module contient la classe Carte."""

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    
    def __init__(self, nom, chaine):
        """ Initialisation de l'objet classe. """
        self.nom = nom
        self.labyrinthe = self.creer_labyrinthe_depuis_chaine(chaine)
        
    def __repr__(self):
        return "<Carte {}>".format(self.nom)
    
    def creer_labyrinthe_depuis_chaine(self,chaine):
        """ Parcours de la chaine de caractère du fichier et ajout de chaque éléméent dans un dictionnaire
        dont la clé est un tuple. """ 
        grille={}
        
        i=1
        taille_ligne = 0
        j=1 
        for char in chaine:
            if char ==  '\n' :
                j +=1
                
                # On lève une exeption si la carte n'a pas le mm nombre de caractère par ligne
                if taille_ligne is not 0 and taille_ligne is not i:
                    raise Exception("Il semblerait que la carte ne soit pas cohérente la ligne {0} a {1} caractère(s) alors que la ligne {2} à  \
                    {} caractère(s). Merci de faire en sorte que toutes les lignes est le même nombre de caractère")
                taille_ligne = i
                i = 1
            if char != '\r' and char != '\n':
                
                # On enregistre la position initial du joueur
                if char == 'X':
                    char=' '
                # On enregistre la position de la sortie
                if char == 'U':
                    position_sortie = [i,j] 
                 
                     
                grille[i,j]=char
                i += 1
            
                
        # On créé un objet Labyrinthe
        return Labyrinthe( taille_ligne -1, j,position_sortie,grille)
            