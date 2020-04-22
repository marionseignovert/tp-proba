class Game:

    def __init__(self):
        self.chevre1 = Door(False, False, False)
        self.chevre2 = Door(False, False, False)
        self.voiture = Door(False, False, True)
        self.portes = [self.chevre1, self.chevre2, self.voiture]

    def init_game(self):
        pass

    def choix_porte(self, i):
       portechoisi = self.portes[i]
       portechoisi.designe = True


    def reveal(self, i):
        porteouvert = self.portes[i]
        porteouvert.ouverte = True


    def open(self, i):
        porte = self.portes[i]
        if i == 2:
            print("vous avez gagné")
        else :
            porte.ouverte = True
            print("vous avez perdu")






class Door:

    def __init__(self, ouverte, designe, gagnante):
        self.ouverte = ouverte
        self.designe = designe
        self.gagnante = gagnante


game = Game()
game.choix_porte(1)
game.reveal(0)
game.open(1)

"""
first_door = Game().chevre1
Game().open(first_door)
"""