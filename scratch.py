# Example 1 -- 
print("Hello, \nWorld")
print("Hello, World\n\nHello World!")

#Example 2 --
#Mistake Number 1, make sure to include quotation marks in your parenthesis ! 
name = input("What is your name? " )

greeting = print("Hello " + "" + name[:1])

grocery_list = ["eggs", "milk", "cheese", "pasta"]

#Mistake made... Make sure to put [] and not () for lists
print("The first item on the list is " + grocery_list[0])
print("The second item on the list is " + grocery_list[1])

#Example 3 --
#Tuples Example and calling the fourth item in the tuple
# planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
#print(planets[3])
#Adding a new example of for loop to the current/previous tuple example



#Example 4 -- 
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

#Example 5 --
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

#Example 6 -- 
#Multidimensional Lists
#Daily High & Low temperature (in Fahrenheit)
#09/07/2023 -- Added Two weeks of high and low data. 
#MISTAKE -- Forgot to add an extra bracket to enclose the new data set. Make Sure to pay attention to small details such as brackets. 
temps = [
    [
        [66, 34],
        [57, 25],
        [49, 45],
        [45, 19],
        [33, 7],
        [32, 14],
        [49, 37],
    ],
    [
        [52, 39],
        [61, 51],
        [64, 51],
        [67, 51], 
        [67, 57],
        [69, 42],
        [32, 14],
        [49, 37],
    ]
]
#Day 1 temps
#Mistake... Make Sure to put brackets not parenthesis !
#print(temps[0])

#Day 2 temps
print(temps[0][1])

#Day 3 temps
#print(temps[2])

#Day 1 High
#print(temps[0][0])

#Day 2 Low
#print(temps[0][1])

#Day 3 Low
#print(temps[2][1])

#Third Day in the second Week's Low
print(temps[1][2][1])

#After adding the second set of values the original day temps examples do not work. The original day temps now have to be formatted like Day 2 Temps

#Example 7 --
#Basic if statement example
a = "Yes"
b = "Yes"

if a == b:
    print("a is equal to b")
    print("Really, it is, I Promise !")
else:
    print("a is not equal to b")


#Example 8 -- 
#If statement example with variables that do not have the same variable
#if the if statement wasn't met and there is NO else condition the print function WILL NOT RUN
c = "Yes"
d = "No"

if c == d:
    print("c is equal to d")
else:
    print("dang dude... I guess it isn't")

#Example 9 -- 
#Example of Greater than comparison 
e = 1
f = 2

if a < b:
    print("a is less than b")

#Example 10 -- 
#else Example
g = 1
h = 2

if g == h:
    print("g is equal to h")
else:
    print("g is not equal to h")

#Example 11 -- 
#Elif(else if) Example
#A way to compare conditions in a chain, starting with a base assumption
i = 1
j = 2
k = 3

if i > j:
    print("i is greater than j")
#The first comparision was not successful so it will check the elif to see if that statement is true.
elif j < k:
    print("j is less than k")
#Always put the Else after you're done putting all the elifs
else: 
    print("I don't know then")

#Example 12 -- 
#Nested Comparisions Example
l = 2
m = 2
n = 2

if l > m:
    print("l is greater than m")
    if m != n:
        print("but m is not equal to n")
    else:
        print("m is equal to n")
else:
    print("l is less than m")


#Example 13 -- For Loops
#Display the planets

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for planet in planets:
    print(planet)
