import unittest
import sys
import os
sys.path.insert(0,os.path.abspath( os.path.join( os.path.dirname(__file__), '../server/') ))
import server
import carte


class CarteHelperTest(unittest.TestCase):
    
    def test_test(self):
        self.assertIsNotNone(Carte.creer_labyrinthe_depuis_chaine("test")) 
        
        
unittest.main()