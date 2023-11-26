x=0
y=5
def setup():
    size(600,600)
    background(100,100,245)   
def draw():
    global x,y
    y=y+5
    x=x+1
    translate(300,300)
    rotate(radians(x))
    strokeWeight(5)
    stroke(235,x,x)
    line(0,0,0,100)
