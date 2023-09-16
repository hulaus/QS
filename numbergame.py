#At the top of colde to generate random numbers
from random import seed  
from random import randint

number = randint(1, 10)

userguess = input("What number do you think it is?  ")


if userguess > str(number):
    print("Doh ! That's Too High !")
    input("Try Again! What is the number?  ")
    while userguess > str(number):
        print("Try again")
        tryagain = input("Cmon.. You can do it ! What is your new guess?  ")
        print(tryagain)
elif userguess < str(number):
    print("Doooohhhh ! That number is too low !")
    print(number)
elif userguess == str(number):
    print("Are you a mind reader?!")
    print(number)



#Once running add more to the game !
#-- Display whether the guess is higher or lower than the number --
#-- Loop until they get the correct answer --
#-- Show how far away the number is from the guess