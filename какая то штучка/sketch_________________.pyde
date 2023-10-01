x=0

def setup():
    size(600,600)

def draw():
    global x
    x = x + 1
    stroke(x, x, x)
    fill(x, x, x)       
    ellipse(x,x,10,10)
