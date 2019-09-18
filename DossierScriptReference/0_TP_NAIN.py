

import random
import time

liste_nain = ["grincheux","joyeux","simplet","prof","timide","dormeur","atchoum"]

seconds = 5


rand_nain = random.choice(liste_nain)

index_nain = liste_nain.index(rand_nain)

hide_nain = liste_nain.pop(index_nain)

random.shuffle(liste_nain)


active_question = raw_input('etes vous pret ? o/n ')

for i in range(seconds):
		
	print("l'enigme va commencer dans " + str(seconds - i))
		
	time.sleep(1)

print('')
print(liste_nain)

print('')
answer_nain = raw_input('qui est le nain manquant ? ')

while answer_nain != rand_nain:

	answer_nain = raw_input('qui est le nain manquant ? ')

	
print('')
print('Well Done')


