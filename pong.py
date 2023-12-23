import turtle

#Variables
score_a = 0
score_b = 0
speed_ball = 30

class Paddle:

    def __init__(self, x, y):
        self.turtle = turtle.Turtle()
        self.turtle.speed(0)
        self.turtle.shape("square")
        self.turtle.shapesize(stretch_wid = 5, stretch_len = 1)
        self.turtle.color("white")
        self.turtle.penup() 
        self.turtle.goto(x, y)

    def paddle_movement(self, speed):
        y = self.turtle.ycor() 
        y += speed
        self.turtle.sety(y)

#Functions
        
#Setting up the window
wn = turtle.Screen()
wn.title("Pong by Eric")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Setting up Paddle A
paddle_a = Paddle(-350, 0)

# Setting up Paddle B
paddle_b = Paddle(350, 0)

# Setting up the Ball
ball = turtle.Turtle()
ball.speed(0)  
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#Setting up the scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A:{score_a}  Player B:{score_b}", align="center", font=("Courier", 24, "normal"))


# Keyboard binding
wn.listen() #listen to keyboard input
wn.onkey(lambda: paddle_a.paddle_movement(speed_ball), "w")
wn.onkey(lambda: paddle_a.paddle_movement(-speed_ball), "s")
wn.onkey(lambda: paddle_b.paddle_movement(speed_ball), "Up")
wn.onkey(lambda: paddle_b.paddle_movement(-speed_ball), "Down")

#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A:{score_a}  Player B:{score_b}", align="center", font=("Courier", 24, "normal"))
        
    #Paddle and ball collision
    if (ball.xcor() > 340) and (ball.xcor() < 360) and (ball.ycor() < paddle_b.turtle.ycor() + 40) and (ball.ycor() > paddle_b.turtle.ycor() - 40) :
        ball.dx *= -1
    if (ball.xcor() < -340) and (ball.xcor() > -360) and (ball.ycor() < paddle_a.turtle.ycor() + 40) and (ball.ycor() > paddle_a.turtle.ycor() - 40) :
        ball.dx *= -1
