x=0
y=0
def setup():
    size(300,300)
    background(0)
def draw():
    global x,y
    ellipseMode(CENTER)
    ellipse(x,y,70,70)
    fill(255,100,100)
    noStroke()
def mouseClicked():
    global x,y
    xDif = x - mouseX
    yDif = y - mouseY  
    if sqrt(xDif*xDif + yDif*yDif)<35:
        background(0) 
        x=random(300)
        y=random(300)
           
