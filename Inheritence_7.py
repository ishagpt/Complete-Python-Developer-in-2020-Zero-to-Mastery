"""
Third Pillar of OOP's is : Inheritance

Inheritance allows new objects to take on the properties of existing objects. So, you can inherit classes.

Let's say we want to create a new game and we have different types of users. So, we have users that can be wizards that
can be else, that can be Archers but all these users have some common functionality and each one of the sub users like
wizards, elves, archers have some common shared functionality. But, then again may be different attacks. So, using OOP
we can actually do inheritance.

Now, you might be wondering, where is the __init__() method in below class. Shouldn't we have that init() method that
gets run first. Well, we could but if we don;t have any variables or attributes that we want to assign the user. Well,
in that case we wouldn't need an init() method.

Users can have different forms. They can be :
Wizards, Archers, Ogers etc. all the characters in our game. But all of them first have to sign in. How we can make sure
that all of these Wizards or Archer classes also have access to sign in. Well, we can use inheritance.

How do we do inheritance? It's quit easy actually. All we have to do is pass the Parent class "User" that we want to
inherit from.

"""


class User():
    def sign_in(self):
        print('logged in')


# creating sub classes below :
class Wizard(User):
    # let's say this wizard has an init() method which will run when the wizard is created and will have a name, power.
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of : {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def attack(self):
        print(f'{self.name} is now left with only : {self.num_of_arrows}')


""" So, let's instantiate a class below and create a wizard1 and then say wizard and run that wizard class and archer1 
for Archer class to instantiate. 
The main important feature of inheritance is :  both two classes Wizard and Archer now have sign_in method available 
from their "User" Parent class and they also have their own unique set of attributes and methods! 
This is the power of inheritance we're keeping our Parent class code dry right? We're abstracting away the part of the
code that these both classes : Wizard and Archer share. But, changin things what according to what each one needs 
(having different - 2 attributes and methods. So, for example we could have different methods and properties than the 
archer but also have shared User's functionality that they have. In this way keep our code organized and clean. 

Now this idea of inheritance is really - 2 powerful and the key is here is that we have a parent class and children 
classes. Now, sometimes these children classes are called subclasses or derived classes because they're subclasses of 
"User" or derived from the "User" class.  
 """

wizard1 = Wizard('Robin',60)  # object creation
archer1 = Archer('Merlin', 100)
print(wizard1.attack())
print(archer1.attack())
print(archer1.sign_in())


"""Python gives us a useful tool to check if something is an instance of a class and easily enough for us. 
"isinstance" and it's a built function in Python, we give it the instance and then the class that we want to check. 
isinstance(instance, class) is the format. 
"""
print(isinstance(wizard1,Wizard))
print(isinstance(archer1,Archer))
# It's True : bcoz wizard class is a sub class of user. Coz, we to run the User class to create wizard1.
print(isinstance(wizard1,User))

""" How we get lots of dunder methods suggestions for an Object apart from the methods and attributes of class.? 
from where do these lot of dunder methods suggestions come from? 
Well, in python remember how I said, everything is an object. Well, everything in Python inherits from the base object 
class that Python comes with and it's called "object". So, we do isinstance(wizard1,object) it gives "true" bcz wizard1 
 inherits or gets methods from the "Wizard" class from the "User" class and even higher up from the "object" base class 
that Python comes with and that's why we have these automatic methods attached for us. So, that using "object" every 
single method that's useful. For example, if I open up a list below and let' say we pick EPR method which we don;t know 
what it really does yet. But, if I go to wizard1 and when we do dot(.) we see that we have it as well becuase
 
 So, when we do something like "User" class it's actually accepting "object" as the parent class in order to accept 
 these properties that are built in and that we might need in the future!"""

print(isinstance(wizard1,object))
