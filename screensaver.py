"""
this is a Screensaver, which shows randomly generated balls.
taken fom the book: Tkinter GUI Application Development Hotshot
with a slight modification
Dhiraj
""" 


from tkinter import *
from random import randint, sample

# A class to generate balls with random attributes

class RandomBall:
    
    def __init__(self, canvas, scrnwidth, scrnheight):
        self.canvas = canvas
        self.xpos = randint(10,int(scrnwidth))
        self.ypos = randint(10,int(scrnheight))
        self.xvelocity = randint(6,12)
        self.yvelocity = randint(6,12)
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        self.radius = randint(40,70)
        r = lambda: randint(0,255)### create a random number from 0-255
        self.color = '#%02x%02x%02x' % (r(),r(),r())
        self.chars = 'abcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*|'
        

    def create_ball(self):
        x1 = self.xpos-self.radius
        y1 = self.ypos-self.radius
        x2 = self.xpos+self.radius
        y2 = self.ypos+self.radius
        #self.itm1 = self.canvas.create_text(x1,y1, text = "B\nA\nL\nL", #text=sample(self.chars,20),
        #						 fill='green', font=('Calibri',15))
        #self.itm2 = self.canvas.create_text(self.scrnwidth/2, 0,
        #					text="M\nA\nT\nR\nI\nX", font=('Courier',18), fill = 'green')
        self.itm = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color,outline=self.color)
        #self.itm3 = self.canvas.create_oval(x1,y1,x1+25,y1+15, fill=self.color, outline='white')
        


    def move_ball(self):
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        if self.ypos >= self.scrnheight - self.radius:
           self.yvelocity = -self.yvelocity # change direction

        if self.ypos <= self.radius :
            self.yvelocity = abs(self.yvelocity)

        if self.xpos >= self.scrnwidth- self.radius or self.xpos <= self.radius:
            self.xvelocity = -self.xvelocity

        self.canvas.move(self.itm, self.xvelocity, self.yvelocity)
        #self.canvas.move(self.itm1, self.xvelocity, self.yvelocity)
        #self.canvas.move(self.itm2,0.0,9.0)



# Now our Screen Saver Program
class ScreenSaver:
    balls = []
    
    def __init__(self, num_balls):
        self.root = Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (w, h))
        self.root.attributes('-alpha', 0.99)

        self.root.bind('<Any-KeyPress>', quit)
        self.root.bind('<Any-Button>', quit)
        self.root.bind('<Motion>', quit)
        self.canvas = Canvas(self.root, width=w, height=h, background = 'black')
        self.canvas.pack()
        for i in range(num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(20, self.run_screen_saver) #call the move_ball method after 20 ms

    def quit(self, event):
        self.root.destroy()



if __name__ == "__main__":
    ScreenSaver(25)  ##25 is the number of balls
    
