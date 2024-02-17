def setup():
    size(400,400)
    background(50,240,190)

def draw(): 
    strokeWeight(5)
    stroke(175,100,200)
    line(mouseX,mouseY,pmouseX,pmouseY) 
    if mousePressed and (mouseButton == RIGHT):
        background(50,240,190)
       
