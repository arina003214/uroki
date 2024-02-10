x=0
ex="r"
def setup():
    size(400,400)
def draw():
    background(175,105,214)
    global x, ex
    strokeWeight(random(10))
    stroke(random(255),random(255),random(255))
    line(x,0,x,400)
    if ex == "r":
        x = x + 1
    if ex == "l":
        x = x - 1
    if x >= 400:
        ex = "l"
    if x <= 0:
        ex = "r"            
    
        
