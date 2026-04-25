import pygame
import random
import sys

# pygame setup
pygame.init()

width=1270
height=720

screen = pygame.display.set_mode((width,height))

pygame.display.set_caption("Flappy Bird Game")
clock = pygame.time.Clock()

background=pygame.image.load("images/stage.png")
bird=pygame.image.load("images/bird.png")
bird=pygame.transform.scale(bird,(80,80)).convert_alpha()

lowerPipe=pygame.image.load("images/pipe.png")
lowerPipe=pygame.transform.scale(lowerPipe,(250,int(height/2))).convert_alpha()

upperPipe=pygame.image.load("images/pipe.png")
upperPipe=pygame.transform.rotate(upperPipe,180)
upperPipe=pygame.transform.scale(upperPipe,(250,int(height/2))).convert_alpha()

hitSound=pygame.mixer.Sound("audio/hit.mp3")

class Game:
    def __init__(self):
        self.gameOn=True
        self.birdX=100
        self.birdY=200

        self.pipVel=0
        self.gravity=0
        self.flap=0
        self.rotateAngle=0
        self.isGameOver=False
        self.playSound=False


        self.pipeX=[width,width+200,width+400,width+600,width+800,width+1000,width+1200]
        self.lowerPipeY=[self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe(),self.randomLowerPipe()]
        self.upperPipeY=[self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe(),self.randomUpperPipe()]
         
    
    def isCollide(self):
        for i in range(7):
            if((self.birdX-20>=self.pipeX[i] and self.birdX<=self.pipeX[i]+lowerPipe.get_width()) and
                (self.birdY+bird.get_height()-40>self.lowerPipeY[i] or self.birdY+40<=self.upperPipeY[i]+upperPipe.get_height())
               ):
                return True
            
        if(self.birdY<=0 or self.birdY+bird.get_height()>=height):
            return True
        
    def screenText(self,text,color,x,y,size,bold,style):
        font=pygame.font.SysFont(style,size,bold=bold)
        screentxt=font.render(text,True,color)
        screen.blit(screentxt,(x,y))
    
    def gameOver(self):
        if(self.isCollide()):
            self.isGameOver=True
            self.gravity=0
            self.flap=0
            self.pipVel=0
            self.rotateAngle=0
            self.screenText("Game Over !!!",(255,25,255),450,300,85,True,"Fixedsys")
            self.screenText("Please enter to play again !!!",(25,255,255),350,380,75,True,"Fixedsys")
            if(self.playSound==False):
                pygame.mixer.Sound.play(hitSound)
                self.playSound=True
        
    def flapBird(self):
        if(self.isGameOver==False):
            self.birdY+=self.gravity
            self.flap-=1
            self.birdY-=self.flap

    def movingPipe(self):
        for i in range(7):
            self.pipeX[i]-=self.pipVel
        for i in range(7):
            if (self.pipeX[i] < -100):
                self.pipeX[i]=width+50
                self.lowerPipeY[i]=self.randomLowerPipe()
                self.upperPipeY[i]=self.randomUpperPipe()

    def randomLowerPipe(self):
        return random.randrange(int(height/2)+50,height-200)
    
    def randomUpperPipe(self):
        return random.randrange(-int(height/2)+200,-50)

    def gameFlappy(self):
        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        if(self.isGameOver==False):
                            self.pipVel=5
                            self.gravity=10
                            self.flap=20
                            self.rotateAngle=15
                    if(self.isGameOver==True):
                        if event.key==pygame.K_RETURN:
                            newObj=Game()
                            newObj.gameFlappy()

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_SPACE:
                        self.rotateAngle=0
            
            #screen background
            screen.blit(background,(0,0))

            #bird display
            screen.blit(pygame.transform.rotozoom(bird,self.rotateAngle,1),(self.birdX,self.birdY))
 
            for i in range(7):
                screen.blit(lowerPipe,(self.pipeX[i],self.lowerPipeY[i]))

            for i in range(7):
                screen.blit(upperPipe,(self.pipeX[i],self.upperPipeY[i]))

            self.movingPipe()
            self.flapBird()

            self.gameOver()
            #Updating the display according to content
            pygame.display.update()
            clock.tick(60)

myGame=Game()
myGame.gameFlappy()
