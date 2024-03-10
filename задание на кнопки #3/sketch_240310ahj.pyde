x=150 
y=150
def setup():
    size(300,300)
    background(255)
def draw():
    global x,y
    stroke(100,100,255)
    fill(100,100,255)
    ellipse(x,y,30,30)
    if mousePressed:
        background(255)
        ellipse(mouseX,mouseY,30,30) 
        x = mouseX
        y = mouseY
   
