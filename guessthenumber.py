#importo random
import random


#defino una funcion guess y pongo x como parametro para que, luego de definirlo, pueda pasar esta funcion
def guess(x): 
    random_number = random.randint(1, x)#hago que el numero random sea entre 1 y x
    guess = 0
    while guess != random_number:
        guess = int(input(f'ingresa un numero del 1 al  {x}: '))
        if guess < random_number:
            print('Muy alto')
        elif guess > random_number:
            print('Muy bajo')
            
    print(F'Felicidades adivinaste! el numero es: {random_number}')
    
    
guess(10)
    