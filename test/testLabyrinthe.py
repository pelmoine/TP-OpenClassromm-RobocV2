import unittest
import sys
import os
from server import labyrinthe
from server.joueur import Joueur
from server import carteHelper
from server.carteHelper import carteHelper

class TestLabyrinthe(unittest.TestCase):
    """ Test lié au méthod présente dans la classe Labyrinthe. """
    
    def testDisplay(self):
        """ Test si il exsite des fichiers dans le répertoire des cartes."""
        
        cartes = carteHelper.chargementCartes()
        for carte in cartes :
            labyrinthe =  carte.labyrinthe
            chaine = labyrinthe.display()
            self.assertIsNotNone(chaine)
            self.assertEqual(len(chaine), (labyrinthe.max_largeur+1) * labyrinthe.max_hauteur)
            
    def testCreateJoueur(self):
        """ Test la création de joueur. """
        
        # Chargement et création des données
        cartes = carteHelper.chargementCartes()
        carte = cartes[0]
        labyrinthe =  carte.labyrinthe
        info_connexion = ('12350', '192.168.1.3')
         
        # Test de la méthod
        labyrinthe.createJoueur(0,info_connexion)
        self.assertTrue(type(labyrinthe.joueurs) is dict)
        self.assertTrue(len(labyrinthe.joueurs) > 0)
        self.assertIsNotNone(labyrinthe.joueurs[info_connexion])
        self.assertTrue(type(labyrinthe.joueurs[info_connexion]) is Joueur)
            
    def testDisplayWithPlayers(self):
        """ Test l'affichage d'un labyrinthe avec plusieurs joueurs. """
        
        # Chargement et création des données
        cartes = carteHelper.chargementCartes()
        carte = cartes[0]
        labyrinthe =  carte.labyrinthe
        info_connexion_joueur_0 = ('12350', '192.168.1.3') 
        info_connexion_joueur_1 = ('12350', '192.168.1.4')       
        labyrinthe.createJoueur(0,info_connexion_joueur_0)
        labyrinthe.createJoueur(1,info_connexion_joueur_1)
        
        # Test de la méthod
        chaine = labyrinthe.displayWithPlayers(info_connexion_joueur_1)
        self.assertIsNotNone(chaine)
        self.assertIn('x', chaine)
        self.assertIn('X', chaine)
        
