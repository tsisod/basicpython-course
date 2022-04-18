import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า

def rectangle():
    '''ฟังชั่นนี้เอาไว้วาดรูปสี่เหลี่ยม '''
    for i in range(4):
        tao.forward(100)
        tao.left(90)
        
def go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    
def donut():
    for i in range(10):
        tao.circle(50)
        tao.left(36)
        tao.circle(50)
        tao.left(37)
        tao.circle(50)
        tao.left(38)
        tao.circle(50)
        tao.left(39)
        tao.circle(50)
        tao.left(40)
        tao.circle(50)

tao.clear()
donut()






		 
