
from py3270 import Emulator
import time
import tkinter as tk
import pandas as pd
import xlrd

##lista = ["Artikel", "Qty"]
xl = pd.read_csv('SaldoCor2.csv', sep=';')##, usecols= lista) ##, dtype = {'Qty':int})

xl.head()
print(xl)

##art = xl[1]
##qty = xl['Qty']
print (xl['Qty'][1])
##xl['saldodiff'] = xl['Qty'] - xl['UPPINV'] + xl['NEDINV']

##print(len(xl))

def handle_click(event):
    U1=U_ID.get()
    U2=P_word.get()
    
    em = Emulator(visible=True)

    em.connect('turbo.got.volvocars.net')

    em.wait_for_field()
    time.sleep(0.2)
    em.send_string('mas')
    em.send_enter()
    time.sleep(1)
    em.wait_for_field()
    
    em.send_string(U1) 
    
    em.exec_command('Tab')
    em.send_string(U2) 
    em.send_enter()
    time.sleep(1)
    em.wait_for_field()
    trans= 'UPPINV' ##str(entry.get())
    em.send_string(trans)
    em.send_enter()
    for i in range(xl.shape[0]):
        
        
        em.send_string(str(art[i]))
        em.send_enter()
        em.send_string('joacim')
        em.send_pf4()
        time.sleep(1)
        em.send_string(str(qty[i]))
        em.send_pf('2')


    time.sleep(3)

def Prod_click(event):
    U1=U_ID.get()
    U2=P_word.get()
    em = Emulator(visible=True)

    em.connect('mas.gothenburg.vcc.ford.com')
    em.wait_for_field()
    time.sleep(0.2)
    em.send_string('mas')
    em.send_enter()
    time.sleep(1)
    em.wait_for_field()
    em.send_string(U1) 
    em.exec_command('Tab')
    em.send_string(U2) 
    em.send_enter()
    time.sleep(1)
    em.wait_for_field()
    trans= str(entry.get())
    em.send_string(trans)
    em.send_enter()
    for i in range(xl.shape[0]):
        i=i+1
        em.send_string(art[i])
        em.send_enter
    time.sleep(3)


window = tk.Tk()
ent =tk.Entry(window)


knapp = tk.Button(text= "Turbo")
knapp.bind("<Button-1>", handle_click)
knapp.grid(column= 0, row=1 )
knapp2 = tk.Button(text= "MAS_Prod")
knapp2.bind("<Button-1>", Prod_click)
knapp2.grid(column= 1, row = 1)
User = tk.Label(text="UserID for MAS")
User.grid(column= 0, row=2) 
U_ID = tk.Entry()
U_ID.grid(column=1,row=2)

PWord = tk.Label(text="Password for MAS")
PWord.grid(column= 0, row=3) 
P_word = tk.Entry()
P_word.grid(column=1,row=3)
label = tk.Label(text="Choose Tranaction for MAS")
label.grid(column= 0, row=4) 
entry = tk.Entry()
entry.grid(column=1,row=4)

window.mainloop()