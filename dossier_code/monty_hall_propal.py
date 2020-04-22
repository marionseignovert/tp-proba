from random import randint


# Je vous propose de simplifier la partie modélisation et de n'utiliser qu'une seule classe Game
# La classe Game comporte 3 attributs:
# porte_gagnante = le numéro de la porte gagnante
# porte_designe = le numéro de la porte désignée par le joueur
# porte_ouverte = le numéro de la porte ouverte par le présentateur

class Game:

    def __init__(self):
        # Je vous propose d'introduire l'aléatoire comme ceci:
        self.porte_gagnante = randint(0, 2) # On tire un nombre au hasard entre 0 et 2 : ce sera le numéro de la voiture gagante
        self.porte_designe = -1  # Au début aucune porte n'est désignée
        self.porte_ouverte = -1  # Au début aucune porte n'est ouverte

    def choix_porte(self, i):
       self.porte_designe = i

    def reveal(self):
        # TODO: le présentateur ouvre une porte selon les conditions suivantes:
        # on se place du point de vue du joueur, donc on n'a pas la main sur le choix du présentateur (j'ai donc retiré le paramètre i)
        # le présentateur ouvre la porte qui n'est pas désignée par le joueur ET qui n'est pas gagnante
        # pour réveler la porte, on changera la valeur de l'attribut self.porte_designe
        print("Le présentateur révèle une porte")

    def open(self, change_porte):
        # TODO: Afficher le message "vous avez gagné" quand l'utilisateur choisi d'ouvrir la porte gagnante
        # On prend en paramètre change_porte: un booléen qui indique si le joueur change de porte ou non
        # Si le joueur de change pas de porte, alors on ouvre la porte designée
        # Si le joueur change de porte, alors on ouvre la porte fermée (non désignée et non ouverte)
        # on utilisera les attributs self.porte_designee, self.porte_ouverte et self.porte_gagnante
        print("--> Gagné ou Perdu?")

    def display(self):
        # Méthode pour afficher l'état des portes
        for i in range(0, 3):
            print("---> Porte", i, end=" ")
            if self.porte_ouverte == i:
                print("ouverte par le présentateur", end=" ")
            if self.porte_gagnante == i:
                print("gagnante", end=" ")
            if self.porte_designe == i:
                print("désignée par le joueur", end= " ")
            if not self.porte_ouverte == i:
                print("(fermée)", end="")
            print()


"""
Déroulé de la partie
"""

# Initialisation du jeu
game = Game()
print("Au départ:")
game.display()

# Choix de la porte par le joueur
print("Le joueur choisi une porte:")
game.choix_porte(1)
game.display()

# Ouverture de la porte par le présentateur
game.reveal()
game.display()

# Choix final de la porte
print("Le joueur indique s'il change de porte ou non")
game.open(False)  # le joueur ne change pas de porte et ouvre la porte désignée au départ
