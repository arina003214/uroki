# Три круга меняют цвета в зависимости от кнопки мыши
def setup():
    size(300,300)
    
def draw():
    background(100)
    strokeWeight(5)
    
    if mousePressed and (mouseButton == LEFT):
        push()
        fill(205,20,195)
        stroke(0,35,255)
        ellipse(150,50,50,50)
        pop()
        ellipse(150,100,50,50)
        ellipse(150,150,50,50)
    elif mousePressed and (mouseButton == RIGHT):
        push()
        fill(205,20,195)
        stroke(0,35,255)
        ellipse(150,150,50,50)
        pop()
        ellipse(150,50,50,50)
        ellipse(150,100,50,50)
    elif mousePressed and (mouseButton == CENTER):
        push()
        fill(205,20,195)
        stroke(0,35,255)
        ellipse(150,100,50,50)
        pop()
        ellipse(150,50,50,50)
        ellipse(150,150,50,50)
    else:
        fill(255)
        ellipse(150,150,50,50)
        ellipse(150,100,50,50)
        ellipse(150,50,50,50)



        
    
