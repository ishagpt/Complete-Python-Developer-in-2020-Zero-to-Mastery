"""
Fourth Pillar of OOP's is : Polymorphism

Well, Poly means : many and morphism means: form. So, ManyForms.
Now, we know that methods belongs to objects. Right? We use the self keyword to act upon the object that got
instantiated. Now, in Python this idea of PolyMorphism refers to the way in which object classes can share the same
method name. But, those method names can act differently based on what object calls them.

So now, let's look at the code. We have our Wizard and Archer Classes and as I mentioned with PolyMorphism different
object classes can share method names. So, we have attack() method here below that is shared with all classes
(User, Archer,Wizard) below but each one does something different thing based on their attributes
(name,power,num_of_arrows).
"""


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
        print(f'{self.name} is now left with only : {self.num_of_arrows} arrows!')


wizard1 = Wizard('Robin', 60)
archer1 = Archer('Merlin', 100)

""" the attack() methods of Wizard class and Archer class is different. So, although they shared the same method names
because of the object that's calling it the output is going to be different. Let's say we have wizard1 and archer1 
objects of Wizard and Archer classes below. Now, what we will  do it here is actually called them in different ways. 
For example : we can create an  entire new function called player_attack() and this player_attack() takes a 
character(char) and in next line we can say character.attack() then run the code below """


def player_attack(char):
    char.attack()


""" we could see the same function attack() give us a different - different output, even though we're calling the same 
things bcoz of the object we pass below into it. That's the PolyMorphism."""

# player_attack(wizard1)
# player_attack(archer1)

""" Another way to demonstrate this if we do a for loop. !! But comment the above two lines of code first!! 
We can have once again two different outputs. Although I am 
calling the same method because of the different objects and this is really powerful concept. Because we're able to 
customise this according to our specific needs even if let's say that the "User" class have a "attack()" method, even if
we run, let's say wizard1.attack() and we run it, it's going to override whatever the original "attack()" (method in 
"User" class) was because we already have that method (attack() method in "Wizard" class.).

But, let's say we wanted to have both User and Wizard class run the attack() method. How can we do this? 
Now, go to "Wizard" class above and see how the "User" class also using it's "attack()" method. Because we use the 
"User" as parameter in "Wizard" class. So, we can run thr User.attack() """

for char in [wizard1, archer1]:
    char.attack()

"""So, polymorphism allows us to have many forms. it's the ability to redefine methods for the derived classes that in 
case here are : Wizard and Archer classes, and an object that get's instantiated can behave in different forms in 
different ways based on Polymorphism, and this is useful because we're able to modify our classes to our specific needs 
but also not have to repeat ourselves in case we want to use something like "attack()" from User inside of wizard. So, 
there's we have it all four pillars of OOP!

Caution : Now, no amount of video or books are going to teach you exactly when to use what."""



