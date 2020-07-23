import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("black")
turtle.setup(600,600)

screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("pink")
bob.speed(0)

def square(size):
  for i in range(4):
    bob.forward(size)
    bob.right(90)


def pattern():
  size = 360 
  for i in range(36):
    square(size)
    bob.right(10)
    size -= 10


pattern()