#At the top of colde to generate random numbers
from random import seed  
from random import randint

number = randint(10, 100)

input("What number do you think it is?  ")

if str(input) > str(number):
    print("Doh ! That's Too High !")
else:
    str(input) < str(number)
    print("Doooohhhh ! That number is too low !")
print(number)


#Once running add more to the game !
#-- Display whether the guess is higher or lower than the number --
#-- Loop until they get the correct answer --
#-- Show how far away the number is from the guess