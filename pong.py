import pygame, sys, random

# self parameter is used to access variables of a particular class
# init will let us create the object for the class ball
class Ball:
    def __init__(self, screen, color, posX, posY, radius): 
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx= 0
        self.dy= 0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)
    
    # will be called as soon as we press the key 'p' , gives starting velocity to the ball
    def start_moving(self):
        self.dx = 0.4
        self.dy = 0.3

    def move(self):
        self.posX = self.posX + self.dx
        self.posY = self.posY+ self.dy

    def paddle_collision(self):
        self.dx= -self.dx

    def wall_collision(self):
        self.dy = -self.dy

class Paddle:
    def __init__(self, screen, color, posX,posY, width, height ):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped' # tells us if the paddle is going up/dowm/or anywhere
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def move(self):
        if self.state == 'up':
            self.posY -= 1
        
        elif self.state == 'down':
            self.posY += 1

    # so that the paddles don't go out of the screen
    def clamp(self):
        if self.posY <= 0:
            self.posY = 0

        if self.posY + self.height >= height:
            self.posY = height-self.height

class CollisionManager:
    def between_ball_and_paddleleft(self, ball, paddleleft):
        if ball.posY + ball.radius > paddleleft.posY and ball.posY - ball.radius < paddleleft.posY + paddleleft.height:
            if ball.posX - ball.radius <= paddleleft.posX + paddleleft.width:
                return True
        
        return False


    def between_ball_and_paddleright(self, ball, paddleright):
        if ball.posY + ball.radius > paddleright.posY and ball.posY - ball.radius < paddleright.posY + paddleright.height:
            if ball.posX + ball.radius >= paddleright.posX:
                return True

        return False
    
    def between_ball_and_walls(self, ball):
        if ball.posY - ball.radius <= 0:
            return True

        if ball.posY + ball.radius >= height:
            return True
        
        return False

pygame.init()

# constants
width = 900
height = 500
black = (0,0,0)
white = (255, 255, 255)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Pongg')

def paint_back():
    screen.fill(black) # fills black background colour
    pygame.draw.line(screen, white, (width//2,0), (width//2, height), 5) # height for the line to go downwards, 5 is the width of the line

paint_back()

# objects

ball = Ball(screen, white, width//2, height//2, 17)
paddleleft = Paddle( screen, white, 15, height//2-55 ,20,110)
paddleright = Paddle( screen, white, width-20-15, height//2-55 ,20,110)
collision = CollisionManager()

playing = False

# mainloop (when exit is typed, we quit the application)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.start_moving()
                playing= True

            if event.key == pygame.K_w:
                paddleleft.state ='up'

            if event.key == pygame.K_s:
                paddleleft.state ='down'

            if event.key == pygame.K_UP:
                paddleright.state ='up'

            if event.key == pygame.K_DOWN:
                paddleright.state ='down'

        # when the user isn't pressing any key       
        if event.type == pygame.KEYUP:
            paddleleft.state ='stopped'
            paddleright.state='stopped'
    
    if playing:
        paint_back()
        ball.move()
        ball.show()

        paddleright.move()
        paddleright.clamp() 
        paddleright.show()

        paddleleft.move()
        paddleleft.clamp()
        paddleleft.show()

        if collision.between_ball_and_paddleleft(ball, paddleleft):
            ball.paddle_collision()

        if collision.between_ball_and_paddleright(ball, paddleright):
            ball.paddle_collision()

        if collision.between_ball_and_walls(ball):
            ball.wall_collision()

    pygame.display.update()



