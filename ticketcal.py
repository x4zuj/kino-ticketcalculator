# made by 4zuj
# I made a ticket calculator!
# If you look in my other projects, you can see that I always start with a greeting :D

print("Greetings, welcome to the website of the cinema XY!")

# First of All, we need variables so this system even works.

q = int(input("How old are you?: "))
if q < 12:
    print("Sorry, you are not allowed to see this movie.")
    exit()
    # I made exit(), since if the User is below of the age of 12, he isn't allowed to go to the cinema.
w = input("Would you like to watch 2D or 3D?: ")
e = input("Would you like to watch the movie in the week or on the weekend?: ")
r = input("Do you have a customer card? (y/n): ")

cur = "€"
price = 10

# Pricing made by the answers the User gave

if q <= 14:
    price = price-3
    
elif q >= 65:
    price = price-2

if e.lower() == "weekend":
    price = price+2

if r == "y":
    if w.lower() == "2d":
        print("Okay, your final price for the 2D film would be:",price*0.9)
    elif w.lower() == "3d":
        print("Okay, your final price for the 3D film would be:",(price+4)*0.9)
    else:
        print("Incorrect Answer.")
elif r == "n":
    if w.lower() == "2d":
        print("Okay, your final for price the 2D film would be :",price)
    elif w.lower() == "3d":
        print("Okay, your final for price the 3D film would be",price+4)
else:
    print("Incorrect Answer")
    
