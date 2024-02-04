x=0
def setup():
    size(400,400)
    background(0,4,44)
def draw():
    global x 
    x = x + 1 
    stroke(255,255,0)
    strokeWeight(random(5))
    point(random(400),random(400))
    if mousePressed:
        background(0,4,44)
   
    
        
