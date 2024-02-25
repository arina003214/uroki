x = 0
def setup():
    size(300,300)
def draw():
    global x 
    
    push()
    fill(30,100,255)
    noStroke()
    rect(80,100,150,100)
    pop() 
    textSize(60)
    text("click",90,170)
def mouseClicked():
    global x 
    if mouseX>80 and mouseX<230 and mouseY>100 and mouseY<200:
        print (x)
        x = x + 1
          
