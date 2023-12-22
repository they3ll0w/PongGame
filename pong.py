import turtle

#Variables
score_a=0
score_b=0
speed_ball = 30

no = turtle.Turtle()

#Functions

#For paddle_a
def paddle_a_up_down(speed):
    y = paddle_a.ycor() 
    y += speed
    paddle_a.sety(y)
    
#For paddle_b
def paddle_b_up_down(speed):
    y = paddle_b.ycor() 
    y += speed
    paddle_b.sety(y)

#Setting up the window
wn = turtle.Screen()
wn.title("Pong by Eric")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Setting up Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup() 
paddle_a.goto(-350,0)

# Setting up Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square") 
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

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
pen.goto(0,260)
pen.write(f"Player A:{score_a}  Player B:{score_b}", align="center", font=("Courier", 24, "normal"))


# Keyboard binding
wn.listen() #listen to keyboard input
wn.onkeypress(paddle_a_up_down(speed_ball), "w")
wn.onkeypress(paddle_a_up_down(-speed_ball), "s")
wn.onkeypress(paddle_b_up_down(speed_ball), "Up")
wn.onkeypress(paddle_b_up_down(speed_ball), "Down")

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
        pen.write(f"Player A:{score_a}  Player B:{score_b}", align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A:{score_a}  Player B:{score_b}", align="center", font=("Courier", 24, "normal"))
        
    #Paddle and ball collision
    if (ball.xcor() > 340) and (ball.xcor() < 360) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40) :
        ball.dx *= -1
    if (ball.xcor() < -340) and (ball.xcor() > -360) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40) :
        ball.dx *= -1
