import random as rd

while True:
    print('Player Please enter Y to roll the dice and N to Not')
    a = input("Y/N    ")
    if a == 'y' or a == 'Y':
        die1 = rd.randint(1, 6)
        die2 = rd.randint(1, 6)
        print(f'({die1},{die2})')
    elif a == 'n' or a == 'N':
        print('Thank you for playing')
        break
    else:
        print("Incorrect input given")
        break
