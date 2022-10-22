import turtle
import random
t=turtle
screen = t.Screen()
screen.colormode(255)
t.speed("fastest")
t.home()

t.penup()
t.goto(-500,300)
t.pendown()

def gradient():
  for i in range(110):
    t.pencolor(int(50+2.25*i),0,100+4*i)
    t.fillcolor(int(50+2.25*i),0,100+4*i)
    t.begin_fill()
    t.fd(1000)
    t.rt(90)
    t.fd(5)
    t.rt(90)
    t.fd(1000)
    t.rt(90)
    t.fd(5)
    t.rt(180)
    t.fd(5)
    t.lt(90)
    t.end_fill()

gradient()

t.penup()
t.goto(0,-150)
t.pendown
t.pencolor(253,94,83)
t.fillcolor(253,94,83)
t.begin_fill()
t.circle(125)
t.end_fill()

t.pencolor("black")
t.penup()
t.goto(-500,-120)
t.pendown()

t.fillcolor("black")
t.begin_fill()
def the_random(rng,lengh):
  for i in range (lengh):
    t.fd(random.randint(1,3))
    t.rt(random.randint(0,rng))
    t.lt(random.randint(0,rng))
    if (random.randint(1,10) > 9):
      t.setheading(0)
    
the_random(8,500)
t.setheading(270)
t.fd(300)
t.rt(90)
t.fd(1000)
t.rt(90)
t.fd(300)
t.end_fill()





t.penup()
t.goto(-250,-150)
t.pendown()

t.fillcolor("black")
t.begin_fill()
def arc(lengh,strech,curve):
  for i in range(lengh):
    t.forward(strech)
    t.lt(curve)
  t.lt(90)
  t.fd(10)
  t.lt(90)
  for i in range(91):
    t.forward(3)
    t.rt(.3)

arc(93,3,.3)
t.end_fill()
t.lt(90)
t.fd(9)
t.lt(90)


for i in range(93):
  t.forward(3)
  t.lt(.3)

t.fillcolor("black")
t.begin_fill()
t.lt(30)

def triangle(size):
  for i in range(3):
    t.fd(size)
    t.lt(120)

triangle(9)
t.end_fill()
t.fd(10)

t.lt(90)
def leaf(lengh,strech,curve,leaf,cuts):
  for i in range (6):
    t.fillcolor("black")
    t.begin_fill()
    for i in range(lengh):
      t.forward(strech)
      t.lt(curve)
    t.lt(120)
    t.fd(15)
    t.lt(90)
    for i in range(cuts):
      t.fd(10)
      t.rt(leaf)
      t.fd(10)
      t.lt(150)
    t.end_fill()

leaf(40,3,.6,146,19)






t.penup()
t.goto(400,-200)
t.pendown()
t.right(210)

t.fillcolor("black")
t.begin_fill()
def arc(lengh,strech,curve):
  for i in range(lengh):
    t.forward(strech)
    t.lt(curve)
  t.lt(90)
  t.fd(10)
  t.lt(90)
  for i in range(91):
    t.forward(3)
    t.rt(.3)

arc(93,3,.3)
t.end_fill()
t.lt(90)
t.fd(9)
t.lt(90)


for i in range(93):
  t.forward(3)
  t.lt(.3)

t.fillcolor("black")
t.begin_fill()
t.lt(30)

def triangle(size):
  for i in range(3):
    t.fd(size)
    t.lt(120)

triangle(9)
t.end_fill()
t.fd(10)

t.lt(90)
def leaf(lengh,strech,curve,leaf,cuts):
  for i in range (6):
    t.fillcolor("black")
    t.begin_fill()
    for i in range(lengh):
      t.forward(strech)
      t.lt(curve)
    t.lt(120)
    t.fd(15)
    t.lt(90)
    for i in range(cuts):
      t.fd(10)
      t.rt(leaf)
      t.fd(10)
      t.lt(150)
    t.end_fill()

leaf(40,3,.6,146,19)





t.penup()
t.goto(-250,-150)
t.pendown()
t.left(110)

t.fillcolor("black")
t.begin_fill()
def arc(lengh,strech,curve):
  for i in range(lengh):
    t.forward(strech)
    t.lt(curve)
  t.lt(90)
  t.fd(10)
  t.lt(90)
  for i in range(91):
    t.forward(3)
    t.rt(.3)

arc(93,3,.3)
t.end_fill()
t.lt(90)
t.fd(9)
t.lt(90)


for i in range(93):
  t.forward(3)
  t.lt(.3)

t.fillcolor("black")
t.begin_fill()
t.lt(30)

def triangle(size):
  for i in range(3):
    t.fd(size)
    t.lt(120)

triangle(9)
t.end_fill()
t.fd(10)

t.lt(90)
def leaf(lengh,strech,curve,leaf,cuts):
  for i in range (7):
    t.fillcolor("black")
    t.begin_fill()
    for i in range(lengh):
      t.forward(strech)
      t.lt(curve)
    t.lt(120)
    t.fd(15)
    t.lt(90)
    for i in range(cuts):
      t.fd(10)
      t.rt(leaf)
      t.fd(10)
      t.lt(150)
    t.end_fill()

leaf(40,3,.6,146,19)