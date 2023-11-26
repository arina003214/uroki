x=0
def setup():
    size(600,600)
   
def draw():   
    global x
    x=x+1
    translate(300,300)
    fill(x)
    rotate(x)
    ellipse(x,x,100,100)

    
