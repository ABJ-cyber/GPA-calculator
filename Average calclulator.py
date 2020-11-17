__author__ = 'Joe'

from tkinter import *
from tkinter import Tk, StringVar, ttk

Root = Tk()
Root.title("Average calculator")

Left=Frame(Root,width=300,height=300)
Left.pack(side="left")

Right=Frame(Root,width=300,height=300)
Right.pack(side="right")

value0 = StringVar()
convert = DoubleVar()
Distance = DoubleVar()

mainmenu=Menu(Root)
Root.config(menu=mainmenu)

filemenu=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="File")

label1=Label(Left,text="Score",font=("arial",30,"bold","italic"),relief="raised",bd=4,width=9,bg="darkslategray",fg="black")
label1.grid(row=0,column=-0)

label2=Label(Right,text="Credit Hours",font=("arial",15,"bold","italic"),relief="raised",bd=4,width=12,height=2,bg="darkslategray",fg="black")
label2.grid(row=0,column=1)

Entry10=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry10.grid(row=1,column=0,sticky=W)
Entry11=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry11.grid(row=2,column=0,sticky=W)
Entry12=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry12.grid(row=3,column=0,sticky=W)
Entry13=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry13.grid(row=4,column=0,sticky=W)
Entry14=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry14.grid(row=5,column=0,sticky=W)
Entry15=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry15.grid(row=6,column=0,sticky=W)
Entry16=Entry(Left,textvariable=convert,relief="sunken",font=("arial",15),bd=2,bg="grey")
Entry16.grid(row=7,column=0,sticky=W)

Entry20=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry20.grid(row=1,column=1,sticky=E)
Entry21=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry21.grid(row=2,column=1,sticky=E)
Entry22=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry22.grid(row=3,column=1,sticky=E)
Entry23=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry23.grid(row=4,column=1,sticky=E)
Entry24=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry24.grid(row=5,column=1,sticky=E)
Entry25=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry25.grid(row=6,column=1,sticky=E)
Entry26=Entry(Right,textvariable=convert,relief="sunken",font=("arial",15),bd=2,width=13,bg="grey")
Entry26.grid(row=7,column=1,sticky=E)





Root.mainloop()
