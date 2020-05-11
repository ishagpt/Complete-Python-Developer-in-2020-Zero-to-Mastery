"""
let's say that we're working for a gaming company and this gaming company has well this Wizard game, that they
want to create almost like Harry Potter. Now how we can think about it in object oriented programming.
Well, the first thing that we're gonna be need is we're going to be have to have players right? Each player has a
character that they need to play. So, let's create a class here and call it "PlayerCharacter"
"""


class PlayerCharacter:
    # Class Object Attribute
    membership = True

    """__init__() method is a special method. This is also called a dunder method or magic method. This is called as a
    constructor method or init() method and this is automatically called anytime when we instantiate an object! Remember
    Instantiating means is we're calling the class to create an object. So, when we're going to use "player1" or
    another object like this it's going to automatically run whatever is in this code block.

    What is self keyword here? Self is a default parameter. Self refers to whatever's the left side of dot. So, this
    way it allow us to have a reference to something that hasn't been created yet. In this case, "Player1"
    and let them know that, hey when it's created when we instantiate then I want you to make sure that "Player1"
    has this name attribute. Well, this is a way for us to define self, self refers to the player character. It's
    ("self") saying hey, this is going to refer to this "PlayerCharacter" that we're going to create "Player1" object
    and I wan't "self.name" equal to whatever the parameter is. So, if I do "player1.name" below and I click to run I
    get "Manthan" in output.
    """

    def __init__(self, name, age):
        # these below are attributes or properties (name,age), that these objects have and you can access them by doing
        # the dot(.) notation then accessing the property itself.
        self.name = name
        self.age = age

    def run(self):
        print(self.name + " " + 'run fast!')


"""
here we instantiated the "player1" below and passed the parameter for "name" as "Manthan" and "Mayank" these two objects
are different fom each other and take a different - 2 place in memory to be stored.
print(player1) --> output --> some random memory location 
So, when we add a separate property with an specific object it won't be available or impact second object! 
Below we have added an "attack" property in "player2" object only and it won't be available to player1 object.
"""
player1 = PlayerCharacter('Manthan', 24)
player2 = PlayerCharacter('Mayank', 25)
player2.attack = 50

print(player1)
print(player1.name)
print(player1.age)
print(player1.run())
# we're getting "None" in output too, bcoz we're not returning anything from run() method!
print(player2)
print(player2.name)
print(player2.age)
print(player2.run())
# we're getting "None" in output too, bcoz we're not returning anything from run() method!
print(player2.attack)

