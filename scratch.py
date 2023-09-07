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