import pyxel
from random import *

class main:
    def __init__(self):
        pyxel.init(256, 256, title="naval", fps=30, quit_key=pyxel.KEY_ESCAPE)
        pyxel.load("theme.pyxres")
        self.x=50
        self.y=50
        self.r=0
        self.niv=1
        self.can=1
        self.gold=0
        self.nivsuiv=10
        self.xc=None
        self.yc=None
        self.feu=False
        self.dirx=0
        self.diry=0
        self.anim=False
        self.etape=0

        pyxel.run(self.update, self.draw)

    def update(self):
            self.ship()
            self.tir()
            self.animation()

    def draw(self):
        pyxel.bltm(0, 0, 1, 0, 0, 256, 256)
        pyxel.blt(self.x, self.y, 0, 35, 2, 10, 12, 5, self.r, 1)
        pyxel.text(5, 5, f"niveau {self.niv}, {self.can} canon(s) de chaques cotés" , 7)
        pyxel.text(5, 10, f"argent : {self.gold}", 7)
        if self.feu==True:
            pyxel.blt(self.xc, self.yc, 0, 80, 32, 2, 2)
        if self.etape:
            if self.etape==0:
                pyxel.blt(self.xc-5, self.yc-5, 0, 50, 3, 11, 10, 5)
            elif self.etape==1:
                pyxel.blt(self.xc-6, self.yc-6, 0, 65, 2, 13, 12, 5)
            if self.etape==2:
                pyxel.blt(self.xc-8, self.yc-8, 0, 80, 0, 16, 16, 5)

    def ship(self):
        self.id=[]
        if pyxel.btnp(pyxel.KEY_RIGHT,1,2):
            self.x = min(245,self.x + 1)
            self.r=90

        elif pyxel.btnp(pyxel.KEY_LEFT,1,2):
            self.x = max(1,self.x - 1)
            self.r=270

        elif pyxel.btnp(pyxel.KEY_UP,1,2):
            self.y = max(1,self.y - 1)
            self.r=0

        elif pyxel.btnp(pyxel.KEY_DOWN,1,2):
            self.y = min(245,self.y + 1)
            self.r=180
    
    def tir (self):
        if self.feu==False:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT,1,10) :
                self.feu = True
                if self.r==0 or self.r==180:
                    if self.r==0:
                        self.dirx = -5
                        self.diry = 0
                    elif self.r==180:
                        self.dirx = 5
                        self.diry = 0
                    self.xc = self.x + 5
                    self.yc = self.y + 8
                elif self.r==90 or self.r==270:
                    if self.r==90:
                        self.diry = -5
                        self.dirx = 0
                    elif self.r==270:
                        self.diry = 5
                        self.dirx = 0
                    self.xc = self.x + 8
                    self.yc = self.y + 5
                    self.dtir =0
                self.a = 0

            elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT,1,10) :
                self.feu = True
                if self.r==0 or self.r==180:
                    if self.r==0:
                        self.dirx = 5
                        self.diry = 0
                    elif self.r==180:
                        self.dirx = -5
                        self.diry = 0
                    self.xc = self.x + 5
                    self.yc = self.y + 8
                elif self.r==90 or self.r==270:
                    if self.r==90:
                        self.diry = 5
                        self.dirx = 0
                    elif self.r==270:
                        self.diry = -5
                        self.dirx = 0
                    self.xc = self.x + 8
                    self.yc = self.y + 5
                self.a = 0

        elif self.feu==True:
            if self.a != 30:
                self.a += 1
                if self.a%2==0:
                    self.xc = self.xc + self.dirx
                    self.yc = self.yc + self.diry
            else:
                self.feu = False
                self.a = 0
                self.anim=True
                self.etape=0
                
    def animation(self): 
        if self.anim==True: 
            if self.etape==0: 
                self.etape+=1 
            elif self.etape==1:
                self.etape+=1 
            elif self.etape==2:
                self.etape=None
                self.anim=True

    def ennemis(self):
        self.niv1=randint(5,10)
        self.niv2=randint(3,5)
        self.niv3=randint(1,3)
        self.niv3=randint(0,1)

main()