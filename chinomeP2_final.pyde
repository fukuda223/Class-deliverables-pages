t = 0
timer = 0
base_time=0
flag=False
before_time=0
flagx=1
count = 0
v = 0
import time

#add_library('minim')
#amp=200.0
#leftY=200
#rightY=600

def setup():
    global img1,img2,img3,img4,img5,img6,img7,img8,img9,img10
    size(400,400)
    textSize(30)
    smooth()
    frameRate(30)
    img1=loadImage("character_murabito_middle_man_green.png")
    img2=loadImage("character_yusha_01_red.png")
    img3=loadImage("character_kamisama_silver.png")
    img4=loadImage("kanoke_halloween_01.png")
    img5=loadImage("character_monster_slime_green.png")
    img6=loadImage("character_monster_zombie_brown.png")
    img7=loadImage("character_monster_mummy_red.png")
    img8=loadImage("character_monster_skeleton_02.png")
    img9=loadImage("character_monster_shinigami_02.png")
    img10=loadImage("character_monster_mao_02.png")
    
    
def draw():
    global h,m,s,flag
    h=hour()
    m=minute()
    s=second()
    
    drawBackDemo()#繰り返し処理　背景色の変更　確認用(30秒ごとに色が変化する)
    #drawBack()#繰り返し処理　背景色の変更
    if flagx ==1:
        drawDC()#デジタル時計
    elif flagx ==2:
        drawTimer()#タイマー
    elif flagx ==3:
        drawStop()#ストップウォッチ
    elif flagx ==4:
        date1()#日付
    drawEllipse()#外枠の円
    drawScale()#目盛り
    drawHour()#時針
    drawMinute()#分針
    drawSecond()#秒針
    date1()#日付
    date2()#継続日数
    km()#走る目標距離


def drawBackDemo():#繰り返し処理　背景色の変更　確認用(30秒ごとに色が変化する)
    if s>=00 and s<=29:
        background(135,206,235)
        stroke(0,0,0)
    else:
        background(255,254,59)
        stroke(0,0,0)


#def drawBack():#繰り返し処理　背景色の変更
    #if h>=6 and h<=17:
        #background(135,206,235)
        #stroke(0,0,0)
    #else:
        #background(99,237,1)
        #stroke(255,255,255)

def drawDC():#デジタル時計
    if s>=00 and s<=29:
    #if h>=6 and h<=17:
        fill(10)
    else:
        fill(10)
    text("Clock Mode",100,250)
    noFill()
    text(nf(hour(),2)+":"+nf(minute(),2)+":"+nf(second(),2),120,300)
    #nf()は表示フォーマット　2桁の表示　hour()minute()second()は関数　現在の時分秒がわかる
    #print("{}:{}:{}".format(h,m,s))

        
def drawEllipse():#外枠の円
    translate(width/2,height/2)#指定した位置に描画の視点を移動するtranslate()
    ellipse(0,0,width,height)
    noFill()
    

def drawScale():#目盛り
    pushMatrix()#現在の座標を一時的に保存するpushMatrix()
    if s>=00 and s<=29:
    #if h>=6 and h<=17:
        fill(10)
    else:
        fill(10)
    noStroke()
    text("1",70,-120)
    text("2",120,-60)
    text("3",150,10)
    text("4",120,90)
    text("5",70,140)
    text("6",-11,165)
    text("7",-90,140)
    text("8",-140,90)
    text("9",-170,10)
    text("10",-150,-60)
    text("11",-100,-120)
    text("12",-20,-140)

    for i in range(60):
        rotate(radians(6))
        ellipse(175,1,5,5)
    for i in range(12):
        rotate(radians(30))#指定した角度だけ座標を回転させるrorate()
        ellipse(175,0,15,15)
    popMatrix()#保存した座標を呼び出すpopMatrix()
    noFill()
    stroke(255)


def drawHour():#時針
    global h
    pushMatrix()
    stroke(175,0,0)    
    rotate(radians(h*(360/12)))
    strokeWeight(10)
    line(0,0,0,-height/3)
    popMatrix()


def drawMinute():#分針
    global m
    pushMatrix()
    stroke(175,0,0)
    rotate(radians(m*(360/60)))
    strokeWeight(5)
    line(0,0,0,-height/2)
    popMatrix()


def drawSecond():#秒針
    global s
    pushMatrix()
    stroke(255,0,0)
    rotate(radians(s*(360/60)))
    strokeWeight(2)
    line(0,0,0,-height/2)
    popMatrix()
        
def drawTimer():
    global t,timer
    if s>=00 and s<=29:
    #if h>=6 and h<=17:
        fill(10)
    else:
        fill(10)
    text("Timer Mode",95,250)
    noFill()
    if timer == 1:
        text(t - time.time(),130,300)
        if t - time.time()<0:
            timer = 0

def keyPressed():
    global timer,t,flagx, count,v
    if key == "1":
        flagx=1
        timer=0
    elif key == "2":
        flagx=2
        if timer==0:
            timer = 1
            t = time.time() + 10
    elif key == "3":
        flagx=3
        timer=0
    elif key == "4":
        flagx=4
    
    
    if key =='2':
        count += 1
        v += 1
    if key =='5':
        count=0
        v=0
        
def drawStop():
    global base_time,before_time
    now = millis()
    if flag == False:
        base_time = now
        #noLoop()
    time = now - base_time
    if before_time != 0:
        time = before_time
    ms = time%1000
    ss = time/1000%60
    m = time/1000/60
    textSize(30)
    if s>=00 and s<=29:
    #if h>=6 and h<=17:
        fill(10)
    else:
        fill(10)
    text("Stop Watch Mode",70,250)
    noFill()
    text(nf(m,2)+":"+nf(ss,2)+"."+nf(ms,3),120,300)

def mousePressed():
    global flag, base_time,before_time
    now=millis()
    if (mouseX, mouseY):
         if flag == False:
            flag = True
            base_time = now
            before_time = 0
            #Loop()
         else:
            flag = False
            before_time=now-base_time
            # noLoop()

#モード切り替えのプログラムはプロ言基礎05参照
import datetime

def date1():
    import datetime
    dt=datetime.date.today()
    #print(dt)
    if s>=00 and s<=29:
    #if h>=6 and h<=17:
        fill(10)
    else:
        fill(10)
    text("Date Mode",110,250)
    text(str(dt),100,300)
    noFill()
   # ボタンのカウントを初期化

def date2():
    fill(0,0,0)
    text(count, 0, -40)
    text("Lv", -35, -40)
    
def km():
    print(v)
    if v>=0 and v<=14:
        text("Today11km",-120,10)
        image(img1,-20,-130)
        img_resize = img1.resize(50, 50)
        img_resize
    if v>=15 and v<=23:
        text("Today9km",-120,10)
        image(img2,-20,-130)
        img_resize = img2.resize(50, 50)
        img_resize
    if v>=24 and v<=29:
        text("Today7km",-120,10)
        image(img3,-20,-130)
        img_resize = img3.resize(50, 50)
        img_resize
    if v>=30:
        text("Today5km",-120,10)
        image(img4,-20,-130)
        img_resize = img4.resize(50, 50)
        img_resize
    if v>=60:
        image(img5,-20,-130)
        img_resize = img5.resize(50, 50)
        img_resize
    if v>=70:
        image(img6,-20,-130)
        img_resize = img6.resize(50, 50)
        img_resize
    if v>=90:
        image(img7,-20,-130)
        img_resize = img7.resize(50, 50)
        img_resize
    if v>=120:
        image(img8,-20,-130)
        img_resize = img8.resize(50, 50)
        img_resize
    if v>=160:
        image(img9,-20,-130)
        img_resize = img9.resize(50, 50)
        img_resize
    if v>=200:
        image(img10,-20,-130)
        img_resize = img10.resize(50, 50)
        img_resize
