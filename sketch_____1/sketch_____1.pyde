x=100
def setup():
    size(600,400)
    colorMode(HSB,360,100,100)
    frameRate(20)
def draw():
    global x 
    x=x-1
    stroke(27,53,77)
    fill(27,53,77)
    ellipse(300,200,250,300)
    fill(240,100,x)
    ellipse(240,150,70,50)  
    fill(240,x,100) 
    ellipse(350,150,70,50)
