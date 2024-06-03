import random
print("Choose a number between 0 to 50. You have 6 attempts to guess.")
a=random.randint(0,50) 
for i in range(0,6):
    b=int(input("\nEnter your guess: "))
    if (a<b):
        print("Try entering a smaller number")
    elif (a>b):
        print("Try entering a larger number")
    else:
        print("You guessed the correct number!")
        break
        
print("The game is over!")

