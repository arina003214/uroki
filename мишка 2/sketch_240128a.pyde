x=0
def setup():
    size(600,600)
def draw():
    global x 
    x = x + 1
    push()
    ellipseMode(CORNER)
    translate(200,260)
    rotate(radians(30))
    ellipse(0,0,60,120) #левкая лапа(рука)
    pop()
    push()
    ellipseMode(CORNER)
    translate(340,350)
    rotate(radians(-90))
    ellipse(0,0,60,120) #правая лапа(огрызок от руки)
    pop()
    ellipse(230,470,70,70) #левая лапа(ноги)
    ellipse(360,470,70,70) #правая лапа(ноги)
    ellipse(300,350,200,250) #туловище
    ellipse(300,340,130,160) #пузико
    ellipse(380,140,90,90) #правое ухо
    ellipse(220,140,90,90) #левое ухо
    ellipse(300,200,160,160) #голова
    ellipse()
    
  
