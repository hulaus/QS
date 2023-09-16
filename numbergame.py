#At the top of colde to generate random numbers
from random import seed  
from random import randint

number = randint(1, 10)

userguess = input("What number do you think it is?  ")
tryagain = input("I'll Give you another chance. What do you think the number is?  ")
toohigh = input("Try again ! *Hint: Try a little lower maybe?  ")
toolow = input("Try again ! *Hint: Try a little higher maybe?  ")

if userguess != number:
    print(tryagain)
    if str(tryagain) > str(number):
        print(toohigh)
    elif str(tryagain) < str(number):
        print(toolow)
    elif str(tryagain) == str(number):
         print("What?! Are you a mind reader? how did you get it right?")
         print(number)

#if userguess > str(number):
#    print("Doh ! That's Too High !")
#    input("Try Again! What is the number?  ")
#    while userguess > str(number):
#        print("Wah Wah... To High..Try again")
#        tryagain = input("Cmon.. You can do it ! What is your new guess?  ")
#        print(tryagain)
#        if str(number) > tryagain: break
#        print("Too low now ugh !")
#        if str(number) == tryagain:
#            print("You did it ! ")
#elif userguess < str(number):
#    print("Doooohhhh ! That number is too low !")
#    print(number)
#elif userguess == str(number):
#    print("Are you a mind reader?!")
#    print(number)



#Once running add more to the game !
#-- Display whether the guess is higher or lower than the number --
#-- Loop until they get the correct answer --
#-- Show how far away the number is from the guess