
# Modification date: Fri Dec 31 22:13:24 2021

# Production date: Sun Sep  3 15:42:58 2023

import random
def main():	
	class Mine:
		def __init__(self, nom, coordonnées, signe = "#", fake_coordonnées = [], vrai_signe = "*"):
			self.nom = nom
			self.vrai_coordonnées = coordonnées
			self.signe = signe
			self.vrai_signe = vrai_signe
			le_fake_nombre = random.randint(0, 2)
			if le_fake_nombre == 0:
				le_fake_nombre = -1
			else:
				le_fake_nombre = 1
			self.coordonnées = [int(self.vrai_coordonnées[0]) + le_fake_nombre, int(coordonnées[1])]
	
	    
		def joueur_mis_son_pied(self, other):
			if self.coordonnées == other.coordonnées:
				return True
			else:
				return False
	
	class Robot:
		def __init__(self, nom, coordonnées, signe, direction = None):
			"""
			Cette function crée une objet "Robot" avec nom comme string, coordonnées comme un liste avec x et y qui sont integers (x, y), et direction comme "droite", "gauche", "haut" ou "bas".
			"""
			self.signe = signe
			self.coordonnées = coordonnées
			self.vrai_coordonnées = coordonnées
			self.direction = direction
			self.nom = nom
	
	    #avancer
		def avancer(self):
			if self.direction == "6":
				self.coordonnées[0] += 1
			elif self.direction == "4":
				self.coordonnées[0] -= 1
			elif self.direction == "8":
				self.coordonnées[1] -= 1
			elif self.direction == "5":
				self.coordonnées[1] += 1
	    
	    
	
	
	Scout = Robot("Scout", [0, 0], "S", "droite")
	
	
	
	import os
	
	clear = lambda: os.system('clear')
	
	clear()
	
	input("Bienvenue à Minmarche! L'objectif est d'aller à l'autre côté. Mais attention! Il y a des mines dans ton chemin! Si tu vois un #, ça veut dire qu'il y a un mine soit à gauche, soit à droite. Bonne chance(Ce n'est pas certain que tu vas survivre)!")
	
	carte = []
	def hl():
		hauteur = input("hauteur de la carte: ")
		longueur = input("longueur de la carte: ")
		return hauteur, longueur
	hauteur, longueur = hl()
	if hauteur == None or hauteur == "":
		hauteur = 15
	if longueur == None or longueur == "":
		longueur = 15
	
	while not type(hauteur) == int and not type(longueur) == int:
		try:
			hauteur = int(hauteur)
			longueur = int(longueur)
		except:
			hauteur, longueur = hl()
		
	
	
	
	robots = []
	
	
	for i in range(hauteur):
		for j in range(longueur//4):
			nombre_au_hazard = random.randint(3, longueur-4)
			for r in range(len(robots)):
				robots_actuelle = robots[r]
				while nombre_au_hazard == robots_actuelle.coordonnées[1]:
					nombre_au_hazard = random.randint(3, longueur-4)
			robots.append(Mine("Mine" + str(i), [nombre_au_hazard, i]))
	
	robots.append(Scout)
	input("Nombre des mines: " + str(len(robots) - 1))
	clear()
	
	
	for l in range(hauteur):
		carte.append([])
		for h in range(longueur):
			carte[l].append("|_|")
	
	def print_carte(carte, alive):
		for h in range(len(carte)):
			ligne_de_carte = []
			la_ligne = ""
			for l in range(len(carte[0])):
				ligne_de_carte.append("|" + "_" + "|")
				for r in robots:
					if alive:#si le joueur est en vie, on va emprinter # ou S
						if r.nom != "Scout":
							if r.coordonnées[0] == len(ligne_de_carte) - 1 and r.coordonnées[1] == h:
								ligne_de_carte[-1] = "|" + r.signe + "|"
						else:
							if r.coordonnées[0] == len(ligne_de_carte) - 1 and r.coordonnées[1] == h:
								ligne_de_carte[-1] = "|" + r.signe + "|"
					else:#sinon on va emprinter o ou X
						if r.nom != "Scout":
							if r.vrai_coordonnées[0] == len(ligne_de_carte) - 1 and r.vrai_coordonnées[1] == h and r.vrai_coordonnées != Scout.coordonnées:
								ligne_de_carte[-1] = "|" + r.vrai_signe + "|"
							if r.vrai_coordonnées[0] == len(ligne_de_carte) - 1 and r.vrai_coordonnées[1] == h and r.vrai_coordonnées == Scout.coordonnées:
								del r
						else:
							if r.coordonnées[0] == len(ligne_de_carte) - 1 and r.coordonnées[1] == h:
								ligne_de_carte[-1] = "|" + "X" + "|"
			for i in range(len(ligne_de_carte)):
				la_ligne = la_ligne + ligne_de_carte[i]
			print(la_ligne) 
	
	
	alive = True
	gagné = False
	while alive and not gagné:
		print_carte(carte, alive)
		laphrase = str(Scout.nom) + " direction: " + str(Scout.direction) + ", " + str(Scout.nom) + " coordonnées: " + str(Scout.coordonnées) +  "\nAvancer vers la droite(6), la gauche(4), le haut(8) ou le bas(5)?: "
		choix1 = str(input(laphrase))
		if choix1 == "6" or choix1 == "4" or choix1 == "8" or choix1 == "5":
				Scout.direction = choix1
				if choix1 == "4" and Scout.coordonnées[0] > 0:
					Scout.avancer()
				elif choix1 == "8" and Scout.coordonnées[1] > 0:
					Scout.avancer()
				elif choix1 == "5" and Scout.coordonnées[1] < len(carte) - 1:
					Scout.avancer()
				elif choix1 == "6":
					Scout.avancer()
				for i in range(len(robots)):
					if not robots[i] == Scout:
						if robots[i].vrai_coordonnées == Scout.coordonnées:
							alive = False
							clear()
							print_carte(carte, alive)
							input("T'ES MORT!")
							continue
				if Scout.coordonnées[0] >= longueur - 1:
					gagné = True
					clear()
					print_carte(carte, alive)
					input("T'AS SURVECU!")
					continue

		if alive and not gagné:       
			clear()

while True:
	main()
