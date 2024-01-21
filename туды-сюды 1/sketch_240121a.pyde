x=0 
mode= "вверх"
def setup():
    size(400,400)
def draw():
    global x,mode
    noStroke()
    background(255)
    fill(255,100,100)
    ellipse(200,x,100,100) 
    if mode == "вверх":
        x = x + 20 
    if mode == "вниз":
        x = x - 20   
    if x >= 400:
        mode= "вниз"
    if x <= 0: 
        mode = "вверх"         
