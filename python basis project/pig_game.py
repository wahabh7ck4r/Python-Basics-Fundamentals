import random

def roll():
    min_value = 1
    max_value = 6
    value = random.randint(min_value, max_value)
    return value


while True:
    player = input("Enter the number of player (2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <=4:
            break
        else:
            print("player must be between 2 to 4")
    else:
        print("Invalid, please try again..")

max_score = 50 
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:

    for player_idx in range(player):
        print(f"\nplayer {player_idx + 1} turn has just started! ")
        print(f"Your total socre is {player_score[player_idx]}")

        current_score = 0
        
        while True:
            should_roll = input("would you like to roll (y)?: ")

            if should_roll.lower() != "y":
                break

            value = roll()

            if value == 1:
                print("you roll a 1! turn done!")
                current_score = 0
                break
            else:
                current_score +=value 
                print("you rolled a ",value)

            print("your score is ",current_score)

        player_score[player_idx] += current_score
        print("your Total socre is : ", player_score[player_idx])
                

max_score = max(player_score)
wining_idx = player_score.index(max_score)
print(f"player number {wining_idx + 1} is winner with socre: {max(player_score)}")