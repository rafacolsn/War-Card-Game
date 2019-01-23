from random import *
import random

listeCouleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
listeValeurs = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As"]

class Carte:
    """Classe de cartes"""
    def __init__(self, couleur, valeur):
        self.c = couleur
        self.v = valeur
        self.nom = "{0} de {1}".format(self.v, self.c)

class Jeu:
    """Classe du jeu de cartes"""
    def __init__(self):
        self.jeu = []
        for couleur in listeCouleurs: 
            for valeur in listeValeurs:
                c = Carte(couleur, valeur)
                self.jeu.append(c.nom)
    
    def afficher(self):
        print(self.jeu)

    def battre(self):
        random.shuffle(self.jeu)

    def tirerJeu(self):
        i = 0
        while i < 52:
            print(self.jeu[i])
            i += 1
    
    # def tirerCartesAuHasard(self, nbr):
    #     i = 1
    #     while i <= nbr:
    #         r = randint(0,51)
    #         print(self.jeu[r])
    #         i += 1

    def tirerCarte(self, n):
        return self.jeu[n]

class Joueur(Jeu):
    """Classe des joueurs"""
    def __init__(self, nom):
        Jeu.__init__(self)
        self.nom = nom

def askName():
    reply = str(raw_input("Quel est votre nom ? "))
    global j1
    j1 = Joueur(reply)

askName()
j2 = Joueur("Ordi")
j1.battre()
j2.battre()

def yes_or_no(question):
    reply = str(raw_input(question+' (o/n): ')).lower().strip()
    if reply[0] == 'o':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")

confirm = yes_or_no("{0}, voulez-vous jouer ?".format(j1.nom))

if confirm:
    c1 = j1.tirerCarte(1)
    c2 = j2.tirerCarte(1)
    print("{0}, votre carte est : {1}".format(j1.nom, c1))
    print("La carte de {0} est : {1}".format(j2.nom, c2))



