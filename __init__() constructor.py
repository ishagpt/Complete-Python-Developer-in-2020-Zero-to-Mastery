""" Remember, a constructor is called every time we instantiate an object! """

class PlayerCharacter:
    membership = True

    """We can do different - 2 things to make sure that we're instantiating the object the proper way.
    We can also give the default parameters - like name can be "anonymous" and let's say age = 0 if the user don't 
    provide it. So, let' say we instantiate the player1 and Player2  without any value, if I click I run I get an 
    error PLayer Object has not attribute name. In __int__ we're able to control and add different - 2 safeguards to 
    perhaps to make sure that we receive their right data type in order to create the object or may be the age is 
    over 18 in order to make sure that when we actually instantiate this "Player1" we're doing it the right way. 
    So, this _init_ gives u a lot of control. """

    def __init__(self, name = 'anonymous', age = 0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Manthan', 24)
print(player1.shout())


