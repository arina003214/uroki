x=0
def setup():
    size(1000,1000)
    background(49,53,90)
def draw():
    # снег с неба
    push()
    stroke(255)
    frameRate(260)
    background(49,53,90)
    global x
    x=x+1
    strokeWeight(20)
    #1
    point(50,x-40)
    #2
    point(150,x-15)
    #3
    point(250,x+20)
    #4
    point(350,x-30)
    #5
    point(450,x+10)
    #6
    point(550,x+25)
    #7
    point(650,x-35)
    #8
    point(750,x+20)
    #9
    point(850,x-40)
    #10
    point(950,x-15)
    #11
    point(100,x-100)
    #12
    point(200,x-120)
    #13
    point(300,x-130)
    #14
    point(400,x-150)
    #15
    point(500,x-140)
    #16
    point(600,x-110)
    #17
    point(700,x-160)
    #18
    point(800,x-170)
    #19
    point(900,x-190)
    #20
    point(50,x-220)
    #21
    point(150,x-230)
    #22
    point(250,x-250)
    #23
    point(350,x-240)
    #24
    point(450,x-260)
    #25
    point(550,x-270)
    #26
    point(650,x-290)
    #27
    point(750,x-280)
    #28
    point(850,x-300)
    #29
    point(950,x-310)
    #30
    point(100,x-350)
    #31
    point(200,x-320)
    #32
    point(300,x-360)
    #33
    point(400,x-340)
    #34
    point(500,x-350)
    #35
    point(600,x-370)
    #36
    point(700,x-380)
    #37
    point(800,x-390)
    #38
    point(900,x-400)
    #39
    point(30,x-420)
    #40
    point(150,x-410)
    #41
    point(250,x-430)
    #42
    point(350,x-420)
    #43 
    point(450,x-440)
    #44
    point(550,x-450)
    #45
    point(650,x-470)
    #46
    point(750,x-460)
    #47
    point(850,x-480)
    #48
    point(950,x-490)
    #49
    point(100,x-500)
    #50
    point(200,x)
    
    
    
    if x > 1000:
        x=0
    pop()
    # обводка для всех предметов
    strokeWeight(5)
    
    # снег на земле
    rect(0,850,1000,150)
    
    # ДОМ
    
    # основа дома
    rect(590,530,350,350)
    # труба
    rect(820,290,90,159)
    # крыша 
    triangle(765,300,520,540,1000,540)
    # дверь 
    rect(715,705,100,175)
    # окна 
    push() 
    fill(100,183,159)
    rect(605,580,100,100)
    translate(220,0)
    rect(605,580,100,100)
    pop()
    # решетки на окнах
    line(605,630,705,630)
    line(655,580,655,680)
    translate(220,0)
    line(605,630,705,630)
    line(655,580,655,680)
    
    # дверная ручка
    ellipse(520,790,20,20) 
    
    # СНЕГОВИК 
    
    # круг номер 1 
    ellipse(100,840,220,220)
    # круг номер 2 
    ellipse(100,680,180,180)
    # круг номер 3 
    ellipse(100,550,140,140)
    # нос снеговика
    push()
    fill(234,110,14)
    triangle(100,560,100,580,200,590)
    pop()
    # глаза снеговика
    push()
    strokeWeight(25)
    point(120,530)
    point(70,530)
    # пуговицы снеговика
    point(100,660)
    point(100,710)
    point(100,820)
    point(100,880)
    pop()
    # ведро у снеговика
    
    
