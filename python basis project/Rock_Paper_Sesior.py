# write a program to built a game sesior paper rock.
import random


def game(com,player):
    if com == player:
        return None
    elif com == 's':
        if player == 'p':
             return  False
        elif player == 'r':
            return True
    elif com == 'p':
        if player == 'r':
             return  False
        elif player == 's':
            return True
    elif com == 'r':
        if player == 's':
             return  False
        elif player == 'p':
            return True
    elif player !='s' or 'r' or 'p' :
        print("please select the given option only")

com = random.randint(1,3)
computer = "computer TURN: sesior(s) paper(p) Rock(r) "
if com == 1:
    com = 's'
elif com == 2:
    com = "p"
else:
    com = 'r'

print(computer)
player = input("YOUR TURN: sesior(s) paper(p) Rock(r)  ")


new = game(com,player)

ply = f'you select : {player}'
cm = f"com select : {com}"

print(ply)
print(cm)


if new == None:
    print("the game is tie!")
elif new:
    print("you won the game!")
else:
    print("you lose ")

