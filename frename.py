import tkinter as tk
import os
HEIGHT = 700
WIDTH = 800
count = 0



def replace_function():
    path = entry_path.get()
    os.chdir(path)
    for f in os.listdir():
        
        z = os.path.splitext(f)
        if z[1] == entry_ext.get():
            global count
            count+=1
        
            os.rename(f , entry_name.get()+str(count)+z[1])

root = tk.Tk()

canvas = tk.Canvas(root,height = HEIGHT , width = WIDTH)
canvas.pack()

frame = tk.Frame(root , bg = '#33FFD7')
frame.place(relheight = 0.8 , relwidth = 0.8 , relx = 0.1 , rely = 0.1)

label = tk.Label(frame , text = ' enter path ')
label.place(relx = 0.001 ,rely = 0.11)

entry_path = tk.Entry(frame, bg = '#e6f7f2')
entry_path.place( relheight = 0.05 , relwidth = 0.6 , relx= 0.12 , rely =0.1)

label = tk.Label(frame , text = ' enter name to replace with ')
label.place(relx = 0.001 ,rely = 0.3)

entry_name = tk.Entry(frame, bg = '#e6f7f2')
entry_name.place( relheight = 0.05 , relwidth = 0.6 , relx= 0.25 , rely =0.3)

label = tk.Label(frame , text = ' enter extension ')
label.place(relx = 0.001 ,rely = 0.5)

entry_ext = tk.Entry(frame, bg = '#e6f7f2')
entry_ext.place( relheight = 0.05 , relwidth = 0.6 , relx= 0.16 , rely =0.5)

button = tk.Button(frame , bg ='#6ce08b' , text = 'replace' , command = lambda: replace_function())
button.place(relheight = 0.05 , relwidth = 0.4 , relx = 0.20 , rely = 0.6)




root.mainloop()