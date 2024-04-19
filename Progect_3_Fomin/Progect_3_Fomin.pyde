def col(x,y,w,h,x2,y2,w2,h2):
   if (x + w >= x2) and (x <= x2 + w2) and (y + h >= y2) and (y <= y2 + h2):
       return True
   else:
       return False
x = 50
y = 950
ysp = 0
grav = 0.2
jump = False
pr = -6
a = False
xy = 700
yx = 975
x1 = 0
y1 = -100
r = 0
s = 0
o = True
sx = 3200
def setup():
    size(1920,1000)
    rectMode(CENTER)
def draw():
    global x,y,ysp,grav,jump,pr,a,xy,yx,r,s,o,sx
    background(1)
    rect(x,y,50,50)
    ysp += grav
    y += ysp
    o = True
    if y > height - 25:
        y = height - 25
        ysp = 0
        a = False
        jump = a
    if x > 600:
        xy -= 6
        x -= 6  
        sx -= 6
    x += 6
    if col(xy,yx,50,50,x,y,50,50):
        ysp = -0.2
        jump == False
    if col(xy + 500,yx,50,50,x,y,50,50):
        ysp = -0.2
        jump == False
        if mousePressed == True:
            ysp = pr
    if col(xy,yx,1,1,x,y,50,50):
        noLoop()
    if col(xy + 500,yx,1,1,x,y,50,50):
        noLoop()
    if col(xy + 65,yx + 25,20,40,x,y,50,50):
        noLoop()
    if col(xy + 1115,yx + 25,20,40,x,y,50,50):
        noLoop()
    if col(sx + 700,yx - 975,1,195,x,y,50,50):
        noLoop()
    if col(sx + 900,yx + 25,1,795,x,y,50,50):
        noLoop()
    if col(sx + 700,yx - 200,1,420,x,y,50,50):
        noLoop()
    if col(sx + 900,yx - 975,1,245,x,y,50,50):
        noLoop()
    if col(sx + 1220,yx + 25,1,195,x,y,50,50):
        noLoop()
    if col(sx + 1220,yx - 975,1,430,x,y,50,50):
        noLoop()
    if col(sx + 1500,yx + 25,1,795,x,y,50,50):
        noLoop()
    if col(sx + 1500,yx - 975,1,1,x,y,50,50):
        noLoop()
    if col(sx + 1800,yx - 975,1,400,x,y,50,50):
        noLoop()
    if col(sx + 1800,yx + 25,1,400,x,y,50,50):
        noLoop()
    if col(xy + 1500,yx,1000,50,x,y,50,50):
        ysp = -0.2
        jump == False
        if mousePressed == True:
            ysp = pr
    if col(xy + 2475,yx - 100,50,100,x,y,50,50):
        r = 1
    if col(xy + 1500,yx,1,1,x,y,50,50):
        noLoop()
    else:
        rect(xy,yx,50,50)
        rect(xy + 500,yx,50,50)
        triangle(xy + 50,yx + 25,xy + 100,yx + 25, xy + 75,yx - 25)
        triangle(xy + 1100,yx + 25,xy + 1150,yx + 25, xy + 1125,yx - 25)
        rect(xy + 2000,yx,1000,50)
        fill(255,0,222)
        ellipse(xy + 2500, yx - 100,50,100)
        fill(255)
        rect(sx + 700,yx - 200,50,425)
        rect(sx + 700,yx - 975,50,200)
        rect(sx + 900,yx + 25,50,800)
        rect(sx + 900,yx - 975,50,250)
        rect(sx + 1220,yx + 25,50,200)
        rect(sx + 1220,yx - 975,50,800)
        rect(sx + 1500,yx + 25,50,800)
        rect(sx + 1500,yx - 975,50,300)
        rect(sx + 1800,yx - 975,50,750)
        rect(sx + 1800,yx + 25,50,750)
def mousePressed():
    global x,y,ysp,grav,jump,pr,a,xy,yx,r,s,o
    if jump == False or r == 1:
        ysp = pr
        a = True
        jump = a 
    
