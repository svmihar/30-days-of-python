import turtle

wn = turtle.Screen()
wn.title("Pong by svmihar")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(1)

#scoring
score1 = 0
score2 = 0

# paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0) #speed of animation, max possible speed
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0) #x,y


# paddle 2 
paddle2 = turtle.Turtle()
paddle2.speed(0) #speed of animation, max possible speed
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0) #x,y

# ball
ball = turtle.Turtle()
ball.speed(0) #speed of animation, max possible speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0) #x,y
ball.dx = 2
ball.dy = -2

# pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white") 
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("PLAYER 1: 0  PLAYER 2: 0", align="center", font=("Courier", 24, "italic"))

# function 
def paddle1_up(): 
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)
    print(y, "paddle1 up")
def paddle1_down():
    y = paddle1.ycor()
    y-=20
    paddle1.sety(y)
    print(y, "paddle1 down")
def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)
    print(y, "paddle2 up")

def paddle2_down():
    y = paddle2.ycor()
    y-=20
    paddle2.sety(y)
    print(y, "paddle2 down")


# keyboard binding

wn.listen() #listen to keyboard input
wn.onkeypress(paddle1_up,"w")
wn.onkeypress(paddle1_down,"s")
wn.onkeypress(paddle2_up,"Up")
wn.onkeypress(paddle2_down,"Down")


#main game loop
while True: 
    wn.update()

    #move the ball 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check border
        #top and bottom
    if(ball.ycor() > 290):
        ball.sety(290)
        ball.dy *=-1
    if(ball.ycor() < -290):
        ball.sety(-290)
        ball.dy *=-1
        # left and right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1+=1
        pen.clear()
        pen.write("PLAYER 1: {}  PLAYER 2: {}".format(score1, score2), align="center", font=("Courier", 24, "italic"))
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2+=1
        pen.clear()
        pen.write("PLAYER 1: {}  PLAYER 2: {}".format(score1,score2), align="center", font=("Courier", 24, "italic"))
    # check paddle and ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() -40):
         ball.setx(-340)
         ball.dx *= -1


