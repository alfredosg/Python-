

import turtle as tu
import os
from math import sqrt
from random import randint
#
#
#Screen
sc = tu.Screen()
sc.bgcolor("black")
sc.title("Space Invaders")
sc.bgpic("space_invaders_background.gif")
#
#
## Border
#
border = tu.Turtle() #a turtle is the arror or smt like that
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pensize(3)
border.pendown()
for side in range(4):
	border.forward(600)
	border.left(90)
border.hideturtle()
#
#
## score
#
sc = 0
score = tu.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.setposition(-290,250)
score.hideturtle()
score_string = "Score: %s" %sc
score.write(score_string, False, align="left", font = ("Arial",14,"normal"))
#
## Register shapes
#
tu.register_shape("player.gif")
tu.register_shape("invader.gif")
## Player
#
player= tu.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.setposition(0,-250)
player.speed(0)
player.setheading(90)
#
#
## Shoot
#
pew = tu.Turtle()
pew.color("white")
pew.shape("square")
pew.shapesize(0.2,0.2,1)
pew.speed(0)
pew.penup()
pew.hideturtle()
#	ready to pew?
pew_state = "ready"
#
#
# Enemies
#
num_en = 5
enemies = []
for i in range(num_en):
	enemies.append(tu.Turtle())
#
## enemy
#
for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup() 
	enemy.setposition(randint(-280,280),randint(100,240))
	enemy.speed(0)
#
#
## motion
#
v_pl = 15 #velocity
v_en = 2
v_pew = 20
#
#
# lef and right
#
def move_left():
	x_pl = player.xcor()
	x_pl = x_pl - v_pl
	if x_pl < -280:
		x_pl = 280
	player.setx(x_pl)
def move_right():
	x_pl = player.xcor()
	x_pl = x_pl + v_pl
	if x_pl > 280:
		x_pl = -280
	player.setx(x_pl)
def move_down():
	y_pl = player.ycor()
	y_pl = y_pl - v_pl
	if y_pl < -280:
		y_pl = -280
	player.sety(y_pl)
def move_up():
	y_pl = player.ycor()
	y_pl = y_pl + v_pl
	if y_pl > 280:
		y_pl = 250
	player.sety(y_pl)
#
#
## shoot
#
def shoot():
	global pew_state
	if pew_state == "ready":
		os.system("aplay laser.wav&")
		pew_state = "pum"
		x_pl = player.xcor()
		y_pl = player.ycor()+10
		pew.setposition(x_pl,y_pl)
		pew.showturtle()
#
#
## Distance
#
def dist(t1,t2):
	return sqrt((t1.xcor()-t2.xcor())**2 + (t1.ycor()-t2.ycor())**2)
#
#
## Collision
#
def iscollision(x1,x2):
	if dist(x1,x2) < 15:
		return True
	else:
		return False
## keyboard 
tu.listen()
#
tu.onkey(move_left,"Left") 
tu.onkey(move_right,"Right")
#	
tu.onkey(move_up,"Up")
tu.onkey(move_down,"Down")
#
tu.onkey(shoot,"space")
#
#
#
## Main game loop
while True:
		# shooting
	y_pew = pew.ycor()
	if pew_state == "pum":
		y_pew = y_pew + v_pew
		pew.sety(y_pew)
	# bullet to the top
	if y_pew > 280:
		pew.hideturtle()
		pew_state = "ready"
	for enemy in enemies:
		#move the enemy
		x_en = enemy.xcor()
		y_en = enemy.ycor()
		x_en = x_en + v_en 
		enemy.setx(x_en)
		# back and down	
		if x_en >280 or x_en <-280:
			for e in enemies:
				y_en2 = e.ycor()
				y_en2 = y_en2 - 10
				e.sety(y_en2)
			v_en = v_en*(-1)
		# check collision
		if iscollision(pew,enemy):
			pew.hideturtle()
			pew.setposition(0,-400)
			bulletstate = "ready"
			#reset
			enemy.setposition(randint(-280,280),randint(100,240))
			sc = sc +100
			score_string = "Score: %s" %sc
			score.clear()
			score.write(score_string, False, align="left", font = ("Arial",14,"normal"))
		if iscollision(player,enemy):
			break
#		
print "Game Over"














raw_input("Press ENTER to finish: ")

