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
#^^ Different than just using print(planets). Using for statement, we are iterating over the planet and running the print statement on each entry.
# WHEN NOT USING A FOR LOOP THE RESULT WILL LOOK LIKE THIS --> ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# WHEN USING FOR LOOP THE RESULT WILL LOOK LIKE THIS --> 
        #Mercury
        #Venus
        #Earth
        #Mars
        #Jupiter
        #Saturn
        #Uranus
        #Neptune

#Explaination -- The planet list is defined with the list of currently named planets in our solar system. 
#Then we use a for statement to say "For each planet in planets, run the following code." For each planet in the list Planets Run Print(Planets)

#For Loop Example 2
#Iterate Through a string
a = "Hello, World!"
for c in a: 
    print(c) #c stands for characacter

#For loop Example 3
#Created a list with three singular nouns, iterated over it with for statement
singular_words = ["student", "teacher", "room"]
for word in singular_words:
    #Modified temporary variable by setting it equal to itself plus the letter "s" at the end
    #word = word + "s"
    #print(word)
#SIMPLER WAY TO GET THE SAME RESULT AS THE CODE ABOVE
    print(word + "s")
#If we want to run code after for loop the else statement can be used
else:
    print("Done!")

#Range Example -- Display the first ten numbers
for i in range(10):
    print(i)

#For loop iterates over the result from the range function supplied with the argument 10

#Enumerate Example -- Display the planets and its number
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

for index, value in enumerate(planets):
    # Almost right but this starts at 0, Need to start at 1 --> print("Planet " + str(index) + ": " + value)
    print("Planet " + str(index + 1) + ": " + value)
    #The + 1 with the index adds 1 to the index so the index now starts at 1 and not 0

#While loop Example -- While i is less than 10, display i

i = 1 #First set variable i to 0 // Changed to one for new example.
#Use while to execute TWO Commands as long as the comparison i <= 10 is true.
while i <= 10: 
    print(i)
    i += 1

#While loop example -- 99 Bottles of beer example
bottles = 99 #First we set the bottles variable to 99
while bottles > 0: #Start a while loop and say "run the following code while bottles is greather than zero".
#Print First and second lines inserting bottles variable(integer) converting inline to string
    print(str(bottles) + " Bottles of beer on the wall.") 
    print(str(bottles) + " Bottles of beer.")
    bottles -= 1 #Subtract by one from the bottles variable then run print again Twice using same variable to string conversion str()
    #^^ This should subtract 1 from bottles variable. 
    print("Take one down, pass it around,")
    print(str(bottles) + " Bottles of beer on the wall")
    
#The Code will loop until the expresion bottles > 0 is no longer true (When bottles variable becomes 0)
#Code Break Down ------------------------- ^^ 

for i in range(99)[::-1]:
    print(str(i + 1) + " Bottles of beer on the wall")
    print(str(i + 1) + " Bottles of beer.")
    i -= 1
    print("Take one down, pass it around,")
    print(str(i + 1) + " Bottles of beer on the wall")

