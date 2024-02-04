x=0
mode="вправо"
def setup():
    size(400,400)
    frameRate(20)

def draw():
    global x,mode
    noStroke()
    background(255)
    fill(100,255,100)
    ellipse(x,x,100,100)

    if mode == "вправо":
       x = x + 20
    if mode == "влево":   
        x = x - 20
    if mousePressed and (mouseButton == LEFT):
        mode = "влево"
    if mousePressed and (mouseButton == RIGHT):        
        mode = "вправо"
    print(x)    
 
