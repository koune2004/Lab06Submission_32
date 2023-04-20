import sys
import pygame as pg

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
        pg.draw.rect(screen,(233,205,208),(self.x,self.y,self.w,self.h))

class Button(Rect):
    def __init__(self, x=0, y=0, w=0, h=0):
        Rect.__init__(self, x, y, w, h)
    
    def isMouseOn(self):
        (mX, mY) = pg.mouse.get_pos()
        if ( self.x <= mX <= self.x + self.w and self.y <= mY <= self.y + self.h):
            return True
        else :
            return False
        
btn = Button(0,0,0,0)

while(run):
    screen.fill((255, 255, 255))
    if btn.isMouseOn(): # if mouse is on object , it will change size.
        btn.w = 400
        btn.h = 200
        btn.x = (win_x/2)-(btn.w/2)
        btn.y = (win_y/2)-(btn.h/2)
    else : # in the normal case my mouse isn't on the object ,it's normal size 
        btn.w = 100
        btn.h = 50
        btn.x = (win_x/2)-(btn.w/2)
        btn.y = (win_y/2)-(btn.h/2)
    btn.draw(screen)

    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False