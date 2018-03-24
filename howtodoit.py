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
        answer.insert(0, 'nqmaa')
    else:
        result = n1 / n2
        answer.delete(0, len(answer.get()))
        answer.insert(0, result)

    #pravi //
gui = tk.Tk()
gui.geometry("300x300")

St = tk.Button (gui, text='+', bg = 'magenta', command = sum,  height= 1, padx= 4)
St.place (x=20, y= 50)

Sr = tk.Button (gui, text='-', bg = 'yellow', command = sub, height= 1, padx= 5)
Sr.place (x=20, y= 80)

Sf = tk.Button (gui, text='*', bg = 'magenta',  command = mul, height= 1, padx= 5)
Sf.place (x=20, y= 110)

Sy = tk.Button (gui, text='/', bg = 'yellow',  command = dev, height= 1, padx= 5)
Sy.place (x=20, y= 140)

#tekstovo pole
pole = tk.Entry(gui)
pole.place (x=90, y=50)

bg = tk.Entry(gui)
bg.place (x=90, y=110)

#otgovor
answer = tk.Entry(gui)
answer.place (x=90, y=180)

gui.mainloop()
