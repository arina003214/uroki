x = 0 
def setup():
    size(400,400)
def draw():
    global x 
    x = x + 1
    stroke(x,x,x)
    fill(x,x,x)
    ellipse(200,200,100,100)
    if x >= 255:
        x=0    
