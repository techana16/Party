import tkinter as tk
import serial

gui = tk.Tk ()
gui.geometry("600x200")

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


S = tk.Button (gui, text='STOP', bg = 'lightpink', command=stop, height= 2, padx= 9 )
S.place (x= 10, y= 110)

l= tk.Button(gui, text='LEFT  ', bg = 'lightpink', command=left , height= 2, padx= 9)
l.place (x=90, y= 110)

R = tk.Button (gui, text='RIGHT', bg = 'lightpink', command=right , height= 2, padx= 7)
R.place (x=220, y= 110)

B = tk.Button (gui, text='BACK', bg ='lightpink', command=back , height= 2, padx= 10)
B.place (x=300, y= 110)

F = tk.Button (gui, text='FORWARD', bg ='lightpink', command=forward , height= 2, padx= 10)
F.place (x=300, y= 10)


gui.mainloop()
