def setup():
    size(400,400)
    background(90,40,100)
def draw():
    if mousePressed and (mouseButton == LEFT):
        line(random(400),random(400),random(400),random(400))
        stroke(random(255),random(255),random(255))
        strokeWeight(random(10))
    elif mousePressed and (mouseButton == RIGHT):
        background(90,40,100)
            
            
            
