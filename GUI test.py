from tkinter import *
import tkinter as tk
import os
import pickle
from datetime import date, timedelta


add=0
daylist=[]
setlist=[]
butlist=[]
definlist=[]
tlist=[]

root = Tk()
root.geometry("300x300")
root.title("Habit tracker")

def count(lista):
    
    if not lista[0]==lista[1]: 
      
        if  lista[0]==lista[1]+timedelta(days=1):
                lista[2]=lista[2]+1

        elif lista[0]<lista[1]:
              lista[2]=0

    else:
        lista[2]=1
      
    lista[1]=lista[0]

    return lista

def enter():
    global enterbut, tbox, add, refin
    
    if enterbut.winfo_exists and tbox.get().replace(" ", "")!="":

        tlist.append(None)
        tlist[add]=tbox.get()
        
        save(tlist[add],f"tlist[{add}].txt")

        enterbut.destroy()   
        tbox.destroy()
        refin.destroy()
        
        adbit.config(state=NORMAL)   
        
        tbox = Entry(root, width=10)
        enterbut=Button(root, text="Enter", command=enter)
        refin = Label(root, text="Enter a habit")


        but=Button(root, text=f"{tlist[add]}", command=lambda add=add: click(add))
        but.pack(side=TOP)
        butlist.append(but)

        add+=1
        save(add,"add.txt")

    if add>=6:
        adbit.config(state=DISABLED)
    if add>0:
        subbot.config(state=NORMAL)
    

def save(g, fname):
    
    with open(fname, "wb") as gman:
        pickle.dump(g,gman)
    return g
def load(g, fname):
    
    with open(fname, "rb") as gman:
        g = pickle.load(gman)   
    return g

def plus():
    global add

    setlist.append(0)
    daylist.append(date.today()) 

    tbox.pack(side=BOTTOM)
    refin.pack(side=BOTTOM)
    enterbut.pack(side=RIGHT)
    if enterbut.winfo_exists:
        adbit.config(state=DISABLED)

def sub():
    global add

    if butlist[-1]["state"]==DISABLED:
        definlist[-1].destroy()
        definlist.pop(-1)
    else:
        pass
    butlist[-1].destroy()
    butlist.pop(-1)
    setlist.pop(-1)
    daylist.pop(-1)

    add-=1
    save(add, "add.txt")
    if add<6:
        adbit.config(state=NORMAL)
    if add<=0:
        subbot.config(state=DISABLED)

def click(i):
    if os.path.exists(f"setlist[{i}].txt"):
        setlist[i]=load(setlist[i], f"setlist[{i}].txt")
    if os.path.exists(f"daylist[{i}].txt"):
        daylist[i]=load(daylist[i], f"daylist[{i}].txt")
    
    info=[date.today()+timedelta(days=5),daylist[i],setlist[i]]
    
    info=count(info)
    
    setlist[i], daylist[i]=info[2], info[1]

    defin = Label(root, text=f"Días de racha {i}: {setlist[i]}")
    defin.pack(side=TOP)
    definlist.append(defin)
    
    butlist[i].config(state=DISABLED)  
    save(setlist[i],f"setlist[{i}].txt")
    save(daylist[i],f"daylist[{i}].txt")

if os.path.exists("add.txt"):
    add=load(add, "add.txt")

for i in range(add):
    tlist.append(f"Botón{i}")
    if os.path.exists(f"tlist[{i}].txt"):
        tlist[i]=load(tlist[i],f"tlist[{i}].txt")
        
    but=Button(root, text=f"{tlist[i]}", command=lambda i=i: click(i))
    but.pack(side=TOP)
    
    butlist.append(but)
    setlist.append(0)
    daylist.append(date.today())

subbot=Button(root, text="-", command=sub)
subbot.pack(side=BOTTOM)

adbit=Button(root, text="+", command=plus)
adbit.pack(side=BOTTOM)

if add==0:
    subbot.config(state=DISABLED)

tbox = Entry(root, width=10)
enterbut=Button(root, text="Enter", command=enter)
refin = Label(root, text="Ingresa un hábito")

root.mainloop()