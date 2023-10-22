x=160
def setup():
     size(1000,1000)
     background(255)
def draw():
    global x 
    x=x+1
    translate(0,150)
    stroke(242,209,142)
    fill(242,209,142)
    ellipse(70,180,150,300) 
    strokeWeight(50)
    stroke(255)
    point(130,130)
    strokeWeight(40)
    stroke(0)
    point(135,130)
    fill(0)   
    rect(50,-20,50,60)
    rect(20,50,120,10) 
    stroke(242,209,142)
    point(x,200)
    strokeWeight(25)
    stroke(0,255,0)
    point(x,200) 
