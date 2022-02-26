import os


class User():
    def __init__(self, first_name, last_name, age=25, profession='Unemployed'):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def displayProfile(self, profession):

        print("The profile used is :" + self.first_name + ", " + self.last_name + ", and work as " + profession +
              " at " + str(self.age))

    def saveProfile(self, state):
        profile = open('ProfileUser' + self.first_name, state)
        profile.write("The profile used is :" + self.first_name + ", " + self.last_name + ", and work as " + self.profession +
                      " at " + str(self.age) + "years old")
        profile.close()
        print("Profile has been successfully saved ")

    def addMoreInfo(self):
        f = open('ProfileUser' + self.first_name, 'r')
        if f.mode == 'r':
            print('\n')
            print('______ The text written before modification _______')
            print(f.read())
            print('\n')
            f.close()

        # f = open('ProfileUser' + self.first_name, 'w')
        value = input('Enter more text if you want :')

        if value is not None:
            f = open('ProfileUser' + self.first_name, 'a+')
            f.write(value)
            f.close()
        elif value is None:
            print("Null value entered")


def main():
    # let's create a new user
    first_name = "John"
    last_name = "Pettersen"
    user = User(first_name, last_name)

    # Save the user info in a file
    user.saveProfile(state='w+')
    user.age = 28
    user.displayProfile("Lawyer")

    user.addMoreInfo()


if __name__ == "__main__":
    main()
