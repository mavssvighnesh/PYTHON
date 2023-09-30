import turtle

turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

for i in range(3):
      for colours in ["red","blue","green","yellow","white","orange"]:
               turtle.color(colours)
               turtle.circle(100)
               turtle.left(20)

turtle.done()