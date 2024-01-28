x=0
y=0
ex="r" #right
ey="d"
def setup():
    size(400,400)
    frameRate(200)
def draw():
    global x,ex,ey,y
    noStroke()
    background(100,255,100)
    fill(100,100,255)
    push()
    translate(200,0)
    ellipse(x,y,100,100)
    pop()
    if ex == "r":
        x = x + 1 
    if ex == "l":
        x = x - 1
    if ey == "d":
        y = y + 1
    if ey == "b":
        y = y - 1 
    
    print(x)
    print(ex)
    if x >= 400-200:
        ex = "l"
    if y >= 400:
        ey = "b"
    if x <= 0-200:
        ex = "r"
    if y <= 0:
         ey ="d"    
        
   
