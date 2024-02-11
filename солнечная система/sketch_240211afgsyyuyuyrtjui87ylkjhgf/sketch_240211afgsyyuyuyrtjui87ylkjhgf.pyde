x=0 
y=0
k=0
q=0
e=0
t=0
def setup():
    size(600,600)
    background(10,10,40)
def draw():
    background(10,10,40)
    global x,y,k,q,e,t
    x = x + 1
    y = y + 5
    k = k + 2 
    q = q + 3
    e = e + 1 
    t = t + 0.9
    fill(10,10,40)
    stroke(100,100,100)
    strokeWeight(1)
    ellipse(300,300,650,650)
    ellipse(300,300,520,520)
    ellipse(300,300,390,390)
    ellipse(300,300,260,260) 
    ellipse(300,300,130,130)

    strokeWeight(60)
    stroke(200,200,50) 
    point(300,300)
    translate(300,300) 
    push()
    rotate(radians(x))
    strokeWeight(30)
    stroke(255,100,100)
    point(50,40)
    pop()
    push()
    rotate(radians(y))
    stroke(100,100,255)
    strokeWeight(25)
    point(-100,80)
    pop()
    
    push()
    rotate(radians(k))
    strokeWeight(40)
    stroke(100,255,100)
    translate(150,120)
    point(0,0)
    
    push()
    rotate(radians(t))
    strokeWeight(15)
    stroke(160,130,20)
    point(30,30)
    pop()
    
    pop()
    
    push()
    rotate(radians(q))
    strokeWeight(50)
    stroke(165,90,30)
    point(-200,160)
    pop()
    push()
    rotate(radians(e))
    strokeWeight(35)
    stroke(110,40,225)
    point(250,200)
    pop()
    
        
    
