# -*- coding: utf-8 -*-

# =============================================================================
# Se importa las librerias de tkinter(Interfaz) y numpy (Algoritmo)
# =============================================================================
from tkinter import *
from tkinter import ttk
import tkinter as tk

import numpy as np

# =============================================================================
# Creación Ventana Principal
# =============================================================================
raiz=tk.Tk()
raiz.title("Método de la Gran M")
raiz.geometry("800x500")

# =============================================================================
# Creación de Frames Utilizados en la ejecución de la aplicación
# =============================================================================

frame1=Frame(raiz, width=800, height=500)
frame1.pack(fill='both', expand=1)
frame2=Frame(raiz, width=800, height=500)
frame3=Frame(raiz, width=800, height=500)
newFrame=Frame(raiz, width=800, height=500)



def main():
    frm1()
    
    
# =============================================================================
#   Creación de elementos del Frame 1 (Ventana Inicial)
# =============================================================================
def frm1():
    
    Lbl1=tk.Label(frame1, text="Metodo de la Gran M")
    Lbl1.config(font=("Helvetica",24))
    Lbl1.grid(pady=5,row=0,column=0, columnspan=2)
    
    Lblm=tk.Label(frame1, text="", height=7)
    Lblm.grid(pady=5,row=1,column=1)
    
    Lbl1_=tk.Label(frame1, text="Tipo de Optimización:")
    Lbl1_.config(font=("Helvetica",15))
    Lbl1_.grid(pady=5,row=2,column=0)
    
    des=ttk.Combobox(frame1, width=30)
    des['values']=('Maximizar', 'Minimizar')
    des.grid(pady=5,row=2, column=1)
    
    Lbl1_1=tk.Label(frame1, text="Numero de Variables")
    Lbl1_1.config(font=("Helvetica",15))
    Lbl1_1.grid(pady=5,row=3,column=0)
    
    
    Txt1=tk.Text(frame1, height=1.5, width=30)
    Txt1.config(font=("Helvetica",15))
    Txt1.grid(pady=5,row=3,column=1)
    
    
    Lbl1_2=tk.Label(frame1, text="Numero de Restricciones")
    Lbl1_2.config(font=("Helvetica",15))
    Lbl1_2.grid(pady=1,row=4,column=0)
    
    
    Txt1_1=tk.Text(frame1, height=1.5, width=30)
    Txt1_1.config(font=("Helvetica",15))
    Txt1_1.grid(pady=1,row=4,column=1)

    Btn1=tk.Button(frame1, text="Aceptar", width=60,command=lambda: frm2(des.get(),Txt1.get("1.0","end"),Txt1_1.get("1.0","end")))
    Btn1.grid(padx=1,pady=5,row=5,column=0, columnspan=2)
    
def frm2(tipo, N_Var, N_Res):
    
    frame1.pack_forget()
    frame2.pack()
    
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
    
    paso=1
    
    Btn2=tk.Button(frame2, text="Continuar", width=60, command=lambda: ejecutar(tipo, Fun_Obj, Rest, N_Var, N_Res,paso))
    Btn2.grid(padx=1,pady=5,row=int(N_Res)+3,column=0, columnspan=int(N_Var)+1)
    

def transformar(tipo, Fun_Obj, Rest, N_Var, N_Res):
    Coef=[]
    Hol=[]
    Art=[]
    b=[]
    cont=0
    for i in range(N_Res):
        nx=[]
        
        for j in range(N_Var):
            n=Rest.get(cont).get("1.0","end")
            nx.append(float(n))
            cont+=1
        
        Coef.append(nx)
            
        n=Rest.get('b'+str(i)).get("1.0","end")
        b.append(int(n))
        
        r=Rest.get('r'+str(i)).get()
        if(r == '>='):
            a=np.zeros(N_Res, dtype=int) 
            h=np.zeros(N_Res, dtype=int)
            a[i]=1
            h[i]=-1
            Art.append(a)
            Hol.append(h)
            
        if(r == '='):
            a=np.zeros(N_Res, dtype=int)
            a[i]=1
            Art.append(a)
            
        if(r == '<='):
            h=np.zeros(N_Res, dtype=int)
            h[i]=1
            Hol.append(h)
    
        
    b=np.array(b)
    
    
    
    matriz=np.concatenate((Coef,np.transpose(np.concatenate((Hol, Art),axis=0)),b.reshape(N_Res,1)),axis=1)
    
    
    Co=np.zeros(matriz.shape[1]-1, dtype=int)
    
    for i in range(matriz.shape[1]-1):
        if(i<N_Var):
            Co[i]=Fun_Obj.get(i).get("1.0", "end")
    
        if(i>((N_Var-1)+np.array(Hol).shape[0])):
            if(tipo=='Maximizar'):
                Co[i]=-1     
            if(tipo=='Minimizar'):
                Co[i]=1
    
    
    return [matriz, Co]
  
    

    
def ejecutar(tipo, Fun_Obj, Rest, N_Var, N_Res, paso):
    if(paso==1):
        matriz=transformar(tipo, Fun_Obj, Rest, N_Var, N_Res)
        Coef=np.array(matriz[1])
        matriz=np.array(matriz[0])
        
        base=Coef[Coef.shape[0]-N_Res: Coef.shape[0]]
#        Coef[::-1][0:Coef.shape[0]-N_Res]
        
        
        Zj=np.zeros(matriz.shape[1], dtype=float)
        for i in range(N_Res):
            n=base[i]*matriz[i]
            Zj=n+Zj
            
        
        
        Cj_Zj=Coef-Zj[0:len(Zj)-1]
        
        Var=[]
        h=1
        a=1
        
        for i in range(len(Coef)):
            if(i<N_Var):
                Var.append('X'+str(i+1))
            if(i>=N_Var):
                if(Coef[i]==0):
                    Var.append('H'+str(h))
                    h+=1
                if(Coef[i]==1 or Coef[i]==-1):
                    Var.append('A'+str(a))
                    a+=1
        V_Base=Var[len(Var)-matriz.shape[0]:len(Var)]
   
    imprimir(Coef, Var, V_Base,base, matriz, Zj, Cj_Zj, tipo, paso)
    paso+=1
    
    
def imprimir(Coef, Var,V_Base,base, matriz, Zj, Cj_Zj, tipo,paso):
   
    
    
    Labl=['Cj', 'VB']
    if(paso==1):
        frame2.pack_forget()
        
        
        Lbl3=tk.Label(frame3, text="Metodo de la Gran M Paso "+str(paso))
        Lbl3.config(font=("Helvetica",24))
        Lbl3.grid(pady=5,row=0,column=0, columnspan=matriz.shape[1]+2)
        
        Labl=np.concatenate((Labl, V_Base,['Zj','Cj-Zj']))
        Var.append('b')
                
        for i in range(matriz.shape[0]+4):
           
            for j in range(matriz.shape[1]+1):
                Txt3_1=tk.Entry(frame3, width=6)
                Txt3_1.config(font=("Helvetica",15))
                Txt3_1.grid(row=i+1,column=j)
                
                if(i>1 and j>0 and j<(matriz.shape[1]+1)):
                    if(i<(matriz.shape[0]+2)):
                        Txt3_1.insert(0,int(matriz[i-2][j-1]))
                    if(i==(matriz.shape[0]+2)):            
                        Txt3_1.insert(0,str(int(Zj[j-1]))+'M')
                    if(i==(matriz.shape[0]+3) and j<matriz.shape[1]):
                        if(Zj[j-1]<0):
                            Txt3_1.insert(0,str(Coef[j-1])+'+'+str(int(Zj[j-1]*-1))+'M')
                        elif(Coef[j-1]==Zj[j-1]):
                            Txt3_1.insert(0,0)
                        else:
                            Txt3_1.insert(0,str(Coef[j-1])+'-'+str(int(Zj[j-1]))+'M') 
                   
                if(j==0):
                    Txt3_1.insert(0,Labl[i])
                
                if(i==1 and j>0):
                    Txt3_1.insert(0,Var[j-1])
        
                if(i==0 and j>0 and j<(matriz.shape[1])):
                    if('A' in Var[j-1]):
                        if(Coef[j-1]==1):    
                            Txt3_1.insert(0,'M')
                        if(Coef[j-1]==-1):
                            Txt3_1.insert(0,'-M')
                    else:
                        Txt3_1.insert(0,Coef[j-1])
        Btn2=tk.Button(frame3, text="Continuar", width=60, command=lambda: calcular(Coef, Var,V_Base,base, matriz, Zj, Cj_Zj, tipo, paso))
        Btn2.grid(padx=1,pady=5,row=matriz.shape[0]+5,column=0, columnspan=matriz.shape[1])
    
        frame3.pack()        
    else:
        frame3.pack_forget()
        Lbl3=tk.Label(newFrame, text="Metodo de la Gran M Paso "+str(paso))
        Lbl3.config(font=("Helvetica",24))
        Lbl3.grid(pady=5,row=0,column=0, columnspan=matriz.shape[1]+2)
        
        Labl=np.concatenate((Labl, V_Base,['Zj','Cj-Zj']))
        for i in range(matriz.shape[0]+4):
           
            for j in range(matriz.shape[1]+1):
                Txt3_1=tk.Entry(newFrame, width=6)
                Txt3_1.config(font=("Helvetica",15))
                Txt3_1.grid(row=i+1,column=j)
                
                if(i>1 and j>0 and j<(matriz.shape[1]+1)):
                    if(i<(matriz.shape[0]+2)):
                        Txt3_1.insert(0,matriz[i-2][j-1])
                    if(i==(matriz.shape[0]+2)):            
                        Txt3_1.insert(0,Zj[j-1])
                    if(i==(matriz.shape[0]+3) and j<matriz.shape[1]):
                        Txt3_1.insert(0,Cj_Zj[j-1])
                        
                if(j==0):
                    Txt3_1.insert(0,Labl[i])
                
                if(i==1 and j>0):
                    Txt3_1.insert(0,Var[j-1])
        
                if(i==0 and j>0 and j<(matriz.shape[1])):
                    Txt3_1.insert(0,Coef[j-1])
        
        if(terminar(tipo, Cj_Zj)==False):        
            Btn2=tk.Button(newFrame, text="Continuar", width=60, command=lambda: calcular(Coef, Var,V_Base,base, matriz, Zj, Cj_Zj, tipo, paso))
            Btn2.grid(padx=1,pady=5,row=matriz.shape[0]+5,column=0, columnspan=matriz.shape[1])
            
            newFrame.pack()        
        else:
            
            r=[]
            for i in range(len(Var)-1):
                
                
                Lbl3_1=tk.Label(newFrame, text=Var[i]+'= ')
                Lbl3_1.config(font=("Helvetica",24))
                Lbl3_1.grid(pady=5,row=matriz.shape[0]+(6+i),column=0, columnspan=2)
                
                if(Var[i] in V_Base):  
                    b=matriz[np.where(np.array(V_Base) == np.array(Var[i]))[0][0]][matriz.shape[1]-1]
                    r.append(b)
                    Lbl3_2=tk.Label(newFrame, text=b)
                else:
                    r.append(0)
                    Lbl3_2=tk.Label(newFrame, text=0)
                
                Lbl3_2.config(font=("Helvetica",24))
                Lbl3_2.grid(pady=5,row=matriz.shape[0]+(6+i),column=1, columnspan=2)
                
            
            
            
            z=sum(Coef*r)
            Lbl3_4=tk.Label(newFrame, text="Z=")
            Lbl3_4.config(font=("Helvetica",24))
            Lbl3_4.grid(pady=5,row=matriz.shape[0]+6,column=3, columnspan=2)
            
            Lbl3_3=tk.Label(newFrame, text=z)
            Lbl3_3.config(font=("Helvetica",24))
            Lbl3_3.grid(pady=5,row=matriz.shape[0]+6,column=4, columnspan=2)
        
            Btn2=tk.Button(newFrame, text="Terminado", width=60)
            Btn2.grid(padx=1,pady=5,row=matriz.shape[0]+5,column=0, columnspan=matriz.shape[1])
            
            
            newFrame.pack()
    

    
def calcular(Coef, Var,V_Base,base, matriz, Zj, Cj_Zj, tipo, paso):

    
    if(paso==1):
        
        M=1000000
        
        base=base*M
        Zj=np.zeros(matriz.shape[1],dtype=float)
        
        for i in range(matriz.shape[0]):
            n=base[i]*matriz[i]
            Zj=n+Zj
            
        Cj_Zj=np.array(Coef+(Zj[0:len(Zj)-1]*-1))
        
        Col_Piv=np.where(Cj_Zj==max(Cj_Zj))[0][0]
        
        div=matriz[:,Col_Piv]/ matriz[:,matriz.shape[1]-1]
        
        Fil_Piv=np.where(div==min(div))[0]
        
        Fil_Piv=Fil_Piv[len(Fil_Piv)-1]
        
        matriz[Fil_Piv]/=matriz[Fil_Piv][Col_Piv]
        
        for i in range(matriz.shape[0]):
            if(i!=Fil_Piv):
                m=matriz[i][Col_Piv]
                matriz[i]=(matriz[Fil_Piv]*(m*-1))+matriz[i]
                
        
        base[Fil_Piv]=Coef[Col_Piv]
        V_Base[Fil_Piv]=Var[Col_Piv]
        
        ar=[]
        for i in range(len(Var)):
            if('A' in Var[i]):
                ar.append(i)
        matriz=np.delete(matriz, ar,axis=1)
        Var=np.delete(Var, ar)
        Coef=np.delete(Coef, ar)
        
        Zj=np.zeros(matriz.shape[1],dtype=float)
        
        for i in range(matriz.shape[0]):
            n=base[i]*matriz[i]
            Zj=n+Zj
            
        Cj_Zj=np.array(Coef+(Zj[0:len(Zj)-1]*-1))
        
        imprimir(Coef, Var, V_Base,base, matriz, Zj, Cj_Zj, tipo, 2)
    
    else:
        
               
        Col_Piv=np.where(Cj_Zj==max(Cj_Zj))[0][0]
        
        div=matriz[:,matriz.shape[1]-1]/matriz[:,Col_Piv]
        
        Fil_Piv=np.where(div==min(div))[0]
        
        Fil_Piv=Fil_Piv[len(Fil_Piv)-1]
        
        matriz[Fil_Piv]/=matriz[Fil_Piv][Col_Piv]
        
        for i in range(matriz.shape[0]):
            if(i!=Fil_Piv):
                m=matriz[i][Col_Piv]
                matriz[i]=(matriz[Fil_Piv]*(m*-1))+matriz[i]
                
        
        base[Fil_Piv]=Coef[Col_Piv]
        V_Base[Fil_Piv]=Var[Col_Piv]
        
        Zj=np.zeros(matriz.shape[1],dtype=float)
        
        for i in range(matriz.shape[0]):
            n=base[i]*matriz[i]
            Zj=n+Zj
            
        Cj_Zj=np.array(Coef+(Zj[0:len(Zj)-1]*-1))
        
        imprimir(Coef, Var, V_Base, base, matriz, Zj, Cj_Zj, tipo, paso+1)
    
def terminar(tipo, Cj_Zj):
    terminado=True
    for i in range(len(Cj_Zj)):
        if(tipo=='Maximizar'):
            if(Cj_Zj[i]>0):
                terminado=False
        if(tipo=='Minimizar'):
            if(Cj_Zj[i]<0):
                terminado=False
    return terminado

main()


raiz.mainloop()

