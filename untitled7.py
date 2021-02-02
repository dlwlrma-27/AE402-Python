import turtle
cosmo=turtle.Turtle()
n=int(input("enter a number"))
for i in range(n):
     cosmo.forward(100)
     cosmo.left(360/n)