x=70
y=0

def setup():
    size(300,300)
    background(0)
def draw():
    fill(255)
    global x,y
    ellipseMode(CENTER)
    ellipse(150,150,x,x)  
    if mousePressed:
        scale(x)
        x = x + 1
        y = y + 1
        fill(y,0,0)
    else:
        if x>=300:
            x = 0
            background(0)
  
