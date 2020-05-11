"""
OOP allow us to create objects that have their own methods like run() and attributes, properties. It's a great way to
add more functionality to a language and mimic the real world.
OOP allow us to write code that is repeatable, well organized and also memory efficient right bcoz we only write our
class once, which Objects can use by passing their customized parameters.
Thinking less procedural and thinking more in terms of functionality grouping data like attributes (name, age) together
with methods (run()) to create this class "PlayerCharacter" that is able to mimic something from the real world.

We can check the class Blueprint from Objects using "help" keyword. Like, help(Player1) or help(list) etc. and this is
the great way to see what class blueprint some of the python data types have.

In the PlayerCharacter, we saw that we're able to create attributes (name,age), and attributes are pieces of data that
are dynamic. That's when we instantiate an object they're going to be unique to that specific object (Player1) like
name and age, and we have to use the "self" keyword to make it's dynamic.

However, there is another thing called - Class Object Attribute (COA), and in COA unlike class these (name,age) regular
class attributes is different because while it's not DYNAMIC it's STATIC. This is something we will use in our code
when there will be no change and this COA is going to be exist for all objects. So, you can't really modify it's just
all the objects that we instantiate will have access to it. So, this doesn't change across instances and we can use this
COA anywhere in class blueprint.

A COA is something that doesn't change across different instances (player1 or player2) v/s in attribute or a class
attribute is something that is dynamic and specific to each each class object. The way we access them is different where
we can actually access membership like this (with PlayerCharacter.membership). But, in order to access a name or a age
anywhere inside of our class we have to use self.age or self.name, which is why anytime we create a method in a class
even if I create a new one over here (below shout () method) and let's say this new one going to be run(). Well, once
again we have to use self as a parameter, and then anything else that we wanna add as the second parameter.
"""


class PlayerCharacter:
    # Class Object Attribute (COA)
    membership = True

    def __init__(self, name, age):
        if self.membership:
            # and we can refer it as "PlayerCharacter.membership" above this also works bcoz this is COA attribute.
            self.name = name
            self.age = age

    def shout(self):
        # we're able to use self in this line bcoz we pass the self as an argument in shout() method name.
        print(f'my name is {self.name}')
        # we can't write the below code line in shout() method, bcoz name is not a COA. It's an attribute which is
        # defined in __init__ constructor.
        # print(f'my name is {PlayerCharacter.name}')


player1 = PlayerCharacter('Manthan', 24)
player2 = PlayerCharacter('Mayank', 25)
player2.attack = 50
print(player1.membership)
print(player1.shout())
print(player2.membership)
print(player2.shout())



