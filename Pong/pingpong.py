import turtle
import random
from math import sqrt
import numpy as np
import time
#
#
####
######### Screen
####
#
sc = turtle.Screen()
sc.setup(1000,600)
sc.bgcolor("black")
sc.title("PingPong")
sc.tracer(0)
#
#
#
####
######### Border
####
#
class Border(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.color("white")
		self.penup()
		self.speed(0)
		self.setposition(-500,250)
		self.pensize(3)
# the loop
		for i in range(2):
			self.pendown()
			self.forward(1000)
			self.right(90)
			self.penup()
			self.forward(500)
			self.right(90)
		self.hideturtle()
#
####
######### player 1
####
#
class P1(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.turtlesize(6,1)
		self.penup()
		self.speed(0)
		self.setposition(-450,0)
		self.score = 0
		self.num = 1
	def up(self):
		if self.ycor()<184:
			dy = self.goto(self.xcor(),self.ycor()+24)
	def down(self):
		if self.ycor()>-184:
			dy = self.goto(self.xcor(),self.ycor()-24)
#
####
######### player 2
####
#
class P2(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.turtlesize(6,1)
		self.penup()
		self.speed(0)
		self.setposition(450,0)
		self.score = 0
		self.num = 2
	def up(self):
		if self.ycor()<184:
			dy = self.goto(self.xcor(),self.ycor()+24)
	def down(self):
		if self.ycor()>-184:
			dy = self.goto(self.xcor(),self.ycor()-24)
#
####
######### ball
####
#
class Ball(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.penup()
		self.color("white")
#		self.goto(x,y)
		self.velx = 0.2
		self.vely = 0.2
#
#
	def move(self):
		x = self.xcor()
		y = self.ycor()
		vx = self.velx
		vy = self.vely
		self.goto(x+vx,y+vy)	
#
	def isCollision(self,other):
		a = self.xcor()
		b = other.xcor()
		c = self.ycor()
		d = other.ycor()
#
		h = np.linalg.norm(c-d)
		w = np.linalg.norm(a-b)
#
		if w < 24 and h < 48:
			return True
		else:
			return False
#
####
######### Restart
####
#
	def restart(self):
		self.setposition(0,0)
		
#
####
######### Score boar
####
#
class ScBoard(turtle.Turtle):
	def __init__(self,t,x,y):
		turtle.Turtle.__init__(self)
		self.color("white")
		self.speed(0)
		self.penup()
		self.setposition(x,y)
		self.hideturtle()
		sc = t.score
		self.write(sc, False, align="left", font = ("Helvetica",72,"normal"))
		
#
####
######### Winner?
####
#
class Wins(turtle.Turtle):
	def __init__(self,t,x,y):
		turtle.Turtle.__init__(self)
		self.color("white")
		self.speed(0)
		self.penup()
		self.setposition(x,y)
		self.hideturtle()
		win = "Winner: Player %s" %t.num
		self.write(sc, False, align="left", font = ("Helvetica",50,"normal"))

		
###################################################
###################################################
###################################################
#
## Main?

border = Border()
p1 = P1()
p2 = P2()
ball = Ball()
x = ball.xcor()
y = ball.ycor()
scx1 = 250
scy1 = 50
scx2 = -250
scy2 = 50
score1 = ScBoard(p1,scx1,scy1)
score2 = ScBoard(p2,scx2,scy2)
## Keyboard
#
turtle.listen()
turtle.onkey(p1.up,"w")
turtle.onkey(p1.down,"s")
turtle.onkey(p2.up,"Up")
turtle.onkey(p2.down,"Down")

#turtle.ontimer(ball.move,t=250)
test = True
while test:
	ball.move()
#
# inside the borders
	if ball.ycor()>250 or ball.ycor()<-250:
		ball.vely *= (-1)
#
# bouning
	if ball.isCollision(p1) or ball.isCollision(p2):
#
		ball.velx *= (-1.05)
		ball.vely *= (-1.05)
		ball.move()
#
	if ball.xcor()>500:
		p1.score = p1.score +1
		ball.velx = 0.2
		ball.vely = 0.2
		sc1 = p1.score
		score1.clear()
		score1.write(sc1, False, align="left", font = ("Helvetica",72,"normal"))
		ball.restart()
	if ball.xcor()<-500:
		p2.score = p2.score +1
		ball.velx = -0.2
		ball.vely = 0.2
		sc2 = p2.score
		score2.clear()
		score2.write(sc2, False, align="left", font = ("Helvetica",72,"normal"))
		ball.restart()
#
# winner
#
	if p1.score == 3:
		winner = Wins(p2,-250,-100)
		win = "Winner: Player %s" %p2.num
		winner.clear()
		winner.write(win, False, align="left", font = ("Helvetica",50,"normal"))
		time.sleep(5)
		test = False
	if p2.score == 3:
		winner = Wins(p1,-250,-100)
		win = "Winner: Player %s" %p1.num
		winner.clear()
		winner.write(win, False, align="left", font = ("Helvetica",50,"normal"))
		time.sleep(5)
		test = False
	
#
# end/restart
#	
		
		
	sc.update()
