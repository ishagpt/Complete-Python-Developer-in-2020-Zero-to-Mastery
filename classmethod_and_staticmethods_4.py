class PlayerCharacter:
    # Class Object Attribute (COA)
    membership = True

    def __init__(self, name, age):
        if self.membership:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    """ How the below method is a class method? It's bcoz we actually use this "Player1.add_things(3,8)" without even 
    instantiating a class. We can use this below method with class name too : "PlayerCharacter.add_things_class(5,14)"  
    """

    @classmethod
    # here is the class "PlayerCharacter" that we're referring to below through "cls" in parameters.
    def add_things_class(cls, num1, num2):
        return num1 + num2

    # we can have a whole new player, Player3 by using this class method in below manner.
    @classmethod
    def add_things_class_another_player(cls, num1, num2):
        return cls('Teddy', num1 + num2)

    @staticmethod
    # static method works exact same way it work in class method, except we don't have this "cls" or the class in
    # parameters. We can simply perform some sort of method.
    def add_things_static(num1, num2):
        return num1 + num2


"""
so the only difference in these two @classmethod and @staticmethod is that we don't have access in our parameters
to this "cls". We'll use @staticmethod where we don't care about the class "PlayerCharacter" state. A class state
is something like all it's attributes. We use a @classmethod, when we do care about the attributes (name,age) may
be we wanna modify them or change them. 
"""
Player1 = PlayerCharacter('Manthan', 24)
Player2 = PlayerCharacter('Mayank', 26)
print(Player1.add_things_class(3, 8))
# it's a method "add_things_class" on a actual class "PlayerCharacter". It's a class method. Class methods are not used
# often frequently.
print(PlayerCharacter.add_things_class(5, 14))
Player3 = PlayerCharacter.add_things_class_another_player(2, 6)
print(Player3.name)
print(Player3.age)
