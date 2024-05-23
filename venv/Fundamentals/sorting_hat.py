names = input()
while True:
    if names == "Welcome!":
        print(f"Welcome to Hogwarts.")
        break
    elif names == "Voldemort":
        print(f"You must not speak of that name!")
        break
    char = int(len(names))
    if char < 5:
        print(f"{names} goes to Gryffindor.")
    if char == 5:
        print(f"{names} goes to Slytherin.")
    if char == 6:
        print(f"{names} goes to Ravenclaw.")
    if char > 6:
        print(f"{names} goes to Hufflepuff.")
    names = input()

# how to commit in pyCharm
prit("how to do that?!?!")