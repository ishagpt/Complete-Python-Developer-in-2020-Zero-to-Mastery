"""
Instrospection : in the computer programming means the ability to determine the type of Object at runtime,
What is runtime? That's when the code is running you can determine the type of an object and it's actually one of
Python's strength because everything in Python is an object. We can examine, we can introspect and actually figure out
what our code does as we're coding and then running and Python allow us to do some introspection and inspect these
objects with some nicer helper functions. This one function called as dir(). When we will run the dir() on an object
well, it will give us all of the methods and attributes that the wizard instance has. So, with dir() function we give it
an instance and right away we get access to wht it has access to.  """

class User():
    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing! ")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        """ But, let's say we wanted to have both User and Wizard run the attack() method. How can we do this? """
        User.attack(self)
        print(f'attacking with power of : {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'{self.name} is now left with only : {self.num_of_arrows}')


wizard1 = Wizard('Robin', 60)
archer1 = Archer('Merlin', 100)

print(dir(wizard1))