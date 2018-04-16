import tkinter as tk
import serial
import background as bg

gui = tk.Tk ()
gui.geometry("520x200")

#car = serial.Serial('com4', 9600)

def stop():
    car.write('F'.encode())

def left():
    car.write('L'.encode())

def right():
    car.write('R'.encode())

def back():
    car.write('B'.encode())

def forward ():
    car.write('F'.encode())


S = tk.Button (gui, text='STOP', bg = 'yellow', command=stop, height= 2, padx= 12 )
S.config(  font=('times', 12))
S.place (x= 430, y= 80)

l= tk.Button(gui, text='LEFT  ', bg = 'yellow', command=left , height= 2, padx= 9)
l.config(  font=('times', 12))
l.place (x=230, y= 80)

R = tk.Button (gui, text='RIGHT', bg = 'lightpink', command=right , height= 2, padx= 7)
R.config(  font=('times', 12))
R.place (x=330, y= 80)

B = tk.Button (gui, text='BACK', bg ='lightpink', command=back , height= 2, padx= 10)
B.config(  font=('times', 12))
B.place (x=130, y= 80)

F = tk.Button (gui, text='FORWARD', bg ='yellow', command=forward , height= 2, padx= 1 )
F.config(  font=('times', 12))
F.place (x=10, y= 80)


gui.mainloop()
