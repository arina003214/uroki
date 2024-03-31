x=0
y=0
w=100
ex="r" #right
ey="d"
speed=1
ladder_x=110
ladder_y=385
ladder_width=90
ladder_height=15

def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
  #2d
  # временные переменные для установки краёв для тестирования
  # rectmode — CORNER, ellipseMode — CENTER, то есть оба по-умолчанию
  testX = cx
  testY = cy

  # which edge is closest?
  if cx < rx:
    testX = rx       # Левый край
  elif cx > rx+rw:
    testX = rx+rw     # правый край

  if cy < ry:
    testY = ry       # верхний край
  elif cy > ry+rh:
    testY = ry+rh   # нижний край

  # получить расстояние от ближайших краев с помощью processing функции dist()
  distance = dist(cx,cy,testX,testY) 

  # если расстояние меньше радиуса, столкновение!
  if distance <= diameter/2:
    return True
  else:
    return False

def setup():
    size(400,400)
    frameRate(200)
def draw():
    global x,ex,ey,y,w,speed,ladder_x,ladder_y,ladder_width, ladder_height
    noStroke()
    background(100,255,100)
    fill(100,100,255)
    push()
    translate(200,0)
    ellipse(x,y,w,w)
    pop()
    if ex == "r":
        x = x + speed 
    if ex == "l":
        x = x - speed
    if ey == "d":
        y = y + speed
    if ey == "b":
        y = y - speed

    print(x)
    print(ex)
    if x >= 400-200:
        ex = "l"
    if x <= 0-200:
        ex = "r"
    if y <= 0:
         ey ="d"
    rect(ladder_x,ladder_y,ladder_width, ladder_height)     
         
    
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            ladder_x = ladder_x - 3
        if keyCode == RIGHT:
            ladder_x = ladder_x + 3

    if y >= 400:
        if collideRectCircle(ladder_x, ladder_y, ladder_width, ladder_height,x,y,w):
            speed=random(1,3)           
        else:             
            noLoop()
            background(255,0,0)
            textSize(60)
            fill(0)
            text('Game over:(',30,200)
     
        
          

             
                      
