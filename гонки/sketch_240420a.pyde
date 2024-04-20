cx=50
rx=330
ry=100
rw=30
rh=200
cy=200
diameter=80

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
    background(255)
def draw():
    background(255)
    global cx,cy,rx,ry,rw,rh,diameter
    noStroke()
    fill(255,0,0)
    rect(0,0,400,100)
    rect(0,300,400,100)
    fill(0)
    rect(rx,ry,rw,rh)
    fill(40,140,210)
    ellipse(cx,cy,diameter,diameter)
    # кнопки
    fill(90,210,40)
    rect(100,320,90,50)
    rect(210,320,90,50)
    textSize(20)
    fill(0)
    text('forward',217,350)
    text('back',125,350)
    if collideRectCircle(rx,ry,rw,rh,cx,cy,diameter):
        background(77,255,3)
        noLoop()
        fill(0)
        textSize(40)
        text('Game completed!!',20,200)    
def mouseClicked():
    global cx 
    if mouseX>100 and mouseX<190 and mouseY>320 and mouseY<370:
        cx = cx - 10
    elif mouseX>210 and mouseX<300 and mouseY>320 and mouseY<370:
        cx = cx + 10    
        
