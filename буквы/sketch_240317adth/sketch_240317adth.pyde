x=0
def setup():
    size(150,150)
    background(255)
def draw():
    if keyPressed:
        if key == 'h' or key == 'H':
            text(key,35,75)
            fill(40,220,160)
        elif key == 'e' or key == 'E':
            text('e',55,75)
            fill(250,120,10)
        elif key == 'l' or key == 'L':
            text('ll',75,75)
            fill(10,250,10)
        elif key == 'O' or key == 'o':
           text('o',95,75)
           fill(200,10,250)
        elif key == '1':
            text('!',115,75)
            fill(255,0,0)
        else:
            if key == 'z' or key == 'Z':
                background(255)
            
    textSize(30)
