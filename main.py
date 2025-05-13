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
        self.dirx=None
        self.diry=None
        self.anim=False
        self.etape=0
        self.dtir =0

        pyxel.run(self.update, self.draw)

    def update(self):
            self.ship()
            self.tir()
            self.anim()

    def draw(self):
        pyxel.cls(5)
        pyxel.blt(self.x, self.y, 0, 35, 2, 10, 12, 5, self.r, 1 )
        pyxel.text(5, 5, f"niveau {self.niv}, {self.can} canon(s) de chaques cotés" , 7)
        pyxel.text(5, 10, f"argent : {self.gold}", 7)
        if self.feu==True:
            pyxel.blt(self.xc, self.yc, 0, 80, 32, 2, 2, )
        if self.etape:
            if self.etape=0:
                pyxel.blt(self.xc, self.yc, 0, 35, 2, 10, 12, 5, self.r, 1 )
            elif self.etape=1:

            if self.etape=2:
        
    def ship(self):
        self.id=[]
        if pyxel.btnp(pyxel.KEY_RIGHT,1,2):
            self.x = self.x + 1
            self.r=90

        elif pyxel.btnp(pyxel.KEY_LEFT,1,2):
            self.x = self.x - 1
            self.r=270

        elif pyxel.btnp(pyxel.KEY_UP,1,2):
            self.y = self.y - 1
            self.r=0

        elif pyxel.btnp(pyxel.KEY_DOWN,1,2):
            self.y = self.y + 1
            self.r=180
    
    def tir (self):
        if self.feu==False:
            if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT,1,10) :
                self.feu = True
                if self.r==0 or self.r==180:
                    if self.r==0:
                        self.dirx = -5
                    elif self.r==180:
                        self.dirx = 5
                    self.xc = self.x + 5
                    self.yc = self.y + 8
                elif self.r==90 or self.r==270:
                    if self.r==90:
                        self.diry = -5
                    elif self.r==270:
                        self.diry = 5
                    self.xc = self.x + 8
                    self.yc = self.y + 5
                    self.dtir =0
                self.a = 0

            elif pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT,1,10) :
                self.feu = True
                if self.r==0 or self.r==180:
                    if self.r==0:
                        self.dirx = 5
                    elif self.r==180:
                        self.dirx = -5
                    self.xc = self.x + 5
                    self.yc = self.y + 8
                    self.dtir =1
                elif self.r==90 or self.r==270:
                    if self.r==90:
                        self.diry = 5
                    elif self.r==270:
                        self.diry = -5
                    self.xc = self.x + 8
                    self.yc = self.y + 5
                    self.dtir =0
                self.a = 0

        elif self.feu==True:
            if self.a != 30:
                self.a += 1
                if self.a%2==0:
                    if self.dtir ==1:
                        self.xc = self.xc + self.dirx
                    else:
                        self.yc = self.yc + self.diry
            else:
                self.feu = False
                self.a = 0
                self.anim=True
                

main()