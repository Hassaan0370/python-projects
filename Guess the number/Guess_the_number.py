import random

computer = random.randint(1,100)
NoOFAttempts = 1
user = 0

while (user != computer):
    user = int(input("Guess a number from 1-100: "))
    if(user<0 or user>100):
        print ("Enter number from 0 to 100!")

    elif(user<computer):
        NoOFAttempts += 1
        print ("Higher number!")

    elif(user>computer):
        NoOFAttempts += 1
        print("Lower Number!")
else:
    print(f"You won in {NoOFAttempts} attempts")