"""So, in PolyMorphism lecture we saw that : how to call a method from a subclass (Wizard) of the parent class (User)
and we did User.attack() in order to run the attack() method and use it. But, we have removed the attack() from User
class and now we want to create an init() function in User class and in this init() function we will take self and let's
say that user will receive let's say email because all the users of our game need to have emails.

we will try to access email with wizard1 object. But, we can't! But, what we have learned so far, as Wizard class is
using the User class. Right? So, we should have it's all attributes and methods accessible right? 

So, what's the best efficient way to make email attribute eligible to both subclasses of User class? 
Well, we wan't to call the inti() method of the User class from inside the init() method of Wizard or Archer class.
Right? Because, every time we instantiate a new "wizard" object, the init() function of "Wizard" class is going to be
called. So, the way to do is to say User.__init__(self,email)"""


class User():

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print("do nothing! ")


class Wizard(User):
    # we're calling the init() method of the User class inside of the wizard. So, when we instantiated a new wizard we
    # ran init() function of Wizard class and inside of this function we ran that User.init() and passed in the email
    # that we passed in as argument in wizard1 object. This is one of way of doing it is - User.__init__(self, email).
    def __init__(self, name, power, email):
        # User.__init__(self, email)

        # another way to do the same is below :
        # super() is a keyword in Python. All we do is run super() and super() is referring to super class that's User
        # class here or the class above Wizard which is User. With super() no longer need to use self in parameter.
        # So, our code looks more cleaner. super() allow us to refer to User class in this below way and not have to
        # worry about passing self.
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of : {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'{self.name} is now left with only : {self.num_of_arrows} arrows!')


wizard1 = Wizard('Robin', 60, 'robinhood@gmail.com')
archer1 = Archer('Merlin', 100)

# we will get this while try to run this : AttributeError: 'Wizard' object has no attribute 'email', when we just
# directly want to run the below line code, without using super() method in ChildClass.
print(wizard1.email)
