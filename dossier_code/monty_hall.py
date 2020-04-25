from random import *

class Game:

    def __init__(self):
        porte_win = randint(0, 2)
        self.porte_gagnante = porte_win
        self.porte_ouverte = -1
        self.porte_designe = -1
        #print("Porte gagnante :", self.porte_gagnante)


    def init_game(self):
        pass

    def choix_porte(self):
        self.porte_designe = randint(0, 2)
        #print("Porte Choisie : ",self.porte_designe)


    def reveal(self):
        if self.porte_designe == self.porte_gagnante:
            porte_a_ouvrir = randint(0,2)
            while porte_a_ouvrir == self.porte_gagnante:
                porte_a_ouvrir = randint(0,2)
            #porteouvert = self.portes[i]
            #porteouvert.ouverte = True
            #print("Porte ouverte : ",porte_a_ouvrir)
            self.porte_ouverte = porte_a_ouvrir

        else:
            porte_a_ouvrir = randint(0, 2)
            while porte_a_ouvrir == self.porte_designe or porte_a_ouvrir == self.porte_gagnante:
                porte_a_ouvrir = randint(0, 2)
            #print("Porte ouverte :", porte_a_ouvrir)
            self.porte_ouverte = porte_a_ouvrir


    def open(self, changement):
        if changement == 1:
            if self.porte_designe == self.porte_gagnante:
                #print("Vous avez perdu")
                return "Loose"
            else:
                #print("Vous avez gagné")
                return "Win"
        elif changement == 0:
            if self.porte_designe == self.porte_gagnante:
                #print("Vous avez gagné")
                return "Win"
            else:
                #print("Vous avez perdu")
                return "Loose"
        else:
            print("Vous avez rentré un paramètre faux")


game = Game()
game.choix_porte()
game.reveal()
game.open(1)


"""
first_door = Game().chevre1
Game().open(first_door)
"""