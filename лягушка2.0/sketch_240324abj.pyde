x=0
y=300
e=300
def setup():
    background(55,120,35)
    size(600,600)
    global x,e,y 
    x=loadImage("frog.png")
def draw():
    imageMode(CENTER)
    background(55,120,35)
    global x,e,y
    translate(e,y)
    
    image(x,0,0,200,200) 
    fill(30,60,20)
    noStroke()
    

    if keyPressed:
        
        background(55,120,35)
        if keyCode ==  UP:
            y=y-5
            rotate(radians(270))
            image(x,0,0,200,200)
              
        elif keyCode == DOWN:
            y=y+5
            rotate(radians(90))
            image(x,0,0,200,200) 
        elif keyCode == LEFT:
            e=e-5
            rotate(radians(180))
            image(x,0,0,200,200)     
        elif keyCode == RIGHT:
            e=e+5
            rotate(radians(0)) 
            image(x,0,0,200,200)
            

             
