size(1000,1000)
background(49,53,90)

# ДОМ

# снег 
rect(0,850,1000,150)
# основа дома
rect(590,530,350,350)
# труба
rect(820,290,90,159)
# крыша 
triangle(765,300,520,540,1000,540)
# дверь 
rect(715,705,100,175)
# окна  
rect(605,580,100,100)
translate(220,0)
rect(605,580,100,100)
# решетки на окнах
line(605,630,705,630)
line(655,580,655,680)
translate(-220,0)
line(605,630,705,630)
line(655,580,655,680)
# дверная ручка
ellipse(735,790,20,20) 

# СНЕГОВИК 

# круг номер 1 
ellipse(300,840,220,220)
# круг номер 2 
ellipse(300,680,180,180)
# круг номер 3 
ellipse(300,550,140,140)
# нос снеговика