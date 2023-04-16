import random

answer = random.randint(1,30)
name = input('Enter your name: ')
guess = input('What is your guess?')
guess = int(guess)

while guess != answer:
    if guess > answer:
        print('mine is smaller')
    else:
        print('mine is larger')
    guess = input('oops, guess again ;)')
    guess = int(guess)

print('Excellent!', name, ',you win')
