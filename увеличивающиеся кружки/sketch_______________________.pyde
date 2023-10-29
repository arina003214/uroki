x=0
def setup():
    size(600,600)
    frameRate(20)
    background(255,100,100)
def draw():
    stroke(random(255),random(255),random(255))
    fill(random(255),random(255),random(255))
    global x
    x=x+1
    scale(x)
    translate(5,10)
    ellipse(x,x,10,10)
    
   
