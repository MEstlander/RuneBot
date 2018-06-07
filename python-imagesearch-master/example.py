from typing import Any

from imagesearch import *


"""
Mycke globals e alltti ett tecken på bra kod!
"""
time3=0
time2=0
time1=0
i=0
isx=565
isy=240
oisx=isx
oisy=isy

def loop():
    """
    Loopar igenom functionen
    """
    global i,isx,isy,oisx,oisy

    while True:
        mining()
        i=i+1
        if i%4==0:
            isx=isx-126
            isy=isy+36
        else:
            isx=isx+42
        if i>=24:
            i=0
            isy=oisy
            isx=oisx
            dropping()

def dropping():
    """
    drops full inventory
    """
    global i,isy,isx,oisx,oisy
    while i<24:
        click_image("iore.png", (isx-16,isy-16), "left", r(0.1,0.1), offset=32)
        i=i+1
        if i%4==0:
            isx=isx-126
            isy=isy+36
        else:
            isx=isx+42
    i=0
    isx=oisx
    isy=oisy


"""
def dropone():
    pos = imagesearcharea("iore.png",0,0,963,623)
    while pos[0]==-1:
        pos = imagesearcharea("iore.png",0,0,963,623)
        if pos[0]!=-1:
            click_image("iore.png", pos, "left", r(0.1,0.1), offset=15)
        time.sleep(0.5)
"""
def mineone(ore):
    """
    :param ore: path ti en bild som ska hittas
    o sen kollar den också om man får inventory full notification
    o flyttar musen ti ett rändom ställe bort från spele (dunno why ja har de men whatevs)
    """
    global time1,i,isx,isy,oisx,oisy
    j=0
    pos=imagesearcharea(ore,0,0,532,400,precision=0.5)
    while pos[0]==-1:
        if j==20:
            print("took a long ass time")
        else:
            pos=imagesearcharea(ore,0,0,532,400,precision=0.5)
        time.sleep(0.3)
    if pos[0]!=-1:
        click_image(ore, pos, "left", r(0.1,0.1), offset=40)
        fullinv = imagesearcharea("fullinvi.png",0,0,963,623)
        if fullinv[0] != -1:
            dropping()
        pyautogui.moveTo(r(700,500),r(100,500),r(0.5,1))
        time.sleep(r(0,0.5))

def checkore(isx,isy):
    """
    Kollar om det kommer en iron ore till inventoryn
    Image recognitionen gör alla bilder gråa så den kan
    int se skillnad mellan brun(kan mineas) o grå (väntar på respawn)
    """
    j=0
    pos=imagesearcharea("iore.png",isx,isy,isx+32,isy+32,precision=0.3)
    gempos=imagesearcharea("gem.png",isx,isy,isx+32,isy+32,precision=0.2)
    while pos[0]==-1 and gempos[0]==-1:
        gempos=imagesearcharea("gem.png",isx,isy,isx+32,isy+32,precision=0.2)
        if j==20:
            print("took too long")
            mining()
        pos=imagesearcharea("iore.png",isx,isy,isx+32,isy+32,precision=0.3)
        j+=1
def miningtwo():
    """
    En annan spot
    """
    global i,time1,time2
    print(str(i))
    if i%2==0:
        if (time2-time1) < 5.4:
            time.sleep(min(time2-time1,5.4))
        mineone("iore2/rock1.png")
        checkore(isx,isy)
        time1=time.time()
    else:
        if (time1-time2) < 5.4:
            time.sleep(min(time1-time2,5.4))
        mineone("iore2/rock2.png")
        checkore(isx,isy)
        time2=time.time()

def mining():
    """
    "Main spotten"
    """
    global i,time1,time2,time3
    print(str(i))
    if i%3==0:
        if (time.time()-time1) < 5.4:
            time.sleep(min(time.time()-time1,5.4))
        mineone("iore/rock1.png")
        checkore(isx,isy)
        time1=time.time()
    elif i%3==1:
        if (time.time()-time2) < 5.4:
            time.sleep(min(time.time()-time2,5.4))
        mineone("iore/rock2.png")
        checkore(isx,isy)
        time2=time.time()
    else:
        if (time.time()-time3) < 5.4:
            time.sleep(min(time.time()-time3,5.4))
        mineone("iore/rock3.png")
        checkore(isx,isy)
        time3=time.time()




#dropping()
#loop()
#mining()
"""
def mining():
    i=0
    pos = imagesearcharea("iore2/rock1.png",0,0,963,623)
    if pos[0]!=-1:
        print("found image")
        click_image("iore2/rock1.png", pos, "left", r(0.1,0.1), offset=20)
        pyautogui.moveTo(r(900,200),r(300,250),r(1,1))
    dedpos = imagesearcharea("iore2/erock1.png",0,0,963,623)
    pos2 = imagesearcharea("iore2/rock2.png",0,0,963,623)
    fullinv = imagesearcharea("fullinvi.png",0,0,963,623)
    if fullinv[0] != -1:
        dropping()
        loop()
    while dedpos[0] == -1:
        if i==50:
            mining()
        fullinv = imagesearcharea("fullinvi.png",0,0,963,623)
        if fullinv[0] != -1:
            dropping()
            loop()
        dedpos = imagesearcharea("iore2/erock1.png",0,0,963,623)
        print("sleeping1")
        time.sleep(0.2)
        i =i+1
    i=0
    if pos2[0]!=-1:
        print("found image2")
        click_image("iore2/rock2.png", pos2, "left", r(0.1,0.1), offset=30)
        pyautogui.moveTo(r(900,200),r(300,250),r(1,1))
    dedpos2 = imagesearcharea("iore2/erock2.png",0,0,963,623)
    fullinv = imagesearcharea("fullinvi.png",0,0,963,623)
    if fullinv[0] != -1:
        dropping()
        loop()
    while dedpos2[0] == -1:
        if i==50:
            loop()
        fullinv = imagesearcharea("fullinvi.png",0,0,963,623)
        if fullinv[0] != -1:
            dropping()
            loop()
        dedpos2 = imagesearcharea("iore/erock2.png",0,0,963,623)
        print("sleeping2")
        time.sleep(0.2)
        i = i + 1
"""
"""
#Triple spot alkharid north and up
def mining():
    i=0
    pos = imagesearcharea("iore/rock1.png",0,0,963,623)
    if pos[0] != -1:
        print("found image")
        click_image("iore/rock1.png", pos, "left", r(0.1,0.1), offset=20)

        pyautogui.moveTo(r(900,200),r(300,250),r(1,1))
    dedpos = imagesearcharea("iore/erock1.png",0,0,963,623)
    pos2 = imagesearcharea("iore/rock2.png",0,0,963,623)
    while dedpos[0] == -1:
        if i == 20:
            mining()
        fullinv = imagesearcharea("fullinv.png",0,0,963,623)
        if fullinv[0] != -1:
            dropping()
            loop()
        dedpos = imagesearcharea("iore/erock1.png",0,0,963,623)
        print("sleeping1")
        time.sleep(0.2)
        i =i+1
    if pos2[0] != -1:
        print("found image2")
        click_image("iore/rock2.png", pos2, "left", r(0.1,0.1), offset=30)
        pyautogui.moveTo(r(900,200),r(300,250),r(1,1))
    dedpos2 = imagesearcharea("iore/erock2.png",0,0,963,623)
    pos3 = imagesearcharea("rock3.png",0,0,963,623)
    while dedpos2[0] == -1:
        if i == 20:
            loop()
        fullinv = imagesearcharea("fullinv.png",0,0,963,623)
        if fullinv[0] != -1:
            dropping()
            loop()
        dedpos2 = imagesearcharea("iore/erock2.png",0,0,963,623)
        print("sleeping2")
        time.sleep(0.2)
        i = i + 1
    if pos3[0] != -1:
        print("found image3")
        click_image("iore/rock3.png", pos2, "left", r(0.1,0.1), offset=30)
        pyautogui.moveTo(r(900,200),r(300,250),r(1,1))
    dedpos3 = imagesearcharea("iore/erock3.png",0,0,963,623)
    while dedpos3[0] == -1:
        if i == 20:
            loop()
        fullinv = imagesearcharea("fullinv.png",0,0,963,623)
        if fullinv[0] != -1:
            dropping()
            loop()
        dedpos3 = imagesearcharea("emptyrock3.png",0,0,963,623)
        print("sleeping3")
        time.sleep(0.2)
        i = i + 1
"""
"""
# Search for the github logo on the whole screen
# note that the search only works on your primary screen.

# This is intended to be used as examples to be copy pasted, do not run the whole file at once

# pos = imagesearch("github.png")
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")

# search for the github logo continuously :

# pos = imagesearch_loop("github.png", 0.5)
#
# print("image found ", pos[0], pos[1])
#
# # search for the logo on the 0,0,800,600 region
#  (a rectangle starting from the top left going 800 pixels to the right and down 600 pixels)
#
# pos = imagesearcharea("github.png", 0, 0, 800, 600)
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")

# the im parameter is usefull if you plan on looking for several different images without the need for recapturing the screen
# the screen capture being one of the most time consuming function it's a good way to optimize

# non -optimized way :
# time1 = time.clock()
# for i in range(10):
#     imagesearcharea("github.png", 0, 0, 800, 600)
#     imagesearcharea("panda.png", 0, 0, 800, 600)
# print(str(time.clock() - time1) + " seconds (non optimized)")
#
# # optimized way :
#
# time1 = time.clock()
# im = region_grabber((0, 0, 800, 600))
# for i in range(10):
#     imagesearcharea("github.png", 0, 0, 800, 600, 0.8, im)
#     imagesearcharea("panda.png", 0, 0, 800, 600, 0.8, im)
# print(str(time.clock() - time1) + " seconds (optimized)")

# sample output :

# 1.6233619831305721 seconds (non optimized)
# 0.4075934110084374 seconds (optimized)


# click image is to be used after having found the image
#x,y,x+32,y+32
#x+36,y,x+36+32,y
#isx = inventory start x
#isy = inventory start y
"""