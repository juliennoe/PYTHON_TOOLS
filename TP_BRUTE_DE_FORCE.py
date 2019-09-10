import itertools
import os


password = 'juliennoe/23'
numbers = 'noejulien23/'
pin = ''
y = ''

for c in itertools.product(numbers, repeat=12):
    pin = y + ''.join(c)
    print (pin)
    os.system("./xyz "+pin)

    if pin == password:
        break


print('vous avez le password')  

