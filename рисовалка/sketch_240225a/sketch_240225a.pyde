x = 0
r = 0
g = 0
b = 0
def setup():
    global r,g,b,x
    size(600,600)
    background(230,200,100)
def draw():
    global r,g,b,x
    push()
    strokeWeight(x)
    stroke(r,g,b)
    line(mouseX,mouseY,pmouseX,pmouseY)
    pop()
    push()
    fill(255,56,20)
    stroke(255,56,20)
    rect(500,10,99,50) 
    rect(500,70,99,50)
    rect(500,130,99,50)
    pop()   
    textSize(30)
    text("Delete",500,45)
    text("color",515,100)
    text("size",525,160)
            
def mouseClicked():
    global r,g,b,x
    if mouseX>500 and mouseX<599 and mouseY>10 and mouseY<60:
        background(230,200,100)
    if mouseX>500 and mouseX<599 and mouseY>70 and mouseY<120:
        r=random(255)
        g=random(255)
        b=random(255) 
    if mouseX>500 and mouseX<599 and mouseY>130 and mouseY<180:
        x=random(0,30)
    
