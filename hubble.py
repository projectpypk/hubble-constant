import streamlit as st
import random
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog



# ---- Developer Password ----
   # change this to your password

# ---- App Title ----
st.set_page_config(page_title="Hubble Contant 💘", page_icon="💘")
st.title("💞 Hubble contant 💞")




root=tk.Tk()
root.title("user inpute")
root.minsize(900,600)
root.maxsize(900,600)
root.configure(bg="cyan4")
data=[]
x =[]
y =[]

def open_dialog():
    global user_name
    user_name=simpledialog.askstring("User Name","Enter your name")
def submit_f():
    global df
    global x
    global y
#    x = np.array([1,2])
 #   y = np.array([3,4])
    galaxy_n = g_name.get()
    object_n = ob_name.get()
    m1 = ap_name.get()
    kline_m1 = k_name.get()
    hline_m1 = h_name.get()
    
    if galaxy_n=="":
         messagebox.showwarning("Warning","please fill the galaxy name")
    elif object_n=="":
         messagebox.showwarning("Warning","please fill the galaxy name")
    elif m1=="":
         messagebox.showwarning("Warning","please fill the galaxy name")
    elif kline_m1=="":
         messagebox.showwarning("Warning","please fill the galaxy name")
    elif hline_m1=="":
         messagebox.showwarning("Warning","please fill the galaxy name")
    else:
         messagebox.showinfo("form submitted")
         m=float(m1)
         kline_m=float(kline_m1)
         hline_m=float(hline_m1)
         M = -22
         kline_r = 3933.7
         hline_r = 3968.47
         delh = (float(hline_m)-float(hline_r))
         #print(delh)
         delk = (float(kline_m)-float(kline_r))
         #print(delk)
         p=(m-M+5)/5
         result = pow(10,p)
         distance = round(result/1000000,3)
         c = 300000
         klinev   =  c*delk/kline_r
         hlinev   =  c*delh/hline_r
         #print(klinev,hlinev)
         averagev =  round((klinev+hlinev)/2,3)
         x.append(distance)
         y.append(averagev)
         #print(x,y)
         data.append([galaxy_n,object_n,m,M,kline_m,kline_r,hline_m,hline_r,distance,averagev])
         df = pd.DataFrame(data, columns=["Galaxy name","object name","m","M","k-measurred","k-rest","h-measured","h-rest","distance","averagev"])              
         tree.insert("",tk.END,values=(galaxy_n,object_n,averagev,distance))
         g_name.delete(0,tk.END)
         ob_name.delete(0,tk.END)
         ap_name.delete(0,tk.END)
         h_name.delete(0,tk.END)
         k_name.delete(0,tk.END)
         button1.config(state="normal")
         button2.config(state="normal")
#print(df)     
def plot_f():
    slope, intercept = np.polyfit(df['distance'],df['averagev'],1)
    df['y_fit'] = slope*df['distance']+intercept
    plt.scatter(x,y,color='red',label='data ponit')
    plt.plot(x,df['y_fit'],color='blue',label='data')
    plt.legend()
    plt.xlabel('Distance in Mpc')
    plt.ylabel('Velocity in km/sec')
    plt.title('hubbel constant')
    plt.show()

def hubbel_f():
    velocity_av= sum(y)/len(y)
    distance_av=sum(x)/len(x)
    H =round(velocity_av/distance_av,2)
    c = (3.171/3.241)*pow(10,12)
    life_uni=round(1/H*c,2)
    hubbel=tk.Label(root,font=("Arial",16),text=H,fg="black",bg="white")
    hubbel.place(y=500,x=670)
    life_u=tk.Label(root,font=("Arial",16),text=life_uni,fg="black",bg="white")
    life_u.place(y=500,x=430)
open_dialog()

num1 = tk.DoubleVar()
num2 = tk.DoubleVar()
num3 = tk.DoubleVar()
num4 = tk.StringVar()
num5 = tk.StringVar()
fram=tk.Frame(root,bd=5,bg="lightblue",relief="sunken",height=60)
tk.Label(fram,text='Hubble constant',font=("Impact",30,"bold"),bg="lightblue",fg='black').pack(pady=10,padx=20)
fram.pack(pady=10,fill="x")
frame=tk.Frame(root,relief="sunken", bg="cyan4")
label=tk.Label(frame,text="galaxy name", font=("Arial",16),relief='flat',bd=0,bg='cyan4')
label.grid(row=0,column=0,padx=10,pady=10)
g_name=tk.Entry(frame,textvariable=num4,font=("Arial,14"),relief="sunken",bd=2)
g_name.grid(row=0,column=1,padx=10)
tk.Label(frame,text="object name", font=("Arial",16),relief='flat',bd=0,bg='cyan4').grid(row=1,column=0,padx=10,pady=10)
ob_name=tk.Entry(frame,font=("Arial,14"),textvariable=num5,relief="sunken",bd=2)
ob_name.grid(row=1,column=1)
tk.Label(frame,text="apparent magn", font=("Arial",16),relief='flat',bd=0,bg='cyan4').grid(row=2,column=0,padx=10,pady=10)
ap_name=tk.Entry(frame,font=("Arial,14"),relief="sunken",bd=2)
ap_name.grid(row=2,column=1)
tk.Label(frame,text="k-line M", font=("Arial",16),relief='flat',bd=0,bg='cyan4').grid(row=3,column=0,padx=10,pady=10)
k_name=tk.Entry(frame,font=("Arial,14"),relief="sunken",bd=2)
k_name.grid(row=3,column=1)
tk.Label(frame,text="h-line M", font=("Arial",16),relief='flat',bd=0,bg='cyan4').grid(row=4,column=0,padx=10,pady=10)
h_name=tk.Entry(frame,font=("Arial,14"),relief="sunken",bd=2)
h_name.grid(row=4,column=1)
tree = ttk.Treeview(frame,columns=("gname","obname","name","age"),show="headings",height=270)
tree.place(y=10,x=440)
tree.heading("gname",text="Galaxy")
tree.heading("obname",text="Object")
tree.heading("name",text="average velocity")
tree.heading("age",text="Distance")
tree.column("gname",width=110)
tree.column("obname",width=110)
tree.column("name",width=110)
tree.column("age",width=110)
button=tk.Button(frame,text="Submit",command=submit_f,relief="flat",bd=0,bg='cyan4',cursor='hand2')
button.place(y=270,x=220)
button1=tk.Button(root,text='Plot',font=("Arial",14),state="disabled",command=plot_f,relief="sunken",bd=2,bg='cyan2',cursor='hand2')
button1.place(y=500,x=20)
button2=tk.Button(root,text='Hubble constant',font=("Arial",14),command=hubbel_f,state="disabled",relief="sunken",bd=2,bg='cyan2',cursor='hand2')
button2.place(y=500,x=100)
frame.pack(pady=5,fill="x",ipadx=10,ipady=40)
tk.Label(root,font=("Arial",12),text="Hubble Constant",bd=0,bg="cyan4").place(x=660,y=450)
tk.Label(root,font=("Arial",12),text="Age of Universe",bd=0,bg="cyan4").place(x=430,y=450)
        
#df = pd.DataFrame(data, columns=["Galaxy name","object name","abs magnitude","appr magnitude","K-line(m)","K-line(r)","H-line(m)","H-line(r)","distance(Mpc)","k-line V","h-line v","average v"])
#print(df)

if not len(tree.get_children())==0:
    df.to_csv(f'{user_name}.csv',index=False)
    
root.mainloop()
