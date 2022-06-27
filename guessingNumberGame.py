import random

number = random.randint(1,10)
print("Welcome to the guessing games")
guessed_num,count = 0,0
while guessed_num != number :
    guessed_num = int(input("Please enter the number which you guessed: "))
    count += 1
    if number == guessed_num:
        print("The number you guessed is right")
    elif count !=3:
        print("The number you have guessed is wrong , please try again")
    if count < 3 or number == guessed_num:
        pass
    else:
        print("You have guessed three times. Chances are over. exiting the game")
        break
