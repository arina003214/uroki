'''
Изяслав решил сделать красивый проект —
бабочка крутится, всё дальше отдаляясь от центра, и закрашивает собой холст
Должны получиться красивые узоры. Но программа даже не запускается.
Как исправить это?

'''

ugol = 0
x = 0

def setup():
    size(700,700)
    img = loadImage('butterfly2-a.png')
    imageMode(CENTER)
    global ugol, x,img
    frameRate(400000000000000000000000000000000000000000000000000000000000000000000000000000)
    
    
def draw():
    global ugol, x,img
    translate(350, 350)
    rotate(radians(ugol))
    image(img, x, 0)
    ugol = ugol + 5
    x = x + 0.1
    
