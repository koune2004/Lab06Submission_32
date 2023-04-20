import sys
import pygame as pg

color = [ (0,0,0) , (255,255,255) , (128,128,128) ]

pg.init()
win_x, win_y = 500, 600
screen = pg.display.set_mode((win_x, win_y))

class button:
    def __init__(self,x=0,y=0,w=0,h=0):
        self.x = x # Position X
        self.y = y # Position Y
        self.w = w # Width
        self.h = h # Height

    def isMouseOn(self):
        (mX, mY) = pg.mouse.get_pos()
        if ( self.x <= mX <= self.x + self.w  and self.y <= mY <= self.y + self.h):
            return True
        else:
            return False
        
    def mousePress(self):
        return pg.mouse.get_pressed()[0]
    
    def createButton(self,name):
        pg.draw.rect(screen,color[2],(self.x,self.y,self.w,self.h))
        sub_font = pg.font.Font(None , 30)
        sub_text = sub_font.render(name,True,color[0])
        screen.blit(sub_text,(self.x+10,self.y+10))

COLOR_INACTIVE = pg.Color('lightskyblue3') # ตั้งตัวแปรให้เก็บค่าสี เพื่อนำไปใช้เติมสีให้กับกล่องข้อความตอนที่คลิกที่กล่องนั้นๆอยู่
COLOR_ACTIVE = pg.Color('dodgerblue2')     # ^^^
FONT = pg.font.Font(None, 25)

class InputBox:
    def __init__(self, x, y, w, h, alpha, num, visible, text=''): #เพิ่ม ตัวแปร alpha num visible ซึ่งเป็น parameter ประเภท boolean 
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.alpha = alpha # เป็น parameter ที่กำหนดว่าสามารถพิมพ์ตัวอักษรได้หรือไม่
        self.num = num # เป็น parameter ที่กำหนดว่าสามารถพิมพ์ตัวเลขได้หรือไม่
        self.visible = visible # เป็น parameter ที่กำหนดว่าสามารถมองเห็นตัวที่พิมพ์ได้หรือไม่
        
    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:# ทำการเช็คว่ามีการคลิก Mouse หรือไม่
            if self.rect.collidepoint(event.pos): #ทำการเช็คว่าตำแหน่งของ Mouse อยู่บน InputBox นี้หรือไม่
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE # เปลี่ยนสีของ InputBox
            
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if self.alpha is False and self.num is True : #เช็คว่าพิมพ์ได้เฉพาะตัวเลข
                        if chr(event.key).isnumeric():
                            self.text += event.unicode
                    elif self.alpha is True and self.num is False : #เช็คว่าพิมพ์ได้เฉพาะตัวอักษร
                        if chr(event.key).isalpha():
                            self.text += event.unicode
                    elif self.alpha is True and self.num is True : #เช็คว่าพิมพ์ได้ทั้งตัวอักษรและตัวเลข
                        if chr(event.key).isalnum():
                            self.text += event.unicode

                # Re-render the text.
                if self.visible is True :
                    self.txt_surface = FONT.render(self.text, True, self.color)
                elif self.visible is False :
                    self.txt_surface = FONT.render("*"*len(self.text), True, self.color)
                
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, Screen):
        # Blit the text.
        Screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(Screen, self.color, self.rect, 2)


# ------------------------------------------------------------  setup  ----------------------------------------------------------------------------------
surname_box = InputBox(50, 75, 140, 32, True , False , True)        # create InputBox1
lastname_box = InputBox(50, 200, 140, 32, True , False , True)      # create InputBox2
age_box = InputBox(50, 325, 140, 32, False , True , True)           # create InputBox3
password_box = InputBox(50, 450, 140, 32, True , True , False)      # create InputBox4
input_boxes = [surname_box, lastname_box, age_box, password_box]    # keep InputBox in the list , easy to call and use later

text_font = pg.font.Font('freesansbold.ttf',30)
text_surname = text_font.render("Surname" , True , color[0] )
text_lastname = text_font.render("Lastname" , True , color[0] )
text_age = text_font.render("Age" , True , color[0] )
text_password = text_font.render("Password" , True , color[0] )
run = True
sub_run = False
SM = button(50,530,100,40)
BK = button(win_x-150,530,100,40)
VB = button(win_x-85,450,35,32)
# -------------------------------------------------------------------------------------------------------------------------------------------------------

while run:
    screen.fill((255, 255, 255))
    for box in input_boxes:                                             # ทำการเรียก InputBox ทุกๆตัว โดยการ Loop เข้าไปยัง list ที่เราเก็บค่า InputBox ไว้
        box.update()                                                    # เรียกใช้ฟังก์ชัน update() ของ InputBox
        box.draw(screen)                                                # เรียกใช้ฟังก์ชัน draw() ของ InputBox เพื่อทำการสร้างรูปบน Screen

    screen.blit(text_surname,(50,45))
    screen.blit(text_lastname,(50,170))
    screen.blit(text_age,(50,294))
    screen.blit(text_password,(50,420))


    SM.createButton("Submit")                                           # create submit button
    VB.createButton("0")                                                # create visible button
    if SM.isMouseOn() and SM.mousePress() :                             # rotate to submit info
        sub_run = True
    if VB.isMouseOn() and VB.mousePress() :                             # push to show password
        input_boxes[3].txt_surface = FONT.render(input_boxes[3].text, True, input_boxes[3].color)

    

    if sub_run :
        screen.fill((255, 255, 255))
        font_info = pg.font.Font(None,28)
        text_hello = font_info.render("Hello!! " + input_boxes[0].text + " " + input_boxes[1].text, True , color[0])
        text_tellage = font_info.render("You are " + input_boxes[2].text + " years old" , True , color[0])
        screen.blit(text_hello,(50,45))
        screen.blit(text_tellage,(50,80))
        BK.createButton("Back")                                         # create back button
        if BK.isMouseOn() and BK.mousePress():                          # rotate back to fill in page
            sub_run = False

    pg.time.delay(1)
    pg.display.update()
    
    for event in pg.event.get():
        for box in input_boxes:
            box.handle_event(event)
        if event.type == pg.QUIT:
            pg.quit()
            run = False