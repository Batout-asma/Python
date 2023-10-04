import random
user_cpt = 0
ai_cpt = 0
def play(user_cpt, ai_cpt):
    print("\t1- Rock ✊\n\t2- Paper ✋\n\t3- Scissors ✌️")
    choice =int(input("Enter your choice: "))
    while choice < 1 or choice > 3:
        choice =int(input("Enter a valid choice: "))
    if choice == 1:
        user_choice = '✊'
    elif choice == 2:
        user_choice = '✋'  
    elif choice == 3:
        user_choice = '✌️'
    print("You played:", user_choice)

    print("\nnow its 🤖 turn ...")

    ai = random.randint(1, 3)
    if ai == 1:
        ai_choice = '✊'
    elif ai == 2:
        ai_choice = '✋'
    elif ai == 3:
        ai_choice = '✌️'
    print("Ai played:", ai_choice,"\n")

    print(user_choice, "VS", ai_choice)
    if ai == choice:
        print("DRAW 🙂\n")
    elif ai == 1 and choice == 3 or ai == 3 and choice == 2 or ai == 2 and choice == 1:
        print("You Lose 💀\n")
        ai_cpt += 1
    else:
        print("You Win 🎉\n")
        user_cpt += 1
    return user_cpt, ai_cpt

print("\n - Winning rules are below: --\n|     ✊ VS ✋ => ✋ Win!     |\n|     ✌️  VS ✋ => ✌️  Win!     |\n|     ✊ VS ✌️  => ✊ Win!     |\n -----------------------------")
while True:
    user_cpt, ai_cpt= play(user_cpt,ai_cpt)
    x = input("Do you want to play again? (y/n): ")
    if x != 'y':
        print("\nThe Final Score is:\n","🤖 ",ai_cpt,"  ",user_cpt," 🧑","\nCya Soon...\n")
        break