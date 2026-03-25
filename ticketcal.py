
# made by 4zuj

print("Greetings, welcome to the website of the cinema XY!")

# First of All, we need variables so this system even works.

q = int(input("How old are you?: "))
if q < 12:
    print("Sorry, you are not allowed to see this movie.")
    exit()
w = input("Would you like to watch 2D or 3D?: ")
e = input("Would you like to watch the movie in the week or on the weekend?: ")
r = input("Do you have a customer card?: ")

cur = "€"
norm = 10
adv = 14

# Pricing made by the answers the User gave

if q == 13 or q == 14:
    norm = norm-3
    adv = adv-3
    print("Price changed")
elif q >= 65:
    norm = norm-2
    adv = adv-2
    print("Price changed")

if e == "weekend":
    norm = norm+2
    adv = adv+2
    print("Price changed")
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

    
