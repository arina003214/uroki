feb=0
star=0
x=700
y=600
r=255
g=41
b=53
h=0

def setup():
    global feb
    size(1920,1080)
    feb=loadImage("images1.jpg")
def draw():
    global feb,star,x,y 
    star = star + 30   
    image(feb,0,0,1920,1080)
    
    push()
    translate(700,600)
    rotate(radians(star))
    stroke(r,h,h)
    strokeWeight(5)
    fill(r,h,h)
    triangle(700-700,500-600,760-700,600-600,640-700,600-600)
    triangle(760-700,700-600,750-700,600-600,640-700,600-600)
    triangle(640-700,700-600,650-700,600-600,740-700,600-600)
    triangle(820-700,600-600,700-700,640-600,700-700,560-600)
    triangle(580-700,600-600,700-700,640-600,700-700,560-600)
    pop()
    
    push()
    translate(1220,y)
    rotate(radians(star))
    stroke(r,h,h)
    strokeWeight(5)
    fill(r,h,h)
    triangle(700-x,500-y,760-x,600-y,640-x,600-y)
    triangle(760-x,700-y,750-x,600-y,640-x,600-y)
    triangle(640-x,700-y,650-x,600-y,740-x,600-y)
    triangle(820-x,600-y,700-x,640-y,700-x,560-y)
    triangle(580-x,600-y,700-x,640-y,700-x,560-y)
    pop()
    if mousePressed and (mouseButton == LEFT):
        push()
        translate(700,600)
        rotate(radians(star))
        stroke(h,b,r)
        strokeWeight(5)
        fill(h,b,r)
        triangle(700-700,500-600,760-700,600-600,640-700,600-600)
        triangle(760-700,700-600,750-700,600-600,640-700,600-600)
        triangle(640-700,700-600,650-700,600-600,740-700,600-600)
        triangle(820-700,600-600,700-700,640-600,700-700,560-600)
        triangle(580-700,600-600,700-700,640-600,700-700,560-600)
        pop()
        
        push()
        translate(1220,y)
        rotate(radians(star))
        stroke(h,b,r)
        strokeWeight(5)
        fill(h,b,r)
        triangle(700-x,500-y,760-x,600-y,640-x,600-y)
        triangle(760-x,700-y,750-x,600-y,640-x,600-y)
        triangle(640-x,700-y,650-x,600-y,740-x,600-y)
        triangle(820-x,600-y,700-x,640-y,700-x,560-y)
        triangle(580-x,600-y,700-x,640-y,700-x,560-y)
        pop()
    elif mousePressed and (mouseButton == RIGHT):
        push()
        translate(700,600)
        rotate(radians(star))
        stroke(g,r,h)
        strokeWeight(5)
        fill(g,r,h)
        triangle(700-700,500-600,760-700,600-600,640-700,600-600)
        triangle(760-700,700-600,750-700,600-600,640-700,600-600)
        triangle(640-700,700-600,650-700,600-600,740-700,600-600)
        triangle(820-700,600-600,700-700,640-600,700-700,560-600)
        triangle(580-700,600-600,700-700,640-600,700-700,560-600)
        pop()
        
        push()
        translate(1220,y)
        rotate(radians(star))
        stroke(g,r,h)
        strokeWeight(5)
        fill(g,r,h)
        triangle(700-x,500-y,760-x,600-y,640-x,600-y)
        triangle(760-x,700-y,750-x,600-y,640-x,600-y)
        triangle(640-x,700-y,650-x,600-y,740-x,600-y)
        triangle(820-x,600-y,700-x,640-y,700-x,560-y)
        triangle(580-x,600-y,700-x,640-y,700-x,560-y)
        pop()
    elif mousePressed and (mouseButton == CENTER):
        push()
        translate(700,600)
        rotate(radians(star))
        stroke(r,r,h)
        strokeWeight(5)
        fill(r,r,h)
        triangle(700-700,500-600,760-700,600-600,640-700,600-600)
        triangle(760-700,700-600,750-700,600-600,640-700,600-600)
        triangle(640-700,700-600,650-700,600-600,740-700,600-600)
        triangle(820-700,600-600,700-700,640-600,700-700,560-600)
        triangle(580-700,600-600,700-700,640-600,700-700,560-600)
        pop()
        
        push()
        translate(1220,y)
        rotate(radians(star))
        stroke(r,r,h)
        strokeWeight(5)
        fill(r,r,h)
        triangle(700-x,500-y,760-x,600-y,640-x,600-y)
        triangle(760-x,700-y,750-x,600-y,640-x,600-y)
        triangle(640-x,700-y,650-x,600-y,740-x,600-y)
        triangle(820-x,600-y,700-x,640-y,700-x,560-y)
        triangle(580-x,600-y,700-x,640-y,700-x,560-y)
        pop()
        
        
