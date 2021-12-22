from random import randbytes, randrange
import tkinter as tk
from tkinter import Button, Image, Label, constants
from tkinter import font
from typing import Text
root=tk.Tk()
root.geometry("2000x1000")
frame=tk.Frame()
frame.master.title("SPACE MINER")
canvas=tk.Canvas(frame)
img=tk.PhotoImage(file="image\space.png")
canvas.create_image(400,400,image=img)
# ------------------------grid constants----------------
GRID=[
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,3,0],
    [0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0],
    [0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0],
    [0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0],
    [0,2,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,2,0,0,0,0,0,0,0,0]
]

# ---------------------function showCrystals----------------
air=tk.PhotoImage(file="image\Air.png")
enemy=tk.PhotoImage(file="image\enemy.png")
point=tk.PhotoImage(file="image\point.png")

def box():
    x1=0
    x2=50
    y1=0
    y2=50
    for col in GRID:
        for row in col:
            if row==1:
                canvas.create_image(x2-25,y2-25,image=air)
            elif row==2:
                canvas.create_image(x2-25,y2-25,image=enemy)
            elif row==3:
                canvas.create_image(x2-25,y2-25,image=point)
            # else:
            #     canvas.create_rectangle(x1,y1,x2,y2,fill="white")
            x1=x2
            x2+=50
        x1=0
        x2=50
        y1=y2
        y2+=50
box()
# ------------------------countPoint When airplane crash Crystal------
number=0
canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
myPoint=canvas.create_text(1250,660,text="0",font=("Pursia",15),fill="white")
def countPoints():
    global number,myPoint
    if number<10 :
        number+=1
    else:
        canvas.delete("all")
        canvas.create_image(400,400,image=img)
        canvas.create_text(1250,660,text=number,font=("Pursia",15),fill="white")
        canvas.create_text(1250,630,text="Your Score",font=("Pursia",15),fill="white")
# ---------------------For display Win or Lose-------------
# def 
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
            elif (GRID[col][row]==1) and (not isRight) and (GRID[col][row+1])==3:
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
            if GRID[col][row]==1 and not isLeft and GRID[col][row-1]==0:
                GRID[col][row]=0
                GRID[col][row-1]=1
                isRight=True
            elif (GRID[col][row]==1) and (not isLeft) and (GRID[col][row-1]==3):
                GRID[col][row]=0 
                GRID[col][row-1]=1
                countPoints()
                isLeft=True
    box()
root.bind("<Left>",moveleft)
# # --------------------moveDown------------------
def moveDown(event):
    global GRID
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
    box()
root.bind("<Down>",moveDown)
# # -------------------------------------moveUp-------------------
def moveUp(event):
    global GRID,result
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
            elif (GRID[col][row]==1) and (not isUp) and (GRID[col-1][row]==3):
                GRID[col][row]=0 
                GRID[col-1][row]=1
                countPoints()
                isUp=True
            elif (GRID[col][row]==1) and (not isUp) and (GRID[col-1][row]==2) (GRID[col-1][row]!=3) and number==10:
                GRID[col][row]=0 
                GRID[col-1][row]=1
                isUp=True
    # print(isUp)
    box()
root.bind("<Up>",moveUp)

# ------------------------------move enemy--------------
# def onClick():
#     box()
#     buttonPlay.pack_forget()
# buttonPlay = tk.Button(root,text="Play",command=onClick)
# buttonPlay.pack(expand=True,fill="both")
# ----------------display------------
canvas.pack(expand=True,fill="both")
frame.pack(expand=True,fill="both")
root.mainloop()