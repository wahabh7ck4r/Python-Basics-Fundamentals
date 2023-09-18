import random

rand = random.randint(1,100)

gusse = 0
user = None

while(user != rand):
    user = int(input("enter your gusse: "))
    gusse = gusse +1
    if user == rand:
        print("your gusses is right!")
    else:
        if(user>rand):
            print("your gusses is wrong! plese selcet the smaller number")
        else:
            print("your gusses is wrong! please select the larger number")

print(f"you gussed the number in {gusse} chance")

with open("hiscore.txt", 'r')as f:
    hiscore = f.read()

if(gusse<int(hiscore)):
    h = open("hiscore.txt", 'w')
    h.write(str(gusse))
