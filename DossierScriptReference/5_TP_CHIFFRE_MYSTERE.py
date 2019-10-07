import random

chance = 5
nombre_mystere = random.randint(1,20)
print(nombre_mystere)

while chance != 0:

    nombre = input('entrer un nombre pour trouver le nombre mystere ')
    print(f'il ne vous reste plus que {chance} essai')
    chance -= 1

    if nombre.isdigit():

        nombre = int(nombre)

        if nombre > nombre_mystere:
            print(f'le nombre mystere est plus petit que {nombre}')

        elif nombre < nombre_mystere:
            print(f'le nombre mystere est plus grand que {nombre}')

        else:
         print('' )
         print('Bravo !' )
         break

    else :
        print('vous devez rentrer un nombre')
        exit()

