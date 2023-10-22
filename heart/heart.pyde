x=35
y=0
t=70
r=105
e=140
w=175
q=210
p=245
o=280
i=315
u=350
a=385
s=420
def setup():
    size(1000,1000)
    background(0)
    stroke(255,0,0)
    strokeWeight(10)
def draw():
    background(0)
    global x 
    global y
    global t
    global r
    global e 
    global w 
    global q
    global p
    global o
    global i
    global u 
    global a 
    global s 
    s=s+1
    a=a+1
    u=u+1
    i=i+1
    o=o+1
    p=p+1 
    q=q+1
    w=w+1
    e=e+1
    r=r+1
    t=t+1
    y=y+1
    x=x+1
    translate(150,0)
    point(450,x)
    point(150,x)
    point(300,x)
    point(400,y)
    point(350,y)
    point(250,y)
    point(200,y)
    point(140,t)
    point(460,t)
    point(460,r)
    point(140,r)
    point(150,e)
    point(450,e)
    point(165,w)
    point(435,w)
    point(180,q)
    point(420,q)
    point(200,p)
    point(400,p)
    point(220,o)
    point(380,o)
    point(240,i)
    point(360,i)
    point(260,u)
    point(340,u)
    point(280,a)
    point(320,a)
    point(300,s)
