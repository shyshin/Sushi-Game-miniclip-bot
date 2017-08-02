import win32con,win32api
import time as time
from PIL import ImageGrab as Image
from PIL import ImageOps
import numpy as np
import os

foodavail={
        'shrimp':5,
        'rice':10,
        'nori':10,
        'fish':10,
        'salmon':5,
        'unagi':5
}
sushitype={
        'gun':1770,
        'cal':2100,
        'oni':1843
}

class go():
        seat1=5514
        seat2=4792
        seat3=9335
        seat4=9254
        seat5=4948
        seat6=7038
        def __init__(self):
                self.x_pad=189
                self.y_pad=197
#----------------------------------
                self.fish=(86,430)
                self.rice=(97,373)
                self.nori=(25,430)
                self.salmon=(30,491)
                self.unagi=(80,499)
                self.shrimp=(38,389)
#----------------------------------
                self.p1=(85,254)
                self.p2=(180,260)
                self.p3=(273,252)
                self.p4=(378,253)
                self.p5=(493,256)
                self.p6=(569,256)
#----------------------------------
                self.free=(503,347)
                self.top=(512,315)
                self.orice=(536,338)
                self.ofish=(561,320)
                self.onori=(474,321)
                self.osalmon=(496,372)
                self.ounagi=(581,278)
                self.oshrimp=(489,289)
                self.slate=(189,422)
                self.phone=(596,397)
                self.exit=(595,386)
        def left_down(self):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(.1)
                print 'left down'
        def left_up(self):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                time.sleep(.1)
                print 'left release'
        def leftClick(self):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
                time.sleep(.1)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
                print "Click."
        def mousePos(self,cord):
                c1=cord[0]
                c2=cord[1]
                win32api.SetCursorPos((self.x_pad+c1,self.y_pad+c2))
        def get_cords(self):
		x,y= win32api.GetCursorPos()
                x=x-self.x_pad
		y=y-self.y_pad
		return x,y
	def screengrab(self):
                box=(self.x_pad,self.y_pad,self.x_pad+638,self.y_pad+480)
                im= Image.grab(box)
                return im
	def start_game(self):
                self.mousePos((324,257))
		self.leftClick()
                time.sleep(.1)
		
		self.mousePos((311,424))
		self.leftClick()
		time.sleep(.1)
                
		self.mousePos((564,492))
		self.leftClick()
		time.sleep(.1)
		
		self.mousePos((339,426))
		self.leftClick()
                time.sleep(.1)
        def order(self):
                self.mousePos(self.phone)
                self.leftClick()
                time.sleep(0.1)

                self.mousePos(self.orice)
                self.leftClick()
                time.sleep(.1)
                self.leftClick()

                self.mousePos(self.free)
                self.leftClick()
                a=time.time()
                return a
        def clear_tables(self):
                self.mousePos(self.p1)
                self.leftClick()
                self.mousePos(self.p2)
                self.leftClick()
                self.mousePos(self.p3)
                self.leftClick()
                self.mousePos(self.p4)
                self.leftClick()
                self.mousePos(self.p5)
                self.leftClick()
                self.mousePos(self.p6)
                self.leftClick()
                
                time.sleep(1.5)
        def foldslate(self):
                self.mousePos(self.slate)
                self.leftClick()
                time.sleep(.1)
        def make_food(self,food):
                if food=="oni":
                        print 'Onigiri'
                        foodavail['rice']-= 2
                        foodavail['nori']-= 1
                        self.mousePos(self.rice)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.nori)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.rice)
                        self.leftClick()
                        time.sleep(.1)
                        self.foldslate()
                        
                elif food=='cal':
                        print 'california roll'
                        foodavail['rice']-= 1
                        foodavail['nori']-= 1
                        foodavail['fish']-= 1
                        self.mousePos(self.rice)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.nori)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.fish)
                        self.leftClick()
                        time.sleep(.1)
                        self.foldslate()

                elif food=='gun':
                        print 'gunkan roll'
                        foodavail['rice']-= 1
                        foodavail['nori']-= 1
                        foodavail['fish']-= 2
                        self.mousePos(self.rice)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.nori)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.fish)
                        self.leftClick()
                        time.sleep(.05)
                        self.mousePos(self.fish)
                        self.leftClick()
                        time.sleep(.1)
                        self.foldslate()
        def buy_food(self,food):
                self.mousePos(self.phone)
                time.sleep(.1)
                self.leftClick()
                if food == "rice":
                        self.mousePos(self.orice)
                        time.sleep(0.1)
                        self.leftClick()
                        s= self.screengrab()
                        if s.getpixel(self.orice) !=(127,127,127):
                                print "rice is avail"
                                self.mousePos(self.orice)
                                self.leftClick()
                                time.sleep(.1)
                                self.mousePos(self.free)
                                self.leftClick()
                                self.leftClick()
                                foodavail['rice']+= 10
                                time.sleep(6.55)
                        else:
                                print 'rice is not avail'
                                self.mousePos(self.exit)
                                self.leftClick()
                                time.sleep(1)
                                self.buy_food(food)
                else:
                        self.mousePos(self.top)
                        self.leftClick()
                        time.sleep(.1)
                        s=self.screengrab()
                        if food == "nori":
                                print "nori is avail"
                                if s.getpixel(self.onori) == (218,246,255):
                                        self.mousePos(self.onori)
                                        self.leftClick()
                                        time.sleep(.1)
                                        self.mousePos(self.free)
                                        self.leftClick()
                                        foodavail['nori']+= 10
                                        time.sleep(6.55)
                                else:
                                        print 'nori is not avail'
                                        self.mousePos(self.exit)
                                        self.leftClick()
                                        time.sleep(1)
                                        self.buy_food(food)
                                 
                        elif food == "fish":
                                
                                if s.getpixel(self.ofish)==(218,246,255):
                                        print "fish is avail"
                                        self.mousePos(self.ofish)
                                        self.leftClick()
                                        time.sleep(.1)
                                        self.mousePos(self.free)

                                        self.leftClick()
                                        foodavail['fish']+= 10
                                        time.sleep(6.55)
                                else:
                                        print "fish is not avail"
                                        self.mousePos(self.exit)
                                        self.leftClick()
                                        time.sleep(1)
                                        self.buy_food(food)
                        elif food == "salmon":
                                if s.getpixel(self.osalmon)==(218,246,255):
                                        print "salmon is avail"
                                        self.mousePos(self.osalmon)
                                        self.leftClick()
                                        time.sleep(.1)
                                        self.mousePos(self.free)
                                        self.leftClick()
                                        foodavail['salmon']+= 5
                                        time.sleep(6.55)
                                else:
                                        print "salmon is not avail"
                                        self.mousePos(self.exit)
                                        self.leftClick()
                                        time.sleep(1)
                                        self.buy_food(food)
                        elif food == "unagi":
                                if s.getpixel(self.ounagi)==(189,98,16):
                                        print "unagi is avail"
                                        self.mousePos(self.ounagi)
                                        self.leftClick()
                                        time.sleep(.1)
                                        self.mousePos(self.free)
                                        self.leftClick()
                                        foodavail['unagi']+= 5
                                        time.sleep(6.55)
                                else:
                                        print "unagi is not avail"
                                        self.mousePos(self.exit)
                                        self.leftClick()
                                        time.sleep(1)
                                        self.buy_food(food)
                        elif food == "shrimp":
                                if s.getpixel(self.shrimp)==(255,255,255):
                                        print "shrimp is avail"
                                        self.mousePos(self.oshrimp)
                                        self.leftClick()
                                        time.sleep(.1)
                                        self.mousePos(self.free)
                                        self.leftClick()
                                        foodavail['rice']+= 10
                                        time.sleep(6.55)
                                else:
                                        print "shrimp is not avail"
                                        self.mousePos(self.exit)
                                        self.leftClick()
                                        time.sleep(1)
                                        self.buy_food(food)
        def check_food(self):
                for i,j in foodavail.items():
                        if i == 'fish' or i== 'rice' or i== 'nori':
                                if j <=3:
                                        print i + 'is low and needs to be replenished'
                                        self.buy_food(i)

        def grab(self):
                box=(self.x_pad+1,self.y_pad+1,self.x_pad+638,self.y_pad+480)
                im= ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
                im.save(os.getcwd() + '\\seat_one_'+str(int(time.time())))
                print a
                return a

        def seat_one(self):
                box=(self.x_pad+24,self.y_pad+112,self.x_pad+24+63,self.y_pad+122)
                im = ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
             #   im.save(os.getcwd() + '\\seat_one_'+str(int(time.time()))+'.png','PNG')
                print "seat one "+ str(a)
                return a
        def seat_two(self):
                box=(self.x_pad+125,self.y_pad+112,self.x_pad+125+63,self.y_pad+122)
                im= ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
              #  im.save(os.getcwd() + '\\seat_two_'+str(int(time.time()))+'.png','PNG')
                print "seat two "+ str(a)
                return a
        def seat_third(self):
                box= (self.x_pad+226,self.y_pad+112,self.x_pad+226+63,self.y_pad+122)
                im = ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
               # im.save(os.getcwd() + '\\seat_third_'+str(int(time.time()))+'.png','PNG')
                print "seat third "+ str(a)
                return a
        def seat_four(self):
                box= (self.x_pad+327,self.y_pad+112,self.x_pad+327+63,self.y_pad+122)
                im = ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
                #im.save(os.getcwd() + '\\seat_four_'+str(int(time.time()))+'.png','PNG')
                print "seat four "+ str(a)
                return a
        def seat_five(self):
                box= (self.x_pad+428,self.y_pad+112,self.x_pad+428+63,self.y_pad+122)
                im = ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
                #im.save(os.getcwd() + '\\seat_five_'+str(int(time.time()))+'.png','PNG')
                print "seat five "+ str(a)
                return a
        def seat_six(self):
                box= (self.x_pad+529,self.y_pad+112,self.x_pad+529+63,self.y_pad+122)
                im = ImageOps.grayscale(Image.grab(box))
                a= np.array(im.getcolors())
                a= a.sum()
                #im.save(os.getcwd() + '\\seat_six_'+str(int(time.time()))+'.png','PNG')
                print "seat six "+ str(a)
                return a
        def get_seats(self):
                self.seat_one()
                self.seat_two()
                self.seat_third()
                self.seat_four()
                self.seat_five()
                self.seat_six()
        def check_bubs(self):
                self.check_food()
                s1= self.seat_one()
                if s1 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s1:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 1 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s1
                else:
                        print "table 1 is occupied"
                self.clear_tables()
                self.check_food()

                s2= self.seat_two()
                if s2 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s2:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 2 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s2
                else:
                        print  "table 2 is occupied"
                self.check_food()
                s3=self.seat_third()
                if s3 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s3:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 3 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s3
                else:
                        print  "table 3 is occupied"
                self.check_food()
                s4=self.seat_four()
                if s4 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s4:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 4 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s4
                else:
                        print  "table 4 is occupied"
                self.check_food()
                s5=self.seat_five()
                if s5 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s5:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 5 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s5
                else:
                        print  "table 5 is occupied"
                self.check_food()
                s6=self.seat_six()
                if s6 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s6:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 6 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s6
                else:
                        print  "table 6 is occupied"
                self.clear_tables()
        def small_check(self):
                self.check_food()
                s1= self.seat_one()
                if s1 != self.seat1:
                        c=0
                        for i,j in sushitype.items():
                                if j == s1:
                                        c=1
                                        k= i
                        if c == 1:
                                print 'table 1 is occupied and needs %s' %k
                                self.make_food(k)
                        else:
                                print 'sushi not found\n sushitype= %i' %s1
                else:
                        print "table 1 is occupied"

def main():
        a= go()
        a.start_game()
        t= time.time()
        b= time.time()
        while b-t<=188.65:
                a.check_bubs()
                b=time.time()
if __name__ == "__main__":
        main()




















