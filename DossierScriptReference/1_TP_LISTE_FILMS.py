"""
Demander de rentrer des titres
ajouter ces titres a une liste
Gerer les doublons
Classer les films par ordre alphabetique
Afficher la liste

"""
continuer = 'o' # DEFINIR UNE VARIABLE POUR QUITTER LA BOUCLE WHILE

liste_films = [] # LISTE DE FILM A REMPLIR

while continuer == 'o': # BOUCLE WHILE / TANT QUE

	add_film = raw_input('ajouter votre film : ') # AJOUT DE FILM VIA LA FONCTION INPUT

	liste_films_en_minuscule = [film.lower() for film in liste_films] # TRANSFORMATION DES INPUT EN STRING ET MINUSCULE

	if add_film.lower() in liste_films_en_minuscule : # SI LES INPUT DANS LA LISTE SONT :

		print('{0}' 'le film est deja present dans la liste'.format(add_film)) # DEJA PRESENT
	
	else: # SINON

		liste_films.append(add_film) # AJOUT A LA LISTE
	
		continuer = raw_input('voulez vous continuer o/n : ') # CONTINUER A RENTRER DES FILMS

		print('')
	
		liste_films.sort() # METTRE LA LISTE DANS L'ORDRE ALPHABETIQUE
	
		print(liste_films) # PRINT LA LISTE

