import tensorflow as tf 
import pygame 
import random 

FPS = 60

WINDOWS_WIDTH = 400
WINDOWS_HEIGHT= 400

#size of paddle 
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60

#ball size 
BALL_WIDTH = 10
BALL_HEIGHT = 10

#distance from the edge of the window
PADDLE_BUFFER = 10

# speed of paddle and ball 
PADDLE_SPEED = 2
BALL_X_SPEED = 3
BALL_Y_SPEED = 2

#RGB colors for paddle and ball
WHITE = (255,255,255)
BLACK = (0,0,0)

#initialize our screen 
screen = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))


def drawBall(ballXpos, ballYpos):
    ball = pygame.Rect(ballXpos, ballYpos, BALL_WIDTH, BALL_HEIGHT)
    pygame.draw.Rect(screen,WHITE,ball)

def drawPaddle1(paddle1Ypos):
    paddle1 = pygame.Rect(PADDLE_BUFFER, paddle1Ypos, PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.Rect(screen, WHITE, paddle1)

def drawPaddle2(paddle2Ypos):
    paddle2 = pygame.Rect(WINDOWS_WIDTH-PADDLE_BUFFER-PADDLE_WIDTH,paddle2Ypos,PADDLE_WIDTH, PADDLE_HEIGHT)
    pygame.draw.Rect(screen, WHITE, paddle2)

def updateBall(paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection):
    #update x and y pos 
    ballXpos += ballXDirection * BALL_X_SPEED
    ballYpos += ballYDirection * BALL_Y_SPEED
    score = 0

     #checks for a collision, if the ball hits the left side
    if (ballXpos <= PADDLE_BUFFER + PADDLE_WIDTH and ballYpos + BALL_HEIGHT >= paddle1Ypos and ballYpos - BALL_HEIGHT <= paddle1Ypos + PADDLE_HEIGHT):
        #switches directions
        ballXDirection = 1
    #past it
    elif (ballXpos <= 0):
        #negative score
        ballXDirection = 1
        score = -1
        return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]


    #check if hits the other sid e
    if (ballXpos >= WINDOWS_WIDTH - PADDLE_WIDTH - PADDLE_BUFFER and ballYpos + BALL_HEIGHT >= paddle2Ypos and ballYpos - BALL_HEIGHT <= paddle2Ypos + PADDLE_HEIGHT):
        ballXDirection = -1
    elif ballXpos >= WINDOWS_WIDTH - BALL_WIDTH:
        ballXDirection = -1
        score = 1
        return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]

    if(ballYpos<=0):
        ballYpos=0
        ballYDirection= 1
    elif ballYpos >= WINDOWS_HEIGHT-BALL_HEIGHT:
        ballYpos = WINDOWS_HEIGHT-BALL_HEIGHT
        ballYDirection = -1
    return [score, paddle1Ypos, paddle2Ypos, ballXpos, ballYpos, ballXDirection, ballYDirection]
        
def updatePaddle1(action, paddle1Ypos):
    #moves up 
    if(action[1] == 1): 
        paddle1Ypos -= PADDLE_SPEED
    #moves down 
    if(action[2]==1):
        paddle1Ypos += PADDLE_SPEED
    #don't let it move off the screen 
    if(paddle1Ypos <0 ):
        paddle1Ypos = 0
    if(paddle1Ypos > WINDOWS_HEIGHT- PADDLE_HEIGHT):
        paddle1Ypos = WINDOWS_HEIGHT - PADDLE_HEIGHT
    return paddle1Ypos

def updatePaddle2(paddle2Ypos, ballYpos):
    #up 
    if(paddle2Ypos + PADDLE_HEIGHT/2 < ballYpos + BALL_HEIGHT/2):
        paddle2Ypos += PADDLE_SPEED
    #up if ball lower in half 
    if(paddle2Ypos + PADDLE_HEIGHT/2 > ballYpos + BALL_HEIGHT/2):
        paddle2Ypos = paddle2Ypos - PADDLE_SPEED
    #don't let it hit top 
    if(paddle2Ypos < 0):
        paddle2Ypos = 0
    #don't let it hit bottom 
    if(paddle2Ypos > WINDOWS_HEIGHT - PADDLE_HEIGHT):
        paddle2Ypos = WINDOWS_HEIGHT - PADDLE_HEIGHT
    return paddle2Ypos

#game calss
class PongGame: 
    def __init__(self):
        #random number for initial direction of ball 
        num = random.randint(0,9)
        #keep score
        self.tally = 0
        #initiate positiions of the paddle 
        self.paddle1Ypos = WINDOWS_HEIGHT/2 - PADDLE_HEIGHT/2
        self.paddle2Ypos = WINDOWS_HEIGHT/2 - PADDLE_HEIGHT/2
        #initiate positions of ball direction 
        self.ballXDirection = 1
        self.ballYDirection = 1
        #starting point of ball pos 
        self.ballXpos = WINDOWS_HEIGHT/2 - BALL_WIDTH /2

        #randomly decide where will the ball move 
        if(0<num<3):
            self.ballXDirection = 1
            self.bally = 1
        if(3<= num <5):
            self.ballXDirection = -1
            self.ballYDirection = 1
        if(5<= num < 8):
            self.ballXDirection = 1
            self.ballYDirection = -1
        if(8 <= num <10):
            self.ballXDirection = -1
            self.ballYDirection = -1
        #new random number 
        num - random.randint(0,9)

        #where will stat, y part 
        self. ballYpos = num*(WINDOWS_HEIGHT - BALL_HEIGHT)/9
    def getPresentFrame(self):
        #call event queue every frame
        pygame.event.pump()

        screen.fill(BLACK)

        #draw paddles
        drawPaddle1(self.paddle1Ypos)
        drawPaddle2(self.paddle2Ypos)

        #draw balls
        drawBall(self.ballXpos, self.ballYpos)

        image_data = pygame.surfarray.array3d(pygame.display.get_surface())

        #updates the window
        pygame.display.flip()

        #return our surface data
        return image_data

    #update our screen 
    def getNextFrame(self, action):
        pygame.event.pump()
        score = 0 
        screen.fill(BLACK)

        #update paddle
        self.paddle1YPos = updatePaddle1(action, self.paddle1YPos)
        drawPaddle1(self.paddle1YPos)

        #update ai paddle
        self.paddle2Ypos = updatePaddle2(self.paddle2Ypos, self.ballYpos)
        drawPaddle2(self.paddle2Ypos)

        #update our vars by updating ball position
        [score, self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection] = updateBall(self.paddle1YPos, self.paddle2YPos, self.ballXPos, self.ballYPos, self.ballXDirection, self.ballYDirection)

        #draw the ball 
        drawBall(self.ballXpos, self.ballYpos)

        #get the surface data 
        image_data = pygame.surfarray.array3d(pygame.display.get_surface())

        #update window
        pygame.display.flip()

        #record the total score
        self.tally += score
        print("tally is " + str(self.tally))

        #return score and surface data
        return [score, image_data]
        