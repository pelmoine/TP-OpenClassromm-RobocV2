# -*-coding:Utf-8 -*

import random
from server.joueur import Joueur
"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self,max_largeur,max_hauteur, position_sortie,grille):
        self.max_largeur = max_largeur
        self.max_hauteur = max_hauteur
        self.joueurs={}
        self.position_sortie = position_sortie
        self.grille = grille


    def display(self):
        """Permet d'afficher la grille du labyrinthe"""
        j=1
        i=1
        chaine = ""
        while (j<=self.max_hauteur):
            i=1
            while(i<=self.max_largeur):
                chaine += self.grille[i,j]
                i += 1
            chaine +="\n"
            j += 1
        
        return chaine
    
    def displayWithPlayers(self, infos_connexion):
        """Permet d'afficher la grille du labyrinthe"""
        j=1
        i=1
        chaine = ""
        while (j<=self.max_hauteur):
            i=1
            while(i<=self.max_largeur):
                is_position_joueur = False
                for cle, valeur in self.joueurs.items():
                    if valeur.position[0] == i and valeur.position[1] == j:
                        if cle == infos_connexion:
                            chaine += 'X'
                            is_position_joueur= True
                            break
                        else :
                            chaine += 'x'
                            is_position_joueur = True
                            break
                if not is_position_joueur:
                    chaine += self.grille[i,j]
                    
                i += 1
            chaine +="\n"
            j += 1
        
        return chaine
    
    def displayToByteArray(self,infos_connexion):
        b = bytearray()
        b.extend(map(ord, self.displayWithPlayers(infos_connexion)))        
        return b        
    
    def murerPercer (self, commande, infos_connexion):
        """ Murer un mûr ou percer une porte. """
        
        if 'p' == commande[0].lower():
            return self.percer(commande[1].lower(), infos_connexion)
        if 'm' == commande[0].lower():
            return self.murer(commande[1].lower(), infos_connexion)
            
    def murer(self, direction, infos_connexion):
        """ Murer une porte. """
        
        if self.murerPossible(direction, infos_connexion):
            if 'e' == direction:
                self.grille[self.joueurs[infos_connexion].position[0] +1, self.joueurs[infos_connexion].position[1] ] = 'O'
            if 'o' == direction:
                self.grille[self.joueurs[infos_connexion].position[0] -1, self.joueurs[infos_connexion].position[1] ] = 'O'
            if 's' == direction:
                self.grille[self.joueurs[infos_connexion].position[0] , self.joueurs[infos_connexion].position[1] +1] = 'O'
            if 'n' == direction:
                self.grille[self.joueurs[infos_connexion].position[0] , self.joueurs[infos_connexion].position[1] -1] = 'O'
                
            return b"Murage possible. \n"
        else:
            return b"Murage impossible. \n"
            
    def percer(self, direction, infos_connexion):
        """ Percer un mur pour créer une porte. """
        
        if self.percerPossible(direction, infos_connexion) :
            if 'e' == direction:
                self.grille[self.joueurs[infos_connexion].position[0] +1, self.joueurs[infos_connexion].position[1] ] = '.'
            if 'o' == direction:
                self.grille[self.joueurs[infos_connexion].position[0] -1 , self.joueurs[infos_connexion].position[1] ] = '.'
            if 's' == direction:
                self.grille[self.joueurs[infos_connexion].position[0]  , self.joueurs[infos_connexion].position[1] +1] = '.'
            if 'n' == direction:
                self.grille[self.joueurs[infos_connexion].position[0]  , self.joueurs[infos_connexion].position[1] -1] = '.'
            return b"Percage possible. \n"   
        else:
            return b"Percage impossible. \n"
            
    def percerPossible(self, direction, infos_connexion) :
        """ Vérifie si percer un mur est bien présent pour percer la porte. """
        
        if 'e' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0] +1, self.joueurs[infos_connexion].position[1] ]
        if 'o' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0] -1 , self.joueurs[infos_connexion].position[1] ]
        if 's' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0]  , self.joueurs[infos_connexion].position[1] +1]
        if 'n' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0]  , self.joueurs[infos_connexion].position[1] -1]
            
        return 'O' == cible 
    
    def murerPossible(self, direction, infos_connexion) :
        """ Vérifie si percer un mur est bien présent pour percer la porte. """
        
        if 'e' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0] +1, self.joueurs[infos_connexion].position[1] ]
        if 'o' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0] -1 , self.joueurs[infos_connexion].position[1] ]
        if 's' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0]  , self.joueurs[infos_connexion].position[1] +1]
        if 'n' == direction:
            cible = self.grille[self.joueurs[infos_connexion].position[0]  , self.joueurs[infos_connexion].position[1] -1]
            
        return '.' == cible
    
    def move(self, commande, infos_connexion):
        """Permet de déplacer votre robot sur la carte du labyrinthe et affiche la grille mise à jour"""
        
        # Récupération de la direction ainsi que du nombre de déplacement
        direction = commande[0].lower()
        # si l'utilisateur n'a pas saisie de nombre de déplacement alors il est de 1 par défaut.
        nb_deplacement = 1
        if len(commande) > 1:
            nb_deplacement = int(commande[1:])
            
        if not self.deplacementPossible(direction, nb_deplacement, infos_connexion):
            return b"Deplacement impossible, un mur vous empeche d'effectuer ce deplacement \n"
        else:
            self.calculNouvellePosition( direction,nb_deplacement, infos_connexion)
            return b"Deplacement possible \n"
            
    def sortieTrouvee(self, infos_connexion):
        """Renvoi True si le joueur a trouvé la sortie, False sinon"""
        return self.joueurs[infos_connexion].position == self.position_sortie
        
    def calculNouvellePosition(self, direction,nb_deplacement, infos_connexion):
        """Calcul la nouvelle position du robot en fonction de la direction et du nombre de déplacement saisie"""
        if direction=='n':
            self.joueurs[infos_connexion].position[1]  -=  nb_deplacement
        elif direction=='s':
            self.joueurs[infos_connexion].position[1]  +=  nb_deplacement
        elif direction=='e':
            self.joueurs[infos_connexion].position[0]  += nb_deplacement
        elif direction=='o':
            self.joueurs[infos_connexion].position[0]  -=  nb_deplacement        
        

    def deplacementPossible(self,direction, nb_deplacement, infos_connexion):
        """Retourne True si  si le déplacement est possible, False sinon"""
        
        deplacement_possible = True
        
        if direction == "n":
            deplacement_possible=self.deplacementNordPossible(nb_deplacement, infos_connexion)
        elif direction == 's':
            deplacement_possible=self.deplacementSudPossible(nb_deplacement,infos_connexion)
        elif direction == 'e':
            deplacement_possible=self.deplacementEstPossible(nb_deplacement,infos_connexion)
        elif direction == 'o':
            deplacement_possible=self.deplacementOuestPossible(nb_deplacement,infos_connexion)
        else :
            raise Exception("La direction rentrée est différente des lettres autorisées ('n','s','e','o')")

        return deplacement_possible
            
    def deplacementNordPossible(self, nb_deplacement, infos_connexion):
        """On vérifie si le déplacement vers le Nord est possible"""
        
        # si le déplacement n'est pas sur la carte on retourne false
        if self.joueurs[infos_connexion].position[1]  - nb_deplacement < 1 :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.joueurs[infos_connexion].position[0] , self.joueurs[infos_connexion].position[1] -i] == 'O':
                return False
            i+=1
         # si rien ne bloque la trajectoire on retourne True
        return True
        
    def deplacementSudPossible(self, nb_deplacement, infos_connexion):
        """On vérifie si le déplacement vers le Sud est possible"""
        
        # si le déplacement n'est pas sur la carte on retourne false
        if self.joueurs[infos_connexion].position[1]  + nb_deplacement < 1 :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.joueurs[infos_connexion].position[0] , self.joueurs[infos_connexion].position[1] +i] == 'O':
                return False
            i+=1
         # si rien ne bloque la trajectoire on retourne True
        return True
                 
    def deplacementOuestPossible(self, nb_deplacement, infos_connexion):
        """On vérifie si le déplacement vers l'Ouest est possible"""
    
        # si le déplacement n'est pas sur la carte on retourne false
        if self.joueurs[infos_connexion].position[0]  - nb_deplacement > self.max_largeur  :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.joueurs[infos_connexion].position[0] -i, self.joueurs[infos_connexion].position[1] ] == 'O':
                return False
            i+=1
        # si rien ne bloque la trajectoire on retourne True
        return True
    
    def deplacementEstPossible(self, nb_deplacement, infos_connexion):
        """ On vérifie si le déplacement vers l'Est est possible. """ 
                    
        # si le déplacement n'est pas sur la carte on retourne false
        if self.joueurs[infos_connexion].position[0]  + nb_deplacement > self.max_largeur  :
            return False
        # si il y a un mûr sur la trajectoire on retourne false
        i=1
        while i<=nb_deplacement:
            if self.grille[self.joueurs[infos_connexion].position[0] +i, self.joueurs[infos_connexion].position[1] ] == 'O':
                return False
            i+=1
         # si rien ne bloque la trajectoire on retourne True
        return True
    
    def createJoueur(self, index, info_connexion):
        """ """
        i = 1
        j = 1
        
        while self.grille[i, j] != ' ' and self.grille[i, j] != '.' : 
            i = random.randint(1, self.max_largeur)
            j = random.randint(1, self.max_hauteur)
            
        self.joueurs[info_connexion]= Joueur(index, info_connexion, i ,j )
        