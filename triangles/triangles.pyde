def setup():
    size(600,400)
    background(0)
def draw():
    fill(random(255),random(0),random(0))
    stroke(random(255),random(0),random(0))   
    triangle(random(300),random(200),random(300),random(200),random(300),random(200))
    fill(random(0),random(0),random(255))
    stroke(random(0),random(0),random(255))
    triangle(random(300,600),random(200),random(300,600),random(200),random(300,600),random(200))
    fill(random(0),random(255),random(0))
    stroke(random(0),random(255),random(0))
    triangle(random(300),random(200,400),random(300),random(200,400),random(300),random(200,400))
    fill(random(255),random(230),random(0))
    stroke(random(255),random(230),random(0))
    triangle(random(300,600),random(200,400),random(300,600),random(200,400),random(300,600),random(200,400))