import sys
import pygame as pg

white = (255,255,255)
gray = (128,128,128)
red = (255,0,0)
purple = (128,0,128)
color = white
pg.init()
run = True
win_x, win_y = 800, 480
mX , mY = 0 , 0
screen = pg.display.set_mode((win_x, win_y))

class Rect: # Rectangle(x,y,w,h)
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height
    def draw(self,screen):
        pg.draw.rect(screen,gray,(self.x,self.y,self.w,self.h))

class Button(Rect):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rect.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        mX, mY = pg.mouse.get_pos()
        if ( self.x <= mX <= self.x + self.w  and self.y <= mY <= self.y + self.h):
            return True
        else :
            return False
        
    def mousePress(self):
        return pg.mouse.get_pressed()[0]
        
btn = Button(0,0,100,100)
while(run):
    screen.fill((255, 255, 255))
    btn.draw(screen)
    
    pg.time.delay(10)
    pg.display.update()
#---------------------------------- hold down -------------------------------- 
    # if pg.key.get_pressed()[pg.K_w]:
    #     btn.y -= 5
    # if pg.key.get_pressed()[pg.K_s]:
    #     btn.y += 5
    # if pg.key.get_pressed()[pg.K_a]:
    #     btn.x -= 5
    # if pg.key.get_pressed()[pg.K_d]:
    #     btn.x += 5

    for event in pg.event.get():
#---------------------------------- press down --------------------------------
        if event.type == pg.KEYDOWN and event.key == pg.K_w: #ปุ่มถูกกดลงและเป็นปุ่ม W
            btn.y -= 5
            print("Key W down")
        if event.type == pg.KEYDOWN and event.key == pg.K_s: #ปุ่มถูกกดลงและเป็นdปุ่ม S
            btn.y += 5
            print("Key S down")
        if event.type == pg.KEYDOWN and event.key == pg.K_a: #ปุ่มถูกกดลงและเป็นปุ่ม A
            btn.x -= 5
            print("Key A down")
        if event.type == pg.KEYDOWN and event.key == pg.K_d: #ปุ่มถูกกดลงและเป็นปุ่ม D
            btn.x += 5
            print("Key D down")
        
        if event.type == pg.QUIT:
            pg.quit()
            run = False