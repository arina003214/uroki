def collidePointCircle(x, y, cx, cy, d):
    if dist(x,y,cx,cy) <= d/2:
        return True
    else:
        return False

def setup():
    size(600, 400)
    
def draw():
    background(100)
    if collidePointCircle(mouseX, mouseY, 300, 200, 70):
        fill(165, 0, 0)
        background(255)
    else:
        fill(255)
        background(165,0,0)
    ellipse(300, 200, 70, 70)
    strokeWeight(0)
    point(mouseX, mouseY)
    strokeWeight(1)
