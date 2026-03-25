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
r = input("Do you have a customer card?: ")

cur = "€"
norm = 10
adv = 14

# Pricing made by the answers the User gave

if q <= 14:
    norm = norm-3
    adv = adv-3
    print("!!! Price changed !!!") # I added a printout, so I could see, if the price has changed.
elif q >= 65:
    norm = norm-2
    adv = adv-2
    print("!!! Price changed !!!") # also just a printout

if e == "weekend":
    norm = norm+2
    adv = adv+2
    print("!!! Price changed !!!") # you know it.
else:
    norm = norm
    adv = adv

if r == "y":
    normcus = norm*0.9
    advcus = adv*0.9
    if w == "2D":
        str(print("Okay, your final price would be:",normcus))
        exit()
    elif w == "3D":
        str(print("Okay, your final price would be:",advcus))
        exit()
    else:
        print("Incorrect Answer.")
elif r == "n":
    if w == "2D":
        print("Okay, your final price would be :",norm)
    elif w == "3D":
        print("Okay, your final price would be",adv)
else:
    print("Incorrect Answer")

    
