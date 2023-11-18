x=0

def setup():
    size(600,400)
    background(100,100,255)
    frameRate(10)
def draw(): 
  
    global x
    x=x+1
    scale(x)
    ellipse(x,x,15,10)
    
