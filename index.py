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
img=tk.PhotoImage(file="image\space.png")
# --------------add sound background-----------
# winsound .PlaySound("sound\spacebackground.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
# ------------------------grid constants----------------
GRID=[
    [0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,3,0],
    [0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,3,0,0,0,0,0,3,0,0,0,3,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,3,0,3,0,0,0,0,0,0,0,0,3,0,3,0,0,0,0,3,0,0,0,0,0],
    [0,2,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,3,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,3,0,0,0,0,3,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0]
]

# ---------------------function showCrystals----------------
air=tk.PhotoImage(file="image\Air.png")
enemy=tk.PhotoImage(file="image\enemy.png")
point=tk.PhotoImage(file="image\point.png")
bgFirst=tk.PhotoImage(file="image\space1.png")
notLost = True
number=0
def box():
    canvas.create_image(400,400,image=img)
    x2=50
    y2=50
    global notLost, number
    if notLost and number <10 :
        for col in GRID:
            for row in col:
                if row==1:
                    canvas.create_image(x2-25,y2-25,image=air)
                elif row==2:
                    canvas.create_image(x2-25,y2-25,image=enemy)
                    # canvas.moveto(x2)
                elif row==3:
                    canvas.create_image(x2-25,y2-25,image=point)
                x2+=50
            x2=50
            y2+=50
    elif number == 10:
        win()
    else:
        lose()
def bg():
    canvas.create_text(100,20,text="Space Miner",font=("Pursia",20),fill="white")
    canvas.create_text(680,650,text="Click here to Play",font=("Pursia",20),fill="white")
    canvas.create_image(650,400,image=bgFirst)
bg()
# ---------------------Button--------------------
def onClick():
    box()
    buttonPlay.pack_forget()
buttonPlay = tk.Button(root,text="Play",font=("Pursia",15),fg="white",bg="blue",pady=15,padx=100,command=onClick)
buttonPlay.config(width=7, height=1, bg="#007EE9",fg="yellow",border="2",rounded="2", font=("Arial", 20, "bold"))
buttonPlay=canvas.create_window(500,250,anchor="nw", window=buttonPlay)

# ------------------------countPoint When airplane crash Crystal------
canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
myPoint=canvas.create_text(1250,660,text="0",font=("Pursia",15),fill="white")
def countPoints():
    global number,myPoint
    if number<10:
        number+=1
        winsound .PlaySound("sound\solid.wav",winsound.SND_FILENAME | winsound.SND_ASYNC)
    else:
        canvas.delete("all")
        canvas.create_image(400,400,image=img)
        canvas.create_text(1250,660,text=number,font=("Pursia",15),fill="white")
        canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
# ---------------------For display Win or Lose-------------
def win():
    canvas.delete("all")
    canvas.create_image(400,400,image=img)
    canvas.create_text(650,350,text="You Win !",font=("Pursia",45),fill="white")
    canvas.create_text(650,450,text="congratulations",font=("Pursia",15),fill="white")
    buttonPlay = tk.Button(root,text="start",font=("Pursia",15),fg="white",bg="blue",pady=15,padx=15,command=onClick,tags="PNC")
    buttonPlay.config(width=7, height=1, bg="#007EE9",fg="yellow",border="2", font=("Arial", 20, "bold"))
    buttonPlay=canvas.create_window(520,500,anchor="nw", window=buttonPlay)
    buttonPlay = tk.Button(root,text="cancel",font=("Pursia",15),fg="white",bg="blue",pady=15,padx=15,command=onClick)
    buttonPlay.config(width=7, height=1, bg="#007EE9",fg="yellow",border="2", font=("Arial", 20, "bold"))
    buttonPlay=canvas.create_window(700,500,anchor="nw", window=buttonPlay)

def lose():  
    canvas.delete("all")
    canvas.create_image(400,400,image=img)
    canvas.create_text(650,350,text="You Lose!",font=("Pursia",45),fill="white")
# --------------------------------Button Play Again-------------------
# def onClick():

# ---------------------------moveright----------------
def moveRight(event):
    global GRID
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
    box()
root.bind("<Right>",moveRight)
    # ----------------------------moveLeft----------------------------
def moveleft(event):
    global GRID
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
    box()
root.bind("<Left>",moveleft)
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
            elif (GRID[col][row]==1) and (GRID[col-1][row]==2) and not isDown:
                lose()
                isDown=False
                canvas.destroy("all")
    box()
root.bind("<Down>",moveDown)
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
                isUp=True
                canvas.destroy("all")
    # print(isUp)
    box() 
root.bind("<Up>",moveUp)
# ----------------display------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()