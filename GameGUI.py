# -*- coding: utf-8 -*-
"""
Created on Wed May  6 16:32:05 2022

@author: carlosAguilar
"""
import random
from tkinter import *
import tkinter as tk
import serial
window = Tk()
#if you m¿want use an arduino only uncomment the line 13, 30, 36, 39,  202 
#arduino = serial.Serial('COM3')


def ganador():
        global p
        global bot
        global j
        global c
        global k
        if j%3==0:
            window.deiconify()
            win=tk.Toplevel()
            win.title("Resultado")
            win.geometry('300x200')
            if (p>bot):
                answer_5=Label (win,image= player_round,      width=300        ,height=200,bg=color,border=0).grid(row=1,column=3,columnspan=1)
                c=c+1
                #led_on()   
                input_text.set(c)
            if (p<bot):
                answer_5=Label (win,image= bot_round,         width=300        ,height=200,bg=color,border=0).grid(row=1,column=3,columnspan=1)
                k=k+1
                input_text2.set(k)
                #led_on_2()
            if (p==bot):
                answer_5=Label (win,image= tie_round,              width=300        ,height=200,bg=color,border=0).grid(row=1,column=3,columnspan=1)
                #led_on_3()
            p=0
            bot=0
def led_on():
    arduino.write(b'0') 
def led_on_2():
    arduino.write(b'1') 
def led_on_3():
    arduino.write(b'2')         
def choose(n):
    if n==1:
       print("             Rock") 
    if n==2:
       print("             Paper") 
    if n==3:
       print("             Scissors")
def rockprint():
     global p
     global bot
     global j
     answer_2=   Label (window,image= rockx2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=1,columnspan=1,rowspan=1)
     b=random.randint(1, 3)
     if b==1:
         answer_3=   Label (window,image= rock2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= tie,              width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         j=j+1
         ganador()
     if b==2:
         answer_2=   Label (window,image= paper2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= bot_wins,         width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         bot=bot+1
         j=j+1
         ganador()
     if b==3:
         answer_3=   Label (window,image= scissors2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= player_wins,      width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         p=p+1
         j=j+1
         ganador()
def scissorsprint():
     global p
     global bot
     global j
     answer_2=   Label (window,image= scissorsx2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=1,columnspan=1,rowspan=1)
     b=random.randint(1, 3)
     if b==1:
         answer_3=   Label (window,image= rock2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= bot_wins,         width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         bot=bot+1
         j=j+1
         ganador() 
     if b==2:
         answer_3=   Label (window,image= paper2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= player_wins,      width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         p=p+1
         j=j+1
         ganador()
     if b==3:
         answer_3=   Label (window,image= scissors2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1) 
         answer_5=Label (window,image= tie,              width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         j=j+1
         ganador()
def paperprint():
     global p
     global bot
     global j
     answer_2=   Label (window,image= paperx2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=1,columnspan=1,rowspan=1)
     a=3
     b=random.randint(1, 3)
     if b==1:
         answer_3=   Label (window,image= rock2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= player_wins,      width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         j=j+1
         p=p+1
         ganador()
     if b==2:
         answer_3=   Label (window,image= paper2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= tie,              width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         j=j+1
         ganador()
     if b==3:
         answer_3=   Label (window,image= scissors2x2,      width=200        ,height=200,bg=color,border=0).grid(row=2,column=7,columnspan=1,rowspan=1)
         answer_5=Label (window,image= bot_wins,         width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
         j=j+1
         bot=bot+1
         ganador()
window.title("Game Aguilar Carlos")
window.geometry("1150x700") # size
window.resizable(False, False) # No modificable
#declaracion de las imagenes

menu=       PhotoImage(master=window,file="Extra/white.gif")
#player 
rock_1=     PhotoImage(master=window,file="Player/rock1.gif")
paper_1=    PhotoImage(master=window,file="Player/paper.gif")
scissors_1= PhotoImage(master=window,file="Player/scissors.gif")
#pc
rock_2=     PhotoImage(master=window,file="Pc/rock2.gif")
paper_2=    PhotoImage(master=window,file="Pc/paper2.gif")
scissors_2= PhotoImage(master=window,file="Pc/scissors2.gif")
VS=         PhotoImage(master=window,file="Extra/VS.gif")
out=        PhotoImage(master=window,file="Extra/out.gif")
player=     PhotoImage(master=window,file="Player/player.gif")
pc=         PhotoImage(master=window,file="Pc/pc.gif")
score=      PhotoImage(master=window,file="Extra/score.gif")
answer=     PhotoImage(master=window,file="Extra/answer.gif")
#answers
rockx2=     PhotoImage(master=window,file="Player/Answers/rockx2.gif")
paperx2=    PhotoImage(master=window,file="Player/Answers/paperx2.gif")
scissorsx2= PhotoImage(master=window,file="Player/Answers/scissorsx2.gif")
rock2x2=    PhotoImage(master=window,file="Pc/Answers/rock2x2.gif")
paper2x2=   PhotoImage(master=window,file="Pc/Answers/paper2x2.gif")
scissors2x2=PhotoImage(master=window,file="Pc/Answers/scissors2x2.gif")
#victorias
player_wins=     PhotoImage(master=window,file="Win/Set/player_wins.gif")
bot_wins=    PhotoImage(master=window,file="Win/Set/bot_wins.gif")
tie= PhotoImage(master=window,file="Win/Set/tie.gif")
player_round=     PhotoImage(master=window,file="Win/Round/player_round.gif")
bot_round=    PhotoImage(master=window,file="Win/Round/bot_round.gif")
tie_round= PhotoImage(master=window,file="Win/Round/tie_round.gif")
#fondo usado para el menu
lbl1= Label(window,image = menu).grid(row=0,column=0,columnspan=11,rowspan=6)
ancho_boton=100
alto_boton=100
color="white"
#score
expression=0
input_text = IntVar()
input_text2 = IntVar()
Pantalla=   Entry(window,    font=("arial",50,"bold"), textvariable = input_text,width=2,          bg=color,border=0).grid(row=0,column=2)
#respuesta
answer_1=   Label (window,image= answer,      width=200        ,height=alto_boton,bg=color,border=0).grid(row=2,column=1,columnspan=1)
answer_1=   Label (window,image= answer,      width=200        ,height=alto_boton,bg=color,border=0).grid(row=2,column=1,columnspan=6)
answer_5=   Label (window,image= answer,      width=300        ,height=100,bg=color,border=0).grid(row=1,column=3,columnspan=3)
#player:
lbl3=       Label (window,image= player,     width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=0,column=0)
#score player
lbl_score=  Label (window,image= score,      width=200        ,height=alto_boton,bg=color,border=0).grid(row=0,column=1,columnspan=1)
#pc:
lbl4=       Label (window,image= pc,         width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=0,column=6)
lbl_score=  Label (window,image= score,      width=200        ,height=alto_boton,bg=color,border=0).grid(row=0,column=7,columnspan=1)
Pantalla_2= Entry(window,    font=("arial",50,"bold"),textvariable = input_text2,         width=2          ,bg=color,border=0).grid(row=0,column=8)
space=      Label (window,image= menu,       width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=9)#espacio
space=      Label (window,image= menu,       width=50,         height=alto_boton,bg=color,border=0).grid(row=5,column=10)#espacio
#boton player 1
rock1 =     Button(window,image= rock_1,     width=ancho_boton,height=alto_boton,bg=color,border=0,command=rockprint).grid(row=5,column=0)
paper1 =    Button(window,image= paper_1,    width=ancho_boton,height=alto_boton,bg=color,border=0,command=paperprint).grid(row=5,column=1)
scissors1 = Button(window,image= scissors_1, width=ancho_boton,height=alto_boton,bg=color,border=0,command=scissorsprint).grid(row=5,column=2)
#boton bot
rock2 =     Button(window,image= rock_2,     width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=6)
paper2 =    Button(window,image= paper_2,    width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=7)
scissors2 = Button(window,image= scissors_2, width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=8)
space=      Label (window,image= menu,       width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=9)#espacio
space=      Label (window,image= menu,       width=50,         height=alto_boton,bg=color,border=0).grid(row=5,column=10)#espacio
#VS
lbl2=       Label (window,image= VS,         width=300        ,height=300       ,bg=color,border=0).grid(row=2,column=3,columnspan=3,rowspan=3)
#out
space=      Label (window,image= menu,       width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=3)#espacio
Boton_out = Button(window,image= out,        width=ancho_boton,height=alto_boton,bg=color,border=0,command=window.destroy).grid(row=5,column=4)
space=      Label (window,image= menu,       width=ancho_boton,height=alto_boton,bg=color,border=0).grid(row=5,column=5)#espacio
p=0
bot=0
j=0
c=0
k=0
window.mainloop()
#arduino.close()