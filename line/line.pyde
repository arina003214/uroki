# Задание 1
# 1. Из центра по косой линии движется точка. 
# 2. Сделай, чтобы это была не точка, а конец линии, начало которой всегда в центре. 
# 3. Не стирай предыдущие кадры. 
# 4. Используй случайный цвет.
x=300
y=300
def setup():
    size(600, 600)  
    
def draw():
    # тут команды
    strokeWeight(10)
    stroke(random(255),random(255),random(255))
    global x 
    global y
    x=x+1
    y=y+1
    line(x,y,300,300)
    
