# ClydeBank Coffee Shop Simulator 4000
# Copyright (C) 2023 Clydebank Media, All Rights Reserved.

#Import items from the random module to generate weather
from random import seed
from random import randint

#Current day number
day = 1 

#Starting cash on hand
cash = 100.00

#Coffee on hand (cups)
coffee = 100


#Sales list of dictionaries
#sales = [
#   {
        #"day": 1,
        #"coffee_inv": 100,
        #"advertising": "10",
        #"temp": 68,
        #"cups_sold": 16
#   },
#   {
        #"day": 2,
        #"coffee_inv": 84,
        #"advertising": "15",
        #"temp": 72,
        #"cups_sold": 20        
#   },
#   {
        #"day": 3,
        #"coffee_inv": 64,
        #"advertising": "5",
        #"temp": 78,
        #"cups_sold": 10        
#   },
# ]
#Create an Empty sales list
sales = []

#Welcome Message
print("Clydebank Coffee Shop Simulator 4000, Version 1.00")
print("Copyright (C) 2023 ClydeBank Media, All Rights Reserved.\n")
print("Let's collect some information before we start the game.\n")

#Get name and Shop Name
name = input("What is your name? ")
shop_name = input("What do you want to name your coffee shop? ")

print("\nOk, let's get  started. Have Fun !")

# print("\nThanks, " + name + ". Let's set some initial pricing.\n")

#The Main Game Loop
running = True
while running:
    #Display the day and add a "fancy" text effect
    print("\n-----| Day" + str(day) + " @ " + shop_name + "|-----")

    #Generate a random temperature between 20 and 90
    #We'll consider seasons later on, but this is good enough for now
    temperature = randint(20, 90)

    #Display the cash and weather
    print("You have $" + str(cash) + " cash and it's " + str(temperature) + " degrees.")
    print("You have coffee on hand to make " + str(coffee) + " cups.\n")

#Get initial price of a cup of coffee
cup_price = input("What do you want to charge per cup of coffee? ")

#Get price of a cup of coffee
print("\nYou can buy advertising to help promote sales.")
advertising = input("How much advertising do you want to buy? (0 for none)")

#Convert advertising into a float
advertising = float(advertising)

#deduct advertising from cash on hand
cash -= advertising

#TODO : CALCULATE TODAY'S PERFORMANCE
#TODO: DISPLAY TODAY'S PERFORMANCE

#Before we loop around add a day 

day += 1
#Display what we have
print("\nGreat. Here's what we've collected so far.\n")
print("Your name is" + name + "and you're opening" + shop_name + "!")
print("Your first cup of coffee will sell for $" + cup_price + ".\n")
