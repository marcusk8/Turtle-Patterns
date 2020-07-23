import turtle



turtle.title("Drawing Turtle")
turtle.bgcolor("Blue")
turtle.setup(600,600)



screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(0)
bob.pensize(3)

def square(size):
  for i in range(4):
    bob.forward(size)
    bob.right(90)


def pattern():
  size = 50 
  for i in range(36):
    square(size)
    bob.right(10)
    size -= 10

pattern()