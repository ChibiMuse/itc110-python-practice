#old mcdonald

def singsong(x):
    if x == 1:
        print("Ee-igh, Ee-igh, Oh!")
    else:
        print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def chorus(animal, sound):
    singsong(0)
    print("And on that farm he had a {0}, ".format(animal), end = " ")
    singsong(1)
    print("With a {0} {0} here and a {0} {0} there.".format(sound))
    print("Here a {0},there a {0}, everywhere a {0}, {0}".format(sound))
    singsong(0)

def main():
    animal = ["cow", "duck", "cat", "dog", "horse"]
    sound = ["moo", "quack", "meow", "bark", "neigh"]
    for i in range (5):
        chorus(animal[i], sound[i])
        print()

main()
