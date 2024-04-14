q=200
w=0
c=0
mode='вправо'
def setup():
    size(400,400)

def draw():
    global q,w,mode,c
    c = c + 5
    noStroke()
    background(255)
    fill(c)
    ellipse(w,q,100,100)
    if c == 255:
        c=0
    
    if mode == 'вправо':
        w = w + 10
    if mode == "влево":   
        w = w - 10
    if w >= 400:
        mode = "влево"
    if w <= 0:        
        mode = "вправо" 
    if keyPressed:
        if keyCode == UP:
            q = q - 5
        elif keyCode == DOWN:
            q = q + 5 
       
