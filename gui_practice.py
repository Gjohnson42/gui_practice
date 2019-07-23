import tkinter
from tkinter import *
# This just calls the GUI window into existence
top = tkinter.Tk()
# Start of widgets and specifiers
top.title("Generic Practice GUI")
canvas = Canvas(top, width = 1000, height = 500)
img = PhotoImage(r"C:\Users\Garrett\Pictures\capacitor.png")
canvas.create_image(20, 20, anchor=NW, image=img)



# End of widget code
tkinter.mainloop()