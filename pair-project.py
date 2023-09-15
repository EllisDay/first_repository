Role = ""
a = "t"


def Class(role):
    global Role
    Role = role
    print("Noted Spacetraveller, you are a(n)")
    return Role


def death():
    global a
    if len(role) > 7:
        print("The black hole got tired of you being near its gravitational pull *and maybe it didn't like your long name* so you got pulled in.")
        a = "f"
        return a

Class(input("What is your purpose in space? "))

print("You were ejected from your spacepod and left to gaze at the supermassive black hole!")

print("What is your name? -Black hole")

name = input("Name:  ")
choices = []
choices2 = []

print("hello "+name)

print("You are facing a supermassive black hole, but you also have an antigravity pistol you can use to try and counteract the gravity; do you let the black hole consume you and be the few to expirience the black holes emptiness? or do you try and escpape with the antigravity pistol?")

print("[1] Go in the black hole         [2] Use the pistol to try and escape")

while a =="t":
    choice1 = input()
    if choice1 == '2':
        choices.append("2")
        print("You pistol shot you across lightyears of space in a matter of miliseconds, but like space, its mostly empty; you have no idea where you are now.")
        print(choices)
    if choice1 == '1':
        choices.append("1")
        print("You let yourself be consummed by the void, you have another option though: do you use your anti-gravity gun on the event horizon, or do you fully let yourself be consumed?")
        print("[1] Accept the black hole as your final stand     [2] Use the anti-gravity gun")
        print(choices)

    if len(Role) > 7:
        death()
        break

    choice2 = input()
    if choice2 == '1':
        print("You used the antigravity gun and came out of a alternative black hole, you begin going away from the black hole and find yourself going closer and closer the the capsule, the capsule reforms as you go inside of it, you're reliving everything in reverse.")
        choices.append("1")
        print(choices)

    elif choice2 == '2':
        print("You enter the black hole, there is no light, no noise, all what you have left is yourself and 5 minutes of oxygen.")
        choices.append("2")
        print(choices)