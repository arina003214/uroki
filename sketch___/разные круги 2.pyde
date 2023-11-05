x=0
def setup():
    size(600,400)
    colorMode(HSB, 360, 100, 100)
def draw():
    global x
    x=x+1
    fill(x, 100, 100)
    ellipse(300,200,100,100)
    fill(100,x,100)
    ellipse(150,200,100,100)
    fill(100,100,x)
    ellipse(450,200,100,100)
        
