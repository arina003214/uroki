x=10
y=20
xp=90
yp=90
stena=0
frog=0
klad=0

def collideRectRect (x, y, w, h, x2, y2, w2, h2):
  # работает правильно, даже если rectMode стоит CENTER
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False


def setup():
    size(600,400)
    global stena,frog,klad
    frog=loadImage('lagyshka.png')
    stena=loadImage('stena.png')
    klad=loadImage('klad.png')
    background(70,220,240)
def draw():
    background(70,220,240)
    global stena,frog,klad,x,y,xp,yp
    image(stena,100,0,50,300)
    image(stena,250,100,50,300)
    image(stena,400,0,50,300)
    image(klad,470,0,120,120)
    image(frog,x,y,xp,yp)

        
     #Столкновение персонажа со стенами
    rect1_collide = collideRectRect(100, 0, 50, 300,   x, y, xp,yp) #прямоугольник1
    rect2_collide = collideRectRect(250, 100, 50, 300,   x, y, xp,yp) #прямоугольник2
    rect3_collide = collideRectRect(400, 0, 50, 300,   x, y,xp,yp) #прямоугольник3
    #Столкновение персонажа с краями
    rect_edges_collide =  x < 0 or 600 < x or y < 0 or 400 < y   
    
# Движение персонажа
    if keyPressed == True:
        if keyCode == RIGHT:
            x = x + 3
            collide = rect1_collide or rect2_collide or rect3_collide or rect_edges_collide
            print(collide)
            if collide == True:
                x = x - 10 #если касается, отходит обратно
            collide=False
        elif keyCode == LEFT:
            x = x - 3
            collide = rect1_collide or rect2_collide or rect3_collide or rect_edges_collide
            print(collide)
            if collide == True:
                x = x + 10 #если касается, отходит обратно
            collide=False
        elif keyCode == UP:
            y = y - 3
            collide = rect1_collide or rect2_collide or rect3_collide or rect_edges_collide
            print(collide)
            if collide == True:
                y = y + 10 #если касается, отходит обратно
            collide=False
        elif keyCode == DOWN:
            y = y + 3
            collide = rect1_collide or rect2_collide or rect3_collide or rect_edges_collide
            print(collide)
            if collide == True:
                y = y - 10 #если касается, отходит обратно
            collide=False       
    if collideRectRect(470,0,120,120,x,y,xp,yp): 
        background(30,250,15)
        textSize(50)
        text('You are winner!!!',100,150,450,100)       


           
