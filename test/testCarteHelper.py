import unittest

import os
import sys
from server import carteHelper
from server import carte
from server.carte import Carte
from server.labyrinthe import Labyrinthe
from server.carteHelper import carteHelper

CARTE_DIRECTORY = "./resources/cartes/"

class CarteHelperTest(unittest.TestCase):
    """ Class de test lié au fonction contenu dans le fichier carteHelper. """
    
    
    def testFichierDansRepertoireCartes(self):
        """ Test si il exsite des fichiers dans le répertoire des cartes."""
        
        listcarte = os.listdir(CARTE_DIRECTORY)
        self.assertIsNotNone(listcarte) 
        self.assertGreater(len(listcarte), 0)
          
    def testChargementCartes(self):
        """ Test si le chargement des cartes se fait correctement ainsi que le labyrinthe associé. """
        cartes = carteHelper.chargementCartes()
        self.assertIsNotNone(cartes) 
        self.assertGreater(len(cartes), 0)
        
        for carte in cartes :
            self.assertTrue(type(carte) is Carte)
            self.assertIsNotNone(carte.nom) 
            self.assertIsNotNone(carte.labyrinthe) 
            self.assertTrue(type(carte.labyrinthe) is Labyrinthe)
            self.assertIsNotNone(carte.labyrinthe.max_largeur) 
            self.assertIsNotNone(carte.labyrinthe.max_hauteur) 
            self.assertIsNotNone(carte.labyrinthe.position_sortie) 
            self.assertIsNotNone(carte.labyrinthe.grille) 
    
