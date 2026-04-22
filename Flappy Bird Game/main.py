import pygame
import random

# pygame setup
pygame.init()

width=1270
height=720

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Flappy Bird Game")
clock = pygame.time.Clock()

background=pygame.image.load("images/stage.png")
bird=pygame.image.load("images/bird.png")
bird=pygame.transform.scale(bird,(80,80))

lowerPipe=pygame.image.load("images/pipe.png")
lowerPipe=pygame.transform.scale(lowerPipe,(250,int(height/2)))

upperPipe=pygame.image.load("images/pipe.png")
upperPipe=pygame.transform.rotate(upperPipe,180)
upperPipe=pygame.transform.scale(upperPipe,(250,int(height/2)))

hitSound=pygame.mixer.Sound("audio/hit.mp3")

class Game:
    def __init__(self):
        self.gameOn=True
        self.birdX=100
        self.birdY=200
        # width=0
        self.pipeX=[width,width+200,width+400,width+600,width+800,width+1000,width+1200]
        self.lowerPipeY=[self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe()]
        self.upperPipeY=[self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe()]

    def randomLowerPipe(self):
        return random.randrange(int(height/2)+50,height-200)
    
    def randomUpperPipe(self):
        return random.randrange(-int(height/2)+200,-50)

    def gameFlappy(self):
        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            #screen background
            screen.blit(background,(0,0))

            #bird display
            screen.blit(bird,(self.birdX,self.birdY))

            for i in range(7):
                screen.blit(lowerPipe,(self.pipeX[i],self.lowerPipeY[i]))

            for i in range(7):
                screen.blit(upperPipe,(self.pipeX[i],self.upperPipeY[i]))

            #Updating the display according to content
            pygame.display.update()
            clock.tick(60)

myGame=Game()
myGame.gameFlappy()
