import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #puede ser high tmb porque high = low
        
        feedback = input(f'es {guess} muy alto (H), muy bajo(L) o correcto(C)??').lower()
        if feedback =='h':
            high = guess - 1
        elif feedback =='l':
            low = guess + 1
            
    print(f'La computadora adivino el numero {guess}')

computer_guess(10)