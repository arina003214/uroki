march=0
x=0
woman=0
y=0
mode=1
def setup():
    global march,woman,flower
    background(250,170,245)
    size(600,600)
    march = loadImage("ol.png")
    woman = loadImage("qaz.png")
    flower = loadImage("wer.png")
def draw():
    global march,x,woman,y,flower,mode
    if mode == 1:
        
        image(march,70,0,450,600)
        fill(220,100,240)
        noStroke()
        ellipse(300,300,130,100)
        fill(240,170,230)
        textSize(40)
        text("open",250,310)
    elif mode == 2: 
        background(250,210,140)
        push()
        translate(290,500)
        rotate(radians(220))
        image(woman,0,0,300,400)
        pop()
        textSize(60)
        fill(230,80,160)
        text(u"С 8 марта!!",150,100)
        rect(490,540,100,50)
        fill(150,210,210)
        textSize(25)
        text("zamena",490,570)
    elif mode == 3: 
        background(220,180,240)
        push()
        translate(290,500)
        rotate(radians(220))
        image(flower,0,0,300,400)
        pop()
        
        textSize(60)
        fill(230,80,160)
        text(u"С 8 марта!!",150,100)
        
def mouseClicked():
    global x,mode
    xDif = 300 - mouseX
    yDif = 300 - mouseY
    if mode == 1 and sqrt(xDif*xDif+yDif*yDif)<65:
        mode = 2
        
    elif mode == 2 and mouseX>490 and mouseX<590 and mouseY>540 and mouseY<590:
        mode = 3
           
        
     
        
      
    
