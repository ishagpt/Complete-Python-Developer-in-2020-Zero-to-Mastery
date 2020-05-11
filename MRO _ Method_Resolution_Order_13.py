""" Let's talk about something that sounds quite complicated it's called as MRO : Method Resolution Order.
What does it mean?  We have brlow example for explanation. """

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B,c):
    pass

