import random

L1 = ['apple', 'mango', 'banana', 'strawberry']
L2 = ['wolf', 'fox', 'deer', 'horse']
L3 = ['swedan', 'france', 'china', 'england']
L4 = ['alger', 'seoul', 'paris', 'moscow']
L5 = ['swain', 'ashe', 'fizz', 'zyra']

list_number = int(input(
    "Choose a list from below:\n\t1-Fruits\n\t2-Animals\n\t3-Countries\n\t4-Capitals\n\t5-LOL Champ\nList Number: "))
if list_number > 5:
    list_number = int(input("Out of range, Enter a right number: "))
if list_number == 1:
    words = L1
elif list_number == 2:
    words = L2
elif list_number == 3:
    words = L3
elif list_number == 4:
    words = L4
elif list_number == 5:
    words = L5

word = random.choice(words)
print("Guess the characters")
guesses = ''
attempts = 10
while attempts > 1:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, "\n", end="")
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win!\n")
        print("The word is:", word)
        break
    new_guess = input("Guess a character:")
    guesses += new_guess
    if new_guess not in word:
        attempts -= 1
        print("Wrong Char")
        print("You have", attempts, "more guesses")
        if attempts == 0:
            print("You Loose")
