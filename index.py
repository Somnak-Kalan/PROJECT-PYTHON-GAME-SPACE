from os import close
import tkinter as tk
import winsound
from random import randbytes, randrange
from tkinter import Button, Image, Label, Variable, constants
from tkinter import font
from typing import Text
# ------------------create window---------
root=tk.Tk()
root.geometry("1200x1000")
frame=tk.Frame()
frame.master.title("SPACE MINER")
canvas=tk.Canvas(frame)
# ----------------------images------------------
air=tk.PhotoImage(file="image\Air.png")
enemy=tk.PhotoImage(file="image\enemy.png")
point=tk.PhotoImage(file="image\point.png")
img=tk.PhotoImage(file="image\space.png")
bgFirst=tk.PhotoImage(file="image\space1.png")
winSpace=tk.PhotoImage(file="image\winspace.png")
gameOver=tk.PhotoImage(file="image\gameOver.png")
winStyle=tk.PhotoImage(file="image\winStyle.png")
winGame=tk.PhotoImage(file="image\win.png")
Wall=tk.PhotoImage(file="image\wall.png")
# -----------------global Variable--------
notLost = True
isFase=True
number=0
# -----------------first window when user open and user should click to play---
canvas.create_image(650,400,image=bgFirst)
canvas.create_text(100,20,text="Space Miner",font=("Pursia",20),fill="white")
canvas.create_image(90,70,image=air)
canvas.create_text(680,650,text="Click here to Play",font=("Pursia",20),fill="black")
canvas.create_text(680,350,text="How to Play",font=("Pursia",20))
canvas.create_text(680,400,text="1.You should collect until 100 points you will win",font=("Pursia",20))
canvas.create_text(680,450,text="2.If you crash on bomb You will loses",font=("Pursia",20))
winsound .PlaySound("sound\play.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ------make grid for player can move by grid----------------
GRID=[
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
    [4,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,4],
    [4,0,0,0,4,4,4,0,0,0,0,0,4,0,4,0,0,0,0,0,4,4,4,0,0,0,4],
    [4,0,0,0,4,0,2,0,0,2,0,4,0,3,0,4,0,0,0,0,0,2,4,0,2,0,4],
    [4,0,0,0,4,0,0,0,0,2,4,0,0,0,0,2,4,0,0,0,3,0,4,0,0,2,4],
    [4,0,0,0,0,0,0,3,0,4,3,0,0,4,0,0,0,4,0,0,0,0,0,0,0,0,4],
    [4,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,2,0,4,0,0,2,3,0,0,0,4],
    [4,0,0,0,0,0,0,0,0,4,0,0,4,0,4,3,0,4,0,0,2,0,0,0,0,0,4],
    [4,2,0,0,0,0,0,0,0,3,4,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,4],
    [4,0,0,0,4,2,0,0,0,0,0,4,0,0,0,4,2,0,0,0,0,0,4,0,0,2,4],
    [4,0,0,0,4,3,0,0,0,0,0,0,4,0,4,0,0,0,0,0,0,3,4,0,0,0,4],
    [4,0,0,0,4,4,4,3,0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,0,0,0,4],
    [4,0,0,0,0,0,0,0,0,0,0,2,0,1,0,0,0,0,0,2,0,0,0,0,0,0,4],
    [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
]
# --------------------for drawgrid easy player run follow grid----------------
def drawGrid():
    global notLost, number
    canvas.create_image(600,400,image=img)
    canvas.create_text(1250,590,text="Your Score",font=("Pursia",15),fill="white")
    x2=50
    y2=50
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
# ----when player win it will display a new window-and go 100 point-
def win():
    canvas.delete("all")
    canvas.create_window(530,450,anchor="nw", window=buttonStart)
    canvas.create_window(700,450,anchor="nw", window=buttonClose)
    canvas.create_image(680,250,image=winSpace)
    canvas.create_image(680,200,image=winGame)
    canvas.create_image(680,200,image=winStyle)
    canvas.create_text(680,400,text="CONGRATULATION !",font=("Pursia",15,"bold"),fill="white")
    canvas.create_text(680,600,text=number,font=("Pursia",15),fill="white")
    canvas.create_text(680,550,text="Your Score",font=("Pursia",15),fill="white")
    winsound .PlaySound("sound\win.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ------when you touch enemy will lose and display new window--
def lose(): 
    canvas.delete("all")
    canvas.create_window(450,360,anchor="nw", window=buttonRestart)
    canvas.create_window(700,360,anchor="nw", window=buttonClose)
    canvas.create_image(700,400,image=gameOver)
    canvas.create_text(100,100,text=number,font=("Pursia",15),fill="white")
    canvas.create_text(100,50,text="Your Score",font=("Pursia",15),fill="white")
    winsound .PlaySound("sound\lose.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
#----------Use for move player and count point and conditon to display Loses---
def movePlayer(posi):
    global isFase,number
    isTrue=True
    for col in range(len(GRID)):
        for row in range(len(GRID[col])):
            # ---player can move right---
                if (posi=="Right") :
                    if  GRID[col][row]==1 and  isTrue and GRID[col][row+1]==0:
                        GRID[col][row]=0
                        GRID[col][row+1]=1
                        isTrue=False
            #--when player touch number 3 ,player will collect and count point--
                    elif  GRID[col][row]==1 and  isTrue and GRID[col][row+1]==3:
                        GRID[col][row+1]=0
                        winsound .PlaySound("sound\solid.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                        number+=10
                    #--when player met number 2 player will lose
                    elif GRID[col][row]==1 and  isTrue and GRID[col][row+1]==2:
                        isFase=False
            #---player can move left---
                if (posi=="Left"):
                    if GRID[col][row]==1 and isTrue and GRID[col][row-1]==0 and GRID[col][row-1]!=2  :
                        GRID[col][row]=0
                        GRID[col][row-1]=1
                        isTrue=False
            #--when player touch number 3 ,player will collect and count point--
                    elif GRID[col][row]==1 and isTrue and GRID[col][row-1]==3:
                        GRID[col][row-1]=0
                        winsound .PlaySound("sound\solid.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                        number+=10
                    #--when player met number 2 player will lose
                    elif GRID[col][row]==1 and  isTrue and GRID[col][row-1]==2:
                        isFase=False
            #---player can move down---
                if  (posi=="Down"):
                    if GRID[col][row]==1 and (isTrue) and GRID[col+1][row]==0:
                        GRID[col][row]=0
                        GRID[col+1][row]=1
                        isTrue=False
            #--when player touch number 3 ,player will collect and count point--
                    elif GRID[col][row]==1 and (isTrue) and GRID[col+1][row]==3:
                        GRID[col+1][row]=0
                        winsound .PlaySound("sound\solid.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                        number+=10
                    #--when player met number 2 player will lose
                    elif GRID[col][row]==1 and  isTrue and GRID[col+1][row]==2:
                        isFase=False
            #---player can move up---
                if (posi=="Up"):
                    if  GRID[col][row]==1 and (isTrue) and GRID[col-1][row]==0:
                        GRID[col][row]=0 
                        GRID[col-1][row]=1
                        isTrue=False
            #--when player touch number 3 ,player will collect and count point--
                    elif GRID[col][row]==1 and (isTrue) and GRID[col-1][row]==3:
                        GRID[col-1][row]=0
                        winsound .PlaySound("sound\solid.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
                        number+=10
                    #--when player met number 2 player will lose
                    elif GRID[col][row]==1 and  isTrue and GRID[col-1][row]==2:
                        isFase=False
    canvas.delete("all")
    conditionDrawOrLose()
# -----------------------USE CONDITION FOR KNOW IT LOSE OR DRAW --------------
def conditionDrawOrLose():
    global isFalse
    if isFase:
        drawGrid()
    else:
        lose()
# ----------------------------moveRight----------------------------
def moveRight(event):
    movePlayer("Right")
# ----------------------------moveLeft----------------------------
def moveleft(event):
    movePlayer("Left")
# # # ------------------------moveDown------------------
def moveDown(event):
    movePlayer("Down")
# # # ------------------------moveUp-------------------
def moveUp(event):
    movePlayer("Up")
# ---------------------Button play first window--------------------
def onClick():
    drawGrid()
    winsound .PlaySound("sound\spacebackground.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ------------------------button restart when game over-----------------
def restart():
    global isFase
    isFase=True
    conditionDrawOrLose()
# ---------------button start when game win-------------
def start():
    drawGrid()
# ------------------button exit when player want to leave program------------
def close():
    root.destroy()
# ---------------------button create text in first window ------------
canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
myPoint=canvas.create_text(1250,660,text="0",font=("Pursia",15),fill="white")
# ----------------------------Click for Player game------------------------
buttonPlay = tk.Button(root,text="Play",font=("Pursia",15),fg="white",bg="blue",pady=15,padx=100,command=onClick)
buttonPlay=canvas.create_window(550,250,anchor="nw", window=buttonPlay)
# --------------------click button start again when player win----------------
buttonStart =Button(root,text="Play",font=("Pursia",15),fg="white",bg="blue",pady=12,padx=50,command=start)
# ----------------click button for restart again when player loses------
buttonRestart= tk.Button(root,text="RESTART",font=("Times",14,"bold"),fg="white",bg="blue",pady=12,padx=50,command=restart)
# -----------button use close program when user want to  stop play-------------
buttonClose=Button(text="EXIT", font=("Times", 14,"bold"),fg="white",bg="blue",pady=12,padx=50,command=close)
# ------------------key event for move  player-------------    
root.bind("<Right>",moveRight)
root.bind("<Left>",moveleft)
root.bind("<Up>",moveUp)
root.bind("<Down>",moveDown)
# ----------------display window------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()