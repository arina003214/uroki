x=0
def setup(): 
    size(400,400)
def draw():
    background(255)
    global x
    x = x + 1
    noStroke()
    fill(100,255,100)
    ellipse(200,200,x,x)
    print(x)
    if x >= 600:
        x=0   
