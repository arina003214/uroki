x=0
y=0
e=0
def setup():
    background(55,120,35)
    size(600,600)
    global x,e,y 
    x=loadImage("frog.png")
def draw(): 
    global x,e,y 
    image(x,e,y,200,200) 
    fill(30,60,20)
    noStroke()
    rect(550,530,50,50)
    rect(495,550,50,50)
    rect(440,530,50,50)
    rect(495,495,50,50)
    fill(150,240,130)
    textSize(30)  
    text("<",450,564)
    text(">",570,564)
    text("^",510,530)
    textSize(20) 
    text("\/",510,580)
def mouseClicked():
    global x,e,y
    background(55,120,35)
    if mouseX>550 and mouseX<600 and mouseY>530 and mouseY<580: 
        e=e+15
    if mouseX>495 and mouseX<545 and mouseY>550 and mouseY<600:
        y=y+15 
    if mouseX>440 and mouseX<490 and mouseY>530 and mouseY<580:
        e=e-15
    if mouseX>495 and mouseX<545 and mouseY>495 and mouseY<545:
        y=y-15     
      
        
