from os import close
import tkinter as tk
import winsound
from random import randbytes, randrange
from tkinter import Button, Image, Label, constants
from tkinter import font
from typing import Text
root=tk.Tk()
root.geometry("2000x1000")
frame=tk.Frame()
frame.master.title("SPACE MINER")
canvas=tk.Canvas(frame)
# ----------------------images------------------
img=tk.PhotoImage(file="image\space.png")
air=tk.PhotoImage(file="image\Air.png")
enemy=tk.PhotoImage(file="image\enemy.png")
point=tk.PhotoImage(file="image\point.png")
bgFirst=tk.PhotoImage(file="image\space1.png")
gameOver=tk.PhotoImage(file="image\gameOver.png")
winStyle=tk.PhotoImage(file="image\winStyle.png")
winGame=tk.PhotoImage(file="image\win.png")
winSpace=tk.PhotoImage(file="image\winspace.png")
Wall=tk.PhotoImage(file="image\wall.png")

# ------------------------grid constants----------------
GRID=[
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [4,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [4,0,0,0,4,4,4,0,0,0,0,0,4,0,4,0,0,0,0,0,4,4,4,0,0,0,4],
    [4,0,0,0,4,0,2,0,0,2,0,4,0,3,0,4,0,0,0,0,0,2,4,0,2,0,4],
    [4,0,0,0,4,0,0,0,0,2,4,0,0,0,0,2,4,0,0,0,3,0,4,0,0,2,4],
    [4,0,0,0,0,0,0,0,0,4,3,0,0,4,0,0,0,4,0,0,0,0,0,0,0,0,4],
    [4,0,0,0,3,0,0,0,4,0,0,0,0,0,0,4,2,0,4,0,0,2,3,0,0,0,4],
    [4,0,0,0,0,0,0,0,0,4,0,0,4,0,4,3,0,4,0,0,2,0,0,0,0,0,4],
    [4,2,0,0,0,0,0,0,0,0,4,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,4],
    [4,0,0,0,4,2,0,0,0,0,0,4,0,0,0,4,2,0,0,0,0,0,4,0,0,2,4],
    [4,0,0,0,4,3,0,0,0,0,0,0,4,0,4,0,0,0,0,0,0,3,4,0,0,0,4],
    [4,0,0,0,4,4,4,3,0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,0,0,0,4],
    [4,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,2,0,0,0,0,0,0,4],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
]
notLost = True
number=0
# ---------------------function showCrystals----------------
def draw():
    global buttonPlay
    canvas.create_image(600,400,image=img)
    canvas.create_text(1250,590,text="Your Score",font=("Pursia",15),fill="white")
    x2=50
    y2=50
    global notLost, number
    if notLost and number <100:
        for col in GRID:
            for row in col:
                if row==1:
                    canvas.create_image(x2-25,y2-25,image=air)
                elif row==2:
                   canvas.create_image(x2-25,y2-25,image=enemy)
                elif row==3:
                    canvas.create_image(x2-25,y2-25,image=point)
                elif row==4:
                    canvas.create_image(x2-25,y2-25,image=Wall)
                x2+=50
            x2=50
            y2+=50
    elif number == 100:
        win()
    else:
        lose()
    canvas.create_text(1250,620,text=number,font=("Pursia",15),fill="white")
    canvas.delete(buttonPlay)

def bg():
    canvas.create_image(650,400,image=bgFirst)
    canvas.create_text(100,20,text="Space Miner",font=("Pursia",20),fill="white")
    canvas.create_image(90,70,image=air)
    canvas.create_text(680,650,text="Click here to Play",font=("Pursia",20),fill="black")
    winsound .PlaySound("sound\play.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
bg()


# ------------------------countPoint When airplane crash Crystal------
canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
myPoint=canvas.create_text(1250,660,text="0",font=("Pursia",15),fill="white")
def countPoints():
    global number,myPoint
    if number<100:
        number+=10
        winsound .PlaySound("sound\solid.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        canvas.delete("all")
        canvas.create_image(400,400,image=img)
# ---------------------Button play first window--------------------
def onClick():
    draw()
    winsound .PlaySound("sound\spacebackground.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
buttonPlay = tk.Button(root,text="Play",font=("Pursia",15),fg="white",bg="blue",pady=15,padx=100,command=onClick)
buttonPlay=canvas.create_window(550,250,anchor="nw", window=buttonPlay)
# ------------------------button restart when game over-----------------
def restart():
    draw()
buttonRestart= tk.Button(root,text="RESTART",font=("Times",14,"bold"),fg="white",bg="blue",pady=12,padx=50,command=restart)
# ---------------button start when game win-------------
def start():
    draw()
buttonStart =Button(root,text="Play",font=("Pursia",15),fg="white",bg="blue",pady=12,padx=50,command=start)
# ------------------button exit when player want to leave program------------
def close():
    root.destroy()
buttonClose=Button(text="EXIT", font=("Times", 14,"bold"),fg="white",bg="blue",pady=12,padx=50,command=close)
# --------------------function for display win and lose-------------
def win():
    global buttonStart,buttonClose
    canvas.delete("all")
    canvas.create_window(530,450,anchor="nw", window=buttonStart)
    canvas.create_window(700,450,anchor="nw", window=buttonClose)
    canvas.create_image(680,250,image=winSpace)
    canvas.create_image(680,200,image=winGame)
    canvas.create_image(680,200,image=winStyle)
    canvas.create_text(680,400,text="CONGRATULATION",font=("Pursia",15,"bold"),fill="white")
    canvas.create_text(680,600,text=number,font=("Pursia",15),fill="white")
    canvas.create_text(680,550,text="Your Score",font=("Pursia",15),fill="white")
    winsound .PlaySound("sound\win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
def lose():  
    global buttonClose,buttonRestart
    canvas.delete("all")
    canvas.create_window(450,350,anchor="nw", window=buttonRestart)
    canvas.create_window(700,350,anchor="nw", window=buttonClose)
    canvas.create_image(700,400,image=gameOver)
    canvas.create_text(100,100,text=number,font=("Pursia",15),fill="white")
    canvas.create_text(100,50,text="Your Score",font=("Pursia",15),fill="white")
    winsound .PlaySound("sound\lose.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ---------------------------moveright----------------
def moveRight(event):
    canvas.delete("all")
    canvas.create_image(400,400,image=img)
    canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
    canvas.create_text(1250,660,text=number,font=("Pursia",15),fill="white")
    isRight=False
    for col in range(len(GRID)):
        for row in range(len(GRID[col])-1):
            if GRID[col][row]==1 and not isRight and GRID[col][row+1]==0:
                GRID[col][row]=0
                GRID[col][row+1]=1
                isRight=True
            elif (GRID[col][row]==1) and (not isRight) and (GRID[col][row+1]==3):
                GRID[col][row]=0 
                GRID[col][row+1]=1
                countPoints()
                isRight=True
            elif (GRID[col][row]==1) and (GRID[col][row+1]==2) and (GRID[col][row-1]==0) and not isRight:
                lose()
                isRight=True
                canvas.destroy("all")
    draw()
# ----------------------------moveLeft----------------------------
def moveleft(event):
    canvas.delete("all")
    canvas.create_image(400,400,image=img)
    canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
    canvas.create_text(1250,660,text=number,font=("Pursia",15),fill="white")
    isLeft=False
    for col in range(len(GRID)):
        for row in range(len(GRID[col])):
            if GRID[col][row]==1 and not isLeft and GRID[col][row-1]==0 and GRID[col][row-1]!=2:
                GRID[col][row]=0
                GRID[col][row-1]=1
                isLeft=True
            elif (GRID[col][row]==1) and (not isLeft) and (GRID[col][row-1]==3):
                GRID[col][row]=0 
                GRID[col][row-1]=1
                countPoints()
                isLeft=True
            elif (GRID[col][row]==1) and (GRID[col][row-1]==2) and (GRID[col][row+1]==0) and not isLeft:
                lose()
                isLeft=True
                canvas.destroy("all")
    draw()
# # --------------------moveDown------------------
def moveDown(event):
    global GRID, notLost
    canvas.delete("all")
    canvas.create_image(400,400,image=img)
    canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
    canvas.create_text(1250,660,text=number,font=("Pursia",15),fill="white")
    isDown=False
    for col in range(len(GRID)):
        for row in range(len(GRID[col])-1):
            if GRID[col][row]==1 and not isDown and GRID[col+1][row]==0:
                GRID[col][row]=0
                GRID[col+1][row]=1
                isDown=True
            elif (GRID[col][row]==1) and (not isDown) and (GRID[col+1][row]==3):
                GRID[col][row]=0 
                GRID[col+1][row]=1
                countPoints()
                isDown=True
            elif (GRID[col][row]==1) and (GRID[col+1][row]==2) and (GRID[col-1][row]==0) and not isDown:
                lose()
                isDown=True
                canvas.destroy("all")
    draw()
# # -------------------------------------moveUp-------------------
def moveUp(event):
    global GRID
    canvas.delete("all")
    canvas.create_image(400,400,image=img)
    canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
    canvas.create_text(1250,660,text=number,font=("Pursia",15),fill="white")
    canvas.itemconfig(myPoint,text=str(number))
    isUp=False
    for col in range(len(GRID)):
        for row in range(len(GRID[col])):
            if GRID[col][row]==1 and not isUp and GRID[col-1][row]==0:
                GRID[col][row]=0 
                GRID[col-1][row]=1
                isUp=True
            elif (GRID[col][row]==1) and (GRID[col-1][row]==3) and not isUp:
                GRID[col][row]=0 
                GRID[col-1][row]=1
                countPoints()
                isUp=True
            elif (GRID[col][row]==1) and (GRID[col-1][row]==2) and (GRID[col+1][row]==0) and not isUp:
                lose()
                isUp=False
                canvas.destroy("all")
    draw() 
# ------------------key event click for move player-------------
root.bind("<Right>",moveRight)
root.bind("<Left>",moveleft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)
# ----------------display------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()