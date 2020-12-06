from tkinter import *
from PIL import ImageTk, Image
import cv2
import queue
import threading
from tkinter import ttk 
from read_cam import read_cam


cam1 = read_cam()
cam1.setDaemon(True)
cam1.start()



def video_stream():
    try:
        frame = cam1.queue.get(timeout = 0.1)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        frame = Image.fromarray(frame)
        frame = ImageTk.PhotoImage(image = frame)
        Label1.frame = frame
        Label1.config(image=frame)
        Label1.after(1, video_stream) 
    except: 
        Label1.frame = None
        Label1.config(image=None)
        Label1.after(1, video_stream)


    
root = Tk()
root.geometry('700x600')
Label1 = Label(root, bg = 'blue', text = 'Waiting for connection')
Button1 = Button(text = 'Start', command = cam1.event.set)
Button2 = Button(text = 'Stop', command = cam1.event.clear)






Label1.place(x = 25, y = 30, width = cam1.width, height = cam1.height)
Button1.place(x = 25, y = 550, width = 80, height = 40)
Button2.place(x = 500, y = 550, width = 80, height = 40)




video_stream()




root.mainloop()
