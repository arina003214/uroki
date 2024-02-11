skr=0
def setup():
    background(0)
    global skr
    size(1920,1080)
    skr=loadImage("pic1.jpeg")
    
def draw():
    if mousePressed:
        global skr    
        image(skr,0,0,1920,1080)
    else:
        background(0)    
