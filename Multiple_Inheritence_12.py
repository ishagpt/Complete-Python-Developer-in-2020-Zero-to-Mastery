""" Let's talk about Multiple Inheritance, which we're able to do in Python. """


class User():
    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of : {self.power}')


class Archer(User):
    def __init__(self, name, num_of_arrows):
        self.name = name
        self.num_of_arrows = num_of_arrows

    def check_arrows(self):
        print(f'{self.name} is now left with only : {self.num_of_arrows}')

    def run(self):
        print("Run, really Fast!")


wizard1 = Wizard('Robin', 60)
archer1 = Archer('Merlin', 100)

""" We have created another class below. Now, we want to have this class all of the above methods of above classes : 
Users, Wizard, Archer. is it possible? Yes, it's. All we need to do is say Wizard and Archer class in parameters of 
HybridBrog class. We can give it as many parameters as we want as simple inheritances. We're inheriting from Wizard and 
 Archer. 
 
 When you do multiple inheritance, things can get complicated. Imagine if there was a code came along on your team at 
 work and tried to understand this code. Well, we've added quite a bit of logic here and things are getting more 
 complicated below and it's hard to keep track of everything in your head. And this is why multiple inheritance is one 
 of those things where it's really really powerful but with great power comes great responsibility bcoz we're creating 
 more and more complexity. Again, part of the reason that some programming languages don't actually allow you to do
   multiple inheritance."""


class HybridBrog(Wizard, Archer):
    def __int__(self,name,power,num_of_arrows):
        Archer.__init__(self,name,num_of_arrows)
        Wizard.__init__(self,name,power)


hb1 = HybridBrog('Aashu', 70, 68)
print(hb1.run())
print(hb1.sign_in())
print(hb1.attack())
print(hb1.check_arrows())