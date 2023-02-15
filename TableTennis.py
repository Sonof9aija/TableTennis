import math,turtle,random
'''
The three Player control options I chose was To put a background, a scoreboard, and a way to end the game. The picture used was a picture of the US open court
which by some miracle aligned with my pre-built court. It automatically calls game when one side receives 3 points. It then tells the person playing to click
on the screen to close the screen and end the game. The scoreboard is fairly self explanatory.
'''
class Ball(turtle.Turtle):
  '''
  Purpose: Creates a Ball object that has a velocity and position variable for the ball.
  Instance variables: self.px: a variable that represents the x-coordinate of the ball; self.py: a variable that represents the y-coordinate of the ball;
  self.vx: a variable that represents the velocity of the ball on the x-axis; self.vy: a variable that represents the velocity of the ball on the y-axis;
  self.px: a variable that represents how many a ball bounces per side.
  Methods: move: It moves the ball object using the velocity variables. Does so by computing a new position then setting turtle in that position.
  hit: It simulates hitting the ball with a racket by changing the velocity significantly; reset: It resets the ball to a random place on the screen when called
  '''
  def __init__(self,px,py,vx,vy):
    turtle.Turtle.__init__(self)
    self.px = px
    self.py = py
    self.vx = vx
    self.vy = vy
    self.speed(0)
    self.penup()
    self.setpos(self.px,self.py)
    self.shape('circle')
    self.turtlesize(0.3)
    self.bounces = 0

  def move(self):
    self.vy -= .981
    self.px = self.xcor() + self.vx
    self.py = self.ycor() + self.vy
    if self.py < 0:
      self.py *= -1
      self.py *= .75
      self.vy *= -1
      self.vy *= .75
      self.bounces += 1
    self.setpos(self.px,self.py)


  def hit(self):
    self.vx *= -1
    self.vy = 15

  def reset(self):
    self.setpos(random.randint(-100,100),random.randint(30,100))
    self.vx = random.randint(6,12)
    self.vy = random.randint(4,10)


class Game:
  '''
  Purpose: Sets up the game and playing field along with game controls and score keeping
  Instance variables: self.rounds: counts the amount of rounds played so the game quits when a player gets 3 points;
  self.left: represents the left part of the scoreboard; self.right: represents the right part of the scoreboard;
  self.left_score: It represents the score of the left side; self.right_score: It represents the score of the right side;
  self.Ball: represents the ball on the screen
  Methods: gameloop: Uses a combination of methods from turtle and the Ball class. It animates the Ball and moves it across the screen. It also quits after a team
  receives a certain number of points in this case 3 points.
  '''
  def __init__(self):
    self.rounds = 0
    self.left = turtle.Turtle()
    self.right = turtle.Turtle()
    self.left_score = 0
    self.right_score = 0
    turtle.bgpic("USopen.gif")
    turtle.delay(0)
    turtle.tracer(0,0)
    turtle.setworldcoordinates(-500, -500, 500, 500)
    turtle.setpos(-400,0)
    turtle.fd(800)
    turtle.setpos(0,0)
    turtle.left(90)
    turtle.fd(30)
    turtle.ht()
    turtle.penup()
    self.right.ht()
    self.left.ht()
    self.right.penup()
    self.left.penup()
    self.left.setpos(-400, 300)
    self.left.write(self.left_score, font=("Arial", 15, "normal"), align="left")
    self.right.setpos(400, 300)
    self.right.write(self.right_score, font=("Arial", 15, "normal"), align="right")
    self.Ball = Ball(random.randint(-100,100),random.randint(30,100),random.randint(6,12) ,random.randint(4,10))
    turtle.update()
    self.gameloop()
    turtle.onkeypress(self.Ball.hit, "space")
    turtle.listen()
    turtle.mainloop()
  def gameloop(self):
    winner = turtle.Turtle()
    winner.ht()
    winner.penup()
    exit_instructions = turtle.Turtle()
    exit_instructions.ht()
    exit_instructions.penup()
    previous_xcor = self.Ball.xcor()
    previous_ycor = self.Ball.ycor()
    self.Ball.move()
    current_xcor = self.Ball.xcor()
    current_ycor = self.Ball.ycor()
    if self.left_score < 3 and self.right_score < 3:
        if self.Ball.bounces < 2:
            if (previous_xcor > 0 and current_xcor < 0) or (previous_xcor < 0 and current_xcor > 0):
                self.Ball.bounces = 0
                if current_ycor < 30:
                    self.Ball.reset()
                    self.Ball.move()
            turtle.update()
            turtle.ontimer(self.gameloop, 30)
        else:
            self.Ball.bounces = 0
            if current_xcor > 0:
                self.left_score += 1
                self.rounds += 1
                self.left.clear()
                self.left.setpos(-400, 300)
                self.left.write(self.left_score, font=("Arial", 15, "normal"), align="left")
                self.Ball.reset()
                self.Ball.move()
                turtle.update()
                turtle.ontimer(self.gameloop, 30)
            if current_xcor < 0:
                self.right_score += 1
                self.rounds += 1
                self.right.clear()
                self.right.setpos(400, 300)
                self.right.write(self.right_score, font=("Arial", 15, "normal"), align="right")
                self.Ball.reset()
                self.Ball.move()
                turtle.update()
                turtle.ontimer(self.gameloop, 30)
        if self.right_score == 3:
            winner.setpos(0,300)
            winner.write("The right player is the winner!", font=("Arial", 15, "normal"), align="center")
            print("The right player is the winner!")
            exit_instructions.setpos(0,-300)
            exit_instructions.write("Click on the screen to exit the game, Thank You :)", font=("Arial", 15, "normal"), align="center")
            turtle.exitonclick()
        if self.left_score == 3:
            winner.setpos(0,300)
            winner.write("The left player is the winner!", font=("Arial", 15, "normal"), align="center")
            exit_instructions.setpos(0,-500)
            exit_instructions.write("Click on the screen to exit the game, Thank You :)", font=("Arial", 15, "normal"), align="center")
            print("The left player is the winner!")
            turtle.exitonclick()
if __name__ == '__main__':
  Game()
