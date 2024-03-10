x=0
r=255
def setup():
    size(300,300)
    background(240,200,150)
def draw():
    rectMode(CENTER) 
    rect(150,150,100,60)
def mouseClicked():
    if mouseX>150 and mouseX<250 and mouseY>150 and mouseY<210:
        noStroke()
        fill(random(255),random(255),random(255))
        noStroke()
        
