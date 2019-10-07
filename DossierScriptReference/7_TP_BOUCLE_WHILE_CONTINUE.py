"""
Récuperer ce que donne l'utilisateur
Tester si la donnée est un nombre

si oui affichr la table de multiplication
si non lui demander a nouveau de rentrer une valeur


"""

oQuitter = ""

while oQuitter != "o":


	oNombre = input("Entrez un nombre ici")

	oBool = oNombre.isdigit()

	if oBool == True:

		oNombre = int(oNombre)

		for i in range(11):
			print(str(i) + "*" + str(oNombre) + "=" + str(i*oNombre))

		oQuitter = input("voulez vous quitter ? o/n ")	

	elif oBool == False:
		print("je n'ai pas rentre le bon caractere")
