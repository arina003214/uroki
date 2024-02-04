def setup():
    background(100,255,100)
    size(400,400)
def draw():
    rectMode(CENTER)
    
    if mousePressed: # если нажата
        background(100,100,255)
    else: # иначе(если не нажата)
        background(255,100,100) 
    rect(200,200,100,100)    
    if mousePressed:
        fill(0)
    else:
        fill(255)   
    if mousePressed:
        stroke(255)
    else:
        stroke(100,255,100)           
  
