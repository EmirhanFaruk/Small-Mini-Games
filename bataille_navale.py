
# Modification date: Thu Dec 30 20:58:16 2021

# Production date: Sun Sep  3 15:42:58 2023

#les imports
#Pour les chaines des charactères colorées
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

#Pour faire attendre
import time

#Pour l'IA
import random 

#Pour effacer les vieux trucs dans la console
from clear_screen import clear # clear()


class Carte:
    def __init__(self, joueur, longueur, hauteur, bateaux):
        self.joueur = joueur
        self.longueur = longueur
        self.hauteur = hauteur
        self.la_carte = [[" 0", "A|", "|B|", "|C|", "|D|", "|E|", "|F|", "|G|", "|H|", "|I|", "|J|"]]
        self.alphabet = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10}
        self.alphabet_list = [" 0", "|A|", "|B|", "|C|", "|D|", "|E|", "|F|", "|G|", "|H|", "|I|", "|J|"]

        for h in range(self.hauteur):
            if h != 9:
                self.la_carte.append([" " + str(h + 1)])
            else:
                self.la_carte.append([str(h + 1)])
            for l in range(self.longueur):
                self.la_carte[-1].append(["|_|"])
        print(self.la_carte)
        print(len(self.la_carte))
        print(len(self.la_carte[0]))
        

    def montre_carte(self, willbeclear):
        if willbeclear:
            clear()
        for h in range(len(self.la_carte)):
            if h == 0:
                la_ligne = " 0|"
            else:
                la_ligne = ""
            for l in range(self.longueur):
                if h == 0:
                    if l != 0:
                        la_ligne = la_ligne + self.la_carte[h][l+1][0] + self.la_carte[h][l+1][1] + self.la_carte[h][l+1][2]
                    else:
                        la_ligne = la_ligne + self.la_carte[h][l+1][0] + self.la_carte[h][l+1][1]
                elif l == 0:
                    la_ligne = la_ligne + self.la_carte[h][l][0] + self.la_carte[h][l][1]
                else:
                    la_ligne = la_ligne + self.la_carte[h][l][0]
            print(la_ligne)


class Bateau():
    n_bd3 = 0
    n_bd2 = 0
    n_bd1 = 0
    def __init__(self, x_et_y, direction):
        self.x_et_y = x_et_y
        self.direction = direction
        #les nombres des bateaux
        if len(self.x_et_y) == 3:
            Bateau.n_bd3 += 1
        elif len(self.x_et_y) == 2:
            Bateau.n_bd2 += 1
        elif len(self.x_et_y) == 1:
            Bateau.n_bd1 += 1


        

    
    



def main():
    carte1 = Carte("1", 5, 5, [])
    carte1.montre_carte(True)
    return

main()