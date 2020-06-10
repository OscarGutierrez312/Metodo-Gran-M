# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import tkinter as tk

import numpy as np

raiz=tk.Tk()
raiz.title("Método de la Gran M")
raiz.geometry("600x500")



frame1=Frame(raiz, width=600, height=500)
frame1.pack(fill='both', expand=1)

frame2=Frame(raiz, width=600, height=500)
frame3=Frame(raiz, width=600, height=500)

Lbl1=tk.Label(frame1, text="Metodo de la Gran M")
Lbl1.config(font=("Helvetica",24))
Lbl1.grid(pady=5,row=0,column=0, columnspan=2)

Lblm=tk.Label(frame1, text="", height=7)
Lblm.grid(pady=5,row=1,column=1)


Lbl1_1=tk.Label(frame1, text="Numero de Variables")
Lbl1_1.config(font=("Helvetica",15))
Lbl1_1.grid(pady=5,row=2,column=0)


Txt1=tk.Text(frame1, height=1.5, width=30)
Txt1.config(font=("Helvetica",15))
Txt1.grid(pady=5,row=2,column=1)


Lbl1_2=tk.Label(frame1, text="Numero de Restricciones")
Lbl1_2.config(font=("Helvetica",15))
Lbl1_2.grid(pady=1,row=3,column=0)


Txt1_1=tk.Text(frame1, height=1.5, width=30)
Txt1_1.config(font=("Helvetica",15))
Txt1_1.grid(pady=1,row=3,column=1)

    
def cambiar():
    frm2()
    frame1.pack_forget()
    frame2.pack()
    
def ejecucion(funcion, restr, NF, NR):
       
    frame2.pack_forget()
    frame3.pack()
           
    A=0
    H=0
    HN=0
    for i in range(NR):
        r=restr.get('r'+str(i)).get()
        if(r == '>='):
            A+=1
            HN+=1
        if(r == '='):
            A+=1
            
        if(r == '<='):
            H+=1
            
    x=NF+A+H+HN
    y=NR+2
    
    matriz=np.zeros((y,x+1))
    
    cont=0
        
    for i in range (NR):
        for j in range (x):
            if(j<NF):
                n=restr.get(cont).get("1.0","end")
                matriz[i][j]=int(n)
                cont+=1
            
            matriz[i][NF+1]=1
             
            matriz[i][x]=restr.get('b'+str(i)).get("1.0","end")
    
    matriz[1][3]=-1
    matriz[1][4]=0
    matriz[1][5]=1
    
    M=10000000
    Col=0
    Fil=0
    
    Coef=[]
    
    Var=['X1', 'X2', 'X3', 'H2', 'H1','b']
    Oper=['Cj','VB',Var[2],Var[1],'Z', 'Cj-Zj']
    
    for i in range(NF):
        Coef.append(int(funcion.get(i).get("1.0","end")))
    Coef.append(0)
    Coef.append(0)
    Coef.append(-M)
        
    matriz[1]=matriz[1]/4
    
    matriz[0]=(matriz[1]*-1)+matriz[0]
    
    matriz[0]=matriz[0]/0.5
    
    matriz[1]=(matriz[0]*-0.5)+matriz[1]
    
    matriz[2]=(matriz[0]*Coef[2])+(matriz[1]*Coef[1])
    
    Coef.append(0)
    
    matriz[3]=Coef-matriz[2]
    
    print(matriz)
    
    Lbl3=tk.Label(frame3, text="Metodo de la Gran M Solución")
    Lbl3.config(font=("Helvetica",24))
    Lbl3.grid(pady=5,row=0,column=0, columnspan=x+2)
    
    
    
    for i in range(y+2):
       
        for j in range(x+1):
            Txt3_1=tk.Entry(frame3, width=5)
            Txt3_1.config(font=("Helvetica",15))
            Txt3_1.grid(row=i+1,column=j)
            if(i>1 and j>0 and j!=(x)):
                Txt3_1.insert(0,matriz[i-2][j-1])  
            if(i>1 and j==x):
                Txt3_1.insert(0,matriz[i-2][j])
            if(j==0):
                Txt3_1.insert(0,Oper[i])
            if(i==1 and j>0):
                Txt3_1.insert(0,Var[j-1])
            if(i==0 and j>0 and j<(x)):
                Txt3_1.insert(0,Coef[j-1])
            
   
    for i in range(1,NF):
        
        Lbl3_1=tk.Label(frame3, text="X"+str(i)+"=")
        Lbl3_1.config(font=("Helvetica",24))
        Lbl3_1.grid(pady=5,row=i+8,column=0, columnspan=2)

        Lbl3_2=tk.Label(frame3, text=matriz[i-1][x])
        Lbl3_2.config(font=("Helvetica",24))
        Lbl3_2.grid(pady=5,row=i+8,column=1, columnspan=2)
        
    Lbl3_1=tk.Label(frame3, text="X"+str(3)+"=")
    Lbl3_1.config(font=("Helvetica",24))
    Lbl3_1.grid(pady=5,row=11,column=0, columnspan=2)

    Lbl3_2=tk.Label(frame3, text=matriz[0][x])
    Lbl3_2.config(font=("Helvetica",24))
    Lbl3_2.grid(pady=5,row=11,column=1, columnspan=2)
        
   
    Lbl3_4=tk.Label(frame3, text="Z=")
    Lbl3_4.config(font=("Helvetica",24))
    Lbl3_4.grid(pady=5,row=9,column=3, columnspan=2)
    
    Lbl3_3=tk.Label(frame3, text=matriz[1][x]*Coef[1])
    Lbl3_3.config(font=("Helvetica",24))
    Lbl3_3.grid(pady=5,row=9,column=4, columnspan=2)

   
def frm2():
    N_Var=Txt1.get("1.0","end")
    N_Res=Txt1_1.get("1.0","end")
    
    N_Var=int(N_Var)
    N_Res=int(N_Res)
    
    Lbl2=tk.Label(frame2, text="Metodo de la Gran M")
    Lbl2.config(font=("Helvetica",24))
    Lbl2.grid(pady=5,row=0,column=0, columnspan=int(N_Var)+1)

    Lbl2_1=tk.Label(frame2, text="Función Objetivo")
    Lbl2_1.config(font=("Helvetica",14))
    Lbl2_1.grid(pady=5,row=1,column=0)
    
    Fun_Obj={}
    
    for i in range (int(N_Var)):
                
        Fun_Obj.setdefault(i,tk.Text(frame2, height=1, width=3))
        Fun_Obj.setdefault(i).config(font=("Helvetica",14))
        Fun_Obj.setdefault(i).grid(pady=5,row=1,column=i+1)
        
        
        
    Lbl2_2=tk.Label(frame2, text="Restricciones:")
    Lbl2_2.config(font=("Helvetica",14))
    Lbl2_2.grid(pady=5,row=2,column=0)
    
    Rest={}
    cont=0
    for i in range (int(N_Res)):
        
        for j in range(int (N_Var)):
                    
            Txt3=tk.Text(frame2, height=1, width=3)
            Txt3.config(font=("Helvetica",14))
            Txt3.grid(pady=5,row=i+3,column=j+1)
            Rest.setdefault(cont, Txt3)
            cont+=1
        
        des=ttk.Combobox(frame2, width=3)
        des['values']=('>=', '=', '<=')
        des.grid(pady=5,row=i+3, column=int(N_Var)+1)
        Rest.setdefault('r'+str(i),des)
        
        Txt4_i=tk.Text(frame2, height=1, width=3)
        Txt4_i.config(font=("Helvetica",14))
        Txt4_i.grid(pady=5,row=i+3,column=int(N_Var)+2)
        Rest.setdefault('b'+str(i),Txt4_i)
      

        
    Btn2=tk.Button(frame2, text="Continuar", width=60, command=lambda: ejecucion(Fun_Obj, Rest,N_Var, N_Res))
    Btn2.grid(padx=1,pady=5,row=int(N_Res)+3,column=0, columnspan=int(N_Var)+1)
    
    
         
Btn1=tk.Button(frame1, text="Aceptar", width=60,command=cambiar)
Btn1.grid(padx=1,pady=5,row=4,column=0, columnspan=2)


raiz.mainloop()

