from random import randrange

n = randrange(1000)

while True:
    v = int(input("Guess the number: "))
    if n == v:
        print("You win!")
        break
    else:
        print('Smaller' if n < v else 'Bigger')