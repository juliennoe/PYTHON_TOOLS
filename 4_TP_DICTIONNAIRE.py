

dictionnaire = {'clef': 'valeur' , 'clef1': 'valeur1', 'clef2': 'valeur2'} # DICTIONNAIRE SIMPLE AVEC CLES ET VALEURS

dictionnaire2 = { # DICTIONNAIRE AVEC SOUS PARTIE / CLES / VALEURS / ITEMS

'Pierre':{'age':40,'profession':'banquier'}, 

'Paul':{'age':25, 'profession': 'ingenieur'}

}

print(dictionnaire['clef']) # PRINT CLES DU DICTIONNAIRE

print(dictionnaire2['Pierre']['profession']) # PRINT LA VALEUR DE > PIERRE > PROFESSION

print(dictionnaire2.keys()) # PRINT LES CLES

print(dictionnaire2.values()) # PRINT LES VALEURS DANS LES CLES

print(dictionnaire2.items()) # PRINT LES ITEMS SOIT TOUTES LES DONNEES DU DICTIONNAIRE

dictionnaire['clef1'] = 'valeur127' # PERMET D'UPDATE LA VALEUR DU DICTIONNAIRE
#dictionnaire.update({'clef1:valeur127'}) # PERMET D'UPDATE LA VALEUR DU DICTIONNAIRE synthaxe differente

print(dictionnaire)

del dictionnaire['clef2']
#dictionnaire.pop('clef2')

print(dictionnaire)

if 'Pierre' in dictionnaire: # CHECKER SI UNE CLE EST DANS LE DICTIONNAIRE
	print('Pierre est dans le dictionnaire')

#if 40 in dictionnaire.keys(): # CHECKER SI UNE VALEUR EST DANS LES CLES