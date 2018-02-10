# -*-coding:Utf-8 -*


"""Ce module contient la classe Joueur."""

class Joueur:

    """Classe représentant un Joueur."""

    def __init__(self,index, info_connexion, i, j):
        self.index = index
        self.info_connexion = info_connexion
        self.position = [i,j]
        
        print("Joueur créé : index={}, info_connex={}, postion={}".format(self.index, self.info_connexion, self.position))