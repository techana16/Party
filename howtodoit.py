import tkinter as tk

def sum():
    n1 = int(pole.get())
    n2 = int(bg.get())
    result= n1 + n2
    answer.delete(0, len(answer.get()))
    answer.insert(0, result)

def sub():
    n1 = int(pole.get())
    n2 = int(bg.get())
    result= n1 - n2
    answer.delete(0, len(answer.get()))
    answer.insert(0, result)

def mul():
    n1 = int(pole.get())
    n2 = int(bg.get())
    result= n1 * n2
    answer.delete(0, len(answer.get()))
    answer.insert(0, result)

def dev():
    n1 = int(pole.get())
    n2 = int(bg.get())
    if n2 ==0:
        answer.delete(0, len(answer.get()))
        answer.insert(0, 'Error')
    else:
        result = n1 / n2
        answer.delete(0, len(answer.get()))
        answer.insert(0, result)

    #pravi //
gui = tk.Tk()
gui.geometry("300x300")

St = tk.Button (gui, text='+', bg = 'magenta', command = sum,  height= 1, padx= 4)
St.config( font = ('times' , 14))
St.place (x=20, y= 30)

Sr = tk.Button (gui, text='-', bg = 'yellow', command = sub, height= 1, padx= 5 )
Sr.config( font = ('times' , 15))
Sr.place (x=20, y= 80)

Sf = tk.Button (gui, text='*', bg = 'magenta',  command = mul, height= 1, padx= 4)
Sf.config( font = ('times' , 15))
Sf.place (x=20, y= 130)

Sy = tk.Button (gui, text='/', bg = 'yellow',  command = dev, height= 1, padx= 5)
Sy.config( font = ('times' , 15))
Sy.place (x=20, y= 180)

#tekstovo pole
pole = tk.Entry(gui)
pole.place (x=90, y=40)

bg = tk.Entry(gui)
bg.place (x=90, y=110)

#otgovor
answer = tk.Entry(gui)
answer.place (x=90, y=180)

gui.mainloop()
