x=0
def setup():
    background(0)
    size(600,400)
    frameRate(20)
def draw():
    global x 
    x=x+1
    stroke(x,0,0)
    fill(x,0,0)
    ellipse(200,100,100,100)
    stroke(0,x,0)
    fill(0,x,0)
    ellipse(200,210,100,100)
    stroke(0,0,x)
    fill(0,0,x)
    ellipse(200,320,100,100)
    stroke(x,x,0)
    fill(x,x,0)
    ellipse(350,100,100,100)
    stroke(0,x,x)
    fill(0,x,x)
    ellipse(350,210,100,100)
    stroke(x,0,x)
    fill(x,0,x)
    ellipse(350,320,100,100)
