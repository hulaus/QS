print("Hello, \nWorld")
print("Hello, World\n\nHello World!")

#Mistake Number 1, make sure to include quotation marks in your parenthesis ! 
name = input("What is your name? " )

greeting = print("Hello " + "" + name[:1])

grocery_list = ["eggs", "milk", "cheese", "pasta"]

#Mistake made... Make sure to put [] and not () for lists
print("The first item on the list is " + grocery_list[0])
print("The second item on the list is " + grocery_list[1])

#Tuples Example and calling the fourth item in the tuple
planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

print(planets[3])

#Example of Set... Will Return deduplicated and formatted it to read better
customers = {"James Smith",
            "Andrea Richards",
            "Sam Sharp",
            "Brenda Longmire",
            "Veronica March",
            "Sylvia Smith",
            "James Smith",
            "Vanessa Bush",
            "Steve Hammersmith",
            "Brenda Longmire",
            "Sylvia Smith",
            "Steve Hammersmith",
            "Walt Hawkins"}

print(customers)

#Example of a Dictionary
#There are 2 Seprate dictionary variables: Four Values, each referenced by a key
#The Keys in this example are name, age, phone, email
#To acces one of these values by its key, we would use the name of the dictionary followed by the key name in brackets
#KEYS ARE UNIQUE -- you cannot have more than one name, age, phone or email key in dictionary
customer1 = {
    "name": "James Smith",
    "age": 24,
    "phone": "555-555-1941",
    "email": "james@xyzinternet.net"
}

customer2 = {
    "name": "Andrea Richards",
    "age": 33,
    "phone": "555-555-4928",
    "email": "andrea@coffeeloversunite.us"
}

print(customer1["name"])

#Multidimensional Lists
#Daily High & Low temperature (in Fahrenheit)
temps = [
    [66, 34],
    [57, 25],
    [49, 45]
]

#Day 1 temps
#Mistake... Make Sure to put brackets not parenthesis !
print(temps[0])

#Day 2 temps
print(temps[1])

#Day 3 temps
print(temps[2])

#Day 1 High
print(temps[0][0])

#Day 2 Low
print(temps[0][1])