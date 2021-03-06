import turtle as trt
from math import sqrt
import random
#
## set screen
sc = trt.Screen()
sc.setup(800,800)
sc.bgcolor("black")
sc.title("Maze")
sc.tracer(0)
#
## images
images = []
for image in images:
	turtle.register_shape(image)
#
## creating a class
#
class Wh_Sq(trt.Turtle): #same properties as Turtle
	def __init__(self):
		trt.Turtle.__init__(self) #initialize Turtle
		self.shape("square")
		self.color("white")
		self.penup() #we don't want to draw
		self.speed(0)
#any Cosa has these properties	  
#
#
## treasure
class Treasure(trt.Turtle):
	def __init__(self,x,y):
		trt.Turtle.__init__(self)
		self.shape("square")
		self.color("gold")
		self.penup()
		self.setheading(90)
		self.speed(0)
		self.goto(x,y)
#
	def destroy(self):
		self.goto(2000,2000)
		self.hideturtle()
## enemy
class Enemy(trt.Turtle):
	def __init__(self,x,y):
		trt.Turtle.__init__(self)
		self.shape("triangle")
		self.color("red")
		self.penup()
		self.setheading(90)
		self.speed(0)
		self.goto(x,y)
		self.direction = random.choice(["up","down","left","right"])
	def move(self):
		if self.direction == "up":
			dx = 0
			dy = 24
		elif self.direction == "down":
			dx = 0
			dy =-24
		elif self.direction == "left":
			dx = -24
			dy = 0
		elif self.direction == "right":
			dx = 24
			dy = 0
		else:
			dx = 0
			dy = 0
#
		if self.isClose(player):
			if player.xcor() < self.xcor:
				self.direction == "left"
			elif player.xcor() >self.xcor:
				self.direction == "right"
			elif player.ycor() > self.ycor:
				self.direction == "up"
			elif player.ycor() < self.ycor:
				self.direction == "down"

#
#
		move_to_x = self.xcor()+dx
		move_to_y = self.ycor()+dy
#
#
		if (move_to_x,move_to_y) not in walls:
			self.goto(move_to_x,move_to_y)
		else:
			self.direction = random.choice(["up","down","left","right"])
#
		trt.ontimer(self.move,t=random.randint(100,300))
#
	def isClose(self,x1):
		distance =  sqrt((self.xcor()-x1.xcor())**2+(self.ycor()-x1.ycor())**2)
		if distance < 148:
			return True
		else:
			return False
#
## player
class Player(trt.Turtle):
	def __init__(self):
		trt.Turtle.__init__(self)
		self.shape("circle")
		self.color("green")
		self.penup()
		self.speed(0)
#
#
## motion
	def go_up(self):
		up_x = self.xcor()
		up_y = self.ycor()+24
		if (up_x,up_y) not in walls:
			self.goto(self.xcor(), self.ycor()+24)
	def go_down(self):
		down_x = self.xcor()
		down_y = self.ycor()-24
		if (down_x,down_y) not in walls:
			self.goto(self.xcor(), self.ycor()-24)
	def go_right(self):
		right_x = self.xcor()+24
		right_y = self.ycor()
		if (right_x,right_y) not in walls:
			self.goto(self.xcor()+24, self.ycor())
	def go_left(self):
		left_x = self.xcor()-24
		left_y = self.ycor()
		if (left_x,left_y) not in walls:
			self.goto(self.xcor()-24, self.ycor())
#	
	def isCollision(self,x1):
		distance =  sqrt((self.xcor()-x1.xcor())**2+(self.ycor()-x1.ycor())**2)
		if distance < 5:
			return True
		else:
			return False
## The levels
#
levels = [""]
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP  XXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX EXXX        XX",
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",
"X  XXX  XXXXXXXXXXXXXXXXX",
"XE        XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX               E     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XXT  XXXXX        E     X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX           XXXX       X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
#
#
#
## lists
walls = []
treasures = []
enemies = []
## The maze
def set_up(levels):
	for i in range(len(levels)):
		for j in range(len(levels[i])):
			#	
			char = levels[i][j]
			sc_x = -288 + (j*24) #x
			sc_y = 288 - (i*24)  #y
		
			if char == "X":
				wh_sq.goto(sc_x,sc_y)
				walls.append((sc_x,sc_y))
				wh_sq.stamp()
			if char == "P":
				player.goto(sc_x,sc_y)
			if char == "T":
				treasures.append(Treasure(sc_x,sc_y))
			if char == "E":
				enemies.append(Enemy(sc_x,sc_y))
				



ini_x = -264
ini_y = 264


wh_sq = Wh_Sq()
player = Player()
set_up(level_1)


#
#
## Keyboard
trt.listen()
trt.onkey(player.go_up,"Up")
trt.onkey(player.go_down,"Down")
trt.onkey(player.go_right,"Right")
trt.onkey(player.go_left,"Left")

for enemy in enemies:
		trt.ontimer(enemy.move,t=250)
		
test = True
while test:
	for treasure in treasures:
		if player.isCollision(treasure):
			print "YOU WIN"
			treasures.remove(treasure)
			treasure.destroy()
			test = False
	for enemy in enemies:
		if player.isCollision(enemy):
			print "Game over"
			player.goto(ini_x,ini_y)
			
	
	sc.update()

