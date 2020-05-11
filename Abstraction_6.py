"""
Second Pillar of OOP's is : Abstraction

Abstraction means : hiding of information or abstracting away the information and giving access to only what's
necessary. So, whatever the user or programmer or the machine is interested in that's the only thing we give access
to everything else we kind of hide it in a blanket underneath the hood because our users don't have to worry about it.
"""


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'my name is {self.name} and I am {self.age} years old')


Player1 = PlayerCharacter('Mayank', 30)

""" 
When we do Player1.speak() we're seeing the abstraction in action because when we click to run this program, we get this
we get the output. But, we don't care how the speak() is implemented. All we know that Player1 has access to speak()
method and I can use it. Same thing when we use list ([].) or tuple (().) we used to get lot of methods suggestion to 
use without knowing about them right? We can't understand the each and every method written else our mind gonna be 
explode. Sometimes, all we need is a method or attribute and just get access to it without having to worry about how 
it's being implemented. We don't need to care about it or at least it makes us more efficient so that we know that a 
works in a certain way and we're not wasting our time learning or coding from scratch.

Example : if we have an iPhone, well that camera feature on an iPhone it'll be nice for an app that we built to use it. 
But, we don't need to actually know exactly how the iPhone camera is coded in iPhone. No, Instead the iPhone usually
gives us a way to say : camera.takepicture() to actually allow us to take a picture without knowing how the Apple 
Engineers actually coded the camera. So, it's very powerful concept. 
"""
print(Player1.speak())

# Let's change the values of player1.name and Player1.speak below and now the Player1 become useless in terms of class
# object.
Player1.name = "!!!!"
Player1.speak = "BOOM BOOM Bumrah! "
print(Player1.speak)

""" what just above happened is really bad! If I have a class that I've abstracted away but anybody can come along, Any 
programmer can come along and just remove all my hard work and overwrite it like that!. 


So, in Python there is the idea of Public and Private and this is related to our discussion of Abstraction. The idea 
behind abstraction is that we hide away information and only give access to things that a user is concerned about. 
Right? So, ideally we shouldn't have access to __init__(), ideally we should not touch those abstracted attributes
and methods. 
"""
tuple1 = (20,30,20,40)
print(len(tuple1))