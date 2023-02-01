import random


def game(player, computer):
    if computer == player:
        return None

    elif computer == 's':
        if player == 'p':
            return False
        elif player == 'r':
            return True

    elif computer == 'r':
        if player == 's':
            return False
        elif player == 'p':
            return True

    elif computer == 'p':
        if player == 'r':
            return False
        elif player == 's':
            return True


computer_point = 0
player_point = 0

for i in range(0, 3):
    print("Comp Turn: rock(r) paper(p) or scissor(s)?\n")
    player = input("Your Turn: rock(r) paper(p) or scissor(s)?\n")
    player = player.lower()
    randNo = random.randint(0, 3)
    if randNo == 1:
        computer = 's'
    elif randNo == 2:
        computer = 'p'
    elif randNo == 3:
        computer = 'r'
    a = game(player, computer)

    print(f"Computer chose {computer}\n")
    print(f"You chose {player}\n")

    if randNo == 1:
        computer = 's'
    elif randNo == 2:
        computer = 'p'
    elif randNo == 3:
        computer = 'r'

    if a == None:
        print("This is a tie!\n")
    elif a == True:
        print("you got 1 point\n")
        player_point += 1
    elif a == False:
        print("computer got 1 point\n")
        computer_point += 1

print(computer_point)
print(player_point)
with open("winner.txt", "a") as f:
    if computer_point > player_point:
        print("computer won")
        f.write("computer won\n")
    elif player_point > computer_point:
        print("player won")
        f.write("player won\n")
    elif computer_point == player_point:
        print("it's a tie")
