x=0

ex="r" 
def setup():
    size(600,600)
def draw():
    global x,ex
    fill(106,67,17)
       
    push()
    ellipseMode(CORNER)
    translate(220,260)
    rotate(radians(45))
    ellipse(0,0,60,120)
    pop()
    push()
    ellipseMode(CORNER)
    translate(380,350)
    rotate(radians(-130))
    ellipse(x,x,60,120) #правая лапа(огрызок от руки)
    pop()
    ellipse(230,470,70,70) #левая лапа(ноги)
    ellipse(360,470,70,70) #правая лапа(ноги)
    ellipse(300,350,200,250) #туловище
    fill(201,136,51)
    ellipse(300,340,130,160) #пузико
    ellipse(380,140,90,90) #правое ухо
    ellipse(220,140,90,90) #левое ухо
    fill(106,67,17)  
    ellipse(300,200,160,160) #голова
    push()
    strokeWeight(35)
    point(260,190)
    translate(75,0)
    point(260,190)
    strokeWeight(15)
    stroke(255)
    point(255,185)
    translate(-75,0)
    point(255,185)
    pop()
    if ex == "r":
        x = x + 1
    if ex == "l":
        x = x - 1
    if x >=170:
        ex = "l"
    if x <= 150:
        ex = "r"    
      
            
    
