import turtle
import random
import os

# https://realpython.com/beginners-guide-python-turtle/

images = ['alfa.png', 'beta.png','gamma.png', 'epsilon.png', 'lambda.png', 'fi.png', 'mi.png', 'ro.png', 'eta.png', 'xi.png', 'z.png', 'theta.png', 'tau.png', 'pi.png', 'psi.png']
i=0;


def drawCircle(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.circle(15)

def fxn(x, y):
    
    print("onClick"+str(x)+" "+str(y))
    i=random.randint(0,14);
    print(F" {i}");

    wn.bgpic(images[i])

    
    if (i==4):
        turtle.speed(5)
        turtle.forward(550)
        turtle.write('Congratulations!!!!!!!!')
        os.system('afplay fiesta.mp3')
        turtle.clear()
        init()
    
     
def init():
    turtle.speed(500)
    drawCircle(100, 40)
    drawCircle(150, 40)
    drawCircle(200, 40)
    drawCircle(250, 40)
    turtle.penup()
    turtle.goto(-300, 55)
    turtle.pendown()    
    turtle.dot(15)




init()
wn = turtle.Screen()
wn.bgpic(images[i])

wn.onclick(fxn)
wn.mainloop()



turtle.done()
