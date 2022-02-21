# Here we declare the static value name
value = 'Jordan'

# Then we declare the method that will take care opf that.


def displayName(name):
    if (name == value):
        print("Welcome back {}".format(name))
    else:
        print("You are not a certified user")


def main():

    print("++++++++++++++ Welcome to our new platform +++++++++++++++++++++++++++++++++++")
    name = input(" Please enter your name ")
    displayName(name)


if __name__ == "__main__":
    main()
