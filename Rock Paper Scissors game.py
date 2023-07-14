import random

def play():
    choice =int(input("Enter your choice: "))
    while choice < 1 or choice > 3:
        choice =int(input("Enter a valid choice: "))
    if choice == 1:
        user_choice = '✊'
    elif choice == 2:
        user_choice = '✋'  
    elif choice == 3:
        user_choice = '✌️'
    print("You played", user_choice)

    print("now its 🤖 turn ...")

    ai = random.randint(1, 3)
    if ai == 1:
        ai_choice = '✊'
    elif ai == 2:
        ai_choice = '✋'
    elif ai == 3:
        ai_choice = '✌️'
    print("Ai played:", ai_choice)

    print(user_choice, "VS", ai_choice)
    if ai == choice:
        print("DRAW 🙂")
    elif ai == 1 and choice == 3 or ai == 3 and choice == 2 or ai == 2 and choice == 1:
        print("You Lose 💀")
    else:
        print("You Win 🎉")


print("\n-- Winning rules are below: --\n|     ✊ VS ✋ => ✋ Win!     |\n|     ✌️  VS ✋ => ✌️  Win!     |\n|     ✊ VS ✌️  => ✊ Win!     |\n -----------------------------")
print("\t1- Rock ✊\n\t2- Paper ✋\n\t3- Scissors ✌️")

play()
x = input("You wanna play again?(y/n): ")
if x =='y':
    while x == 'y':
        play()
        x = input("You wanna play again?(y/n): ")
    else:
        print("Cya Soon...")
else:
    print("Cya Soon...")