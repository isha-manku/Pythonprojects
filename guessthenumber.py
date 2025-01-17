import random
target = random.randint(1,100)
while True:
    userchoice = input("Guess the number or press Q to quit ")
    if(userchoice=="Q"):
        break
    userchoice = int(userchoice)
    if(userchoice == target):
        print("success : correct guess!")
        break
    elif(userchoice<target):
        print("your number is too small.Take a bigger guess")
    else:
        print("your number is too big.Take a smaller guess")
print("_______________GAME OVER______________")
