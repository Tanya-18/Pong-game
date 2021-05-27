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
        self.dx = 1
        self.dy = 0.5

    def move(self):
        self.posX = self.posX + self.dx
        self.posY = self.posY+ self.dy

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
            self.posY -= 2
        
        elif self.state == 'down':
            self.posY += 2


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
        paddleright.show()
        paddleleft.move()
        paddleleft.show()

    pygame.display.update()



