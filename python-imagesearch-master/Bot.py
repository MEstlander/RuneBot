from typing import Any

from imagesearch import *


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
    Loops through functions
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
        click_image("images/iore.png", (isx-16,isy-16), "left", r(0.1,0.1), offset=32)
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
        fullinv = imagesearcharea("images/fullinvi.png",0,0,963,623)
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
    pos=imagesearcharea("images/iore.png",isx,isy,isx+32,isy+32,precision=0.3)
    gempos=imagesearcharea("images/gem.png",isx,isy,isx+32,isy+32,precision=0.2)
    while pos[0]==-1 and gempos[0]==-1:
        gempos=imagesearcharea("images/gem.png",isx,isy,isx+32,isy+32,precision=0.2)
        if j==20:
            print("took too long")
            mining()
        pos=imagesearcharea("images/iore.png",isx,isy,isx+32,isy+32,precision=0.3)
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


