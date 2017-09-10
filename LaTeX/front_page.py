##cv bulider front page
##welcome

from Tkinter import *
#import Tkinter
import gui_for_proj as gui

def tech_gui_close():
    front.destroy()
    gui.mcf()
    

def ntech_gui_close():
    front.destroy()
    #gui.main_cv_frame()
    

    
front = Tk()

front.geometry("300x200")
front.title("CV Bulider")
front.configure(bg = "white")


donot = Label(front , text = "                              ",bg = "white")
donot.grid(row = 1,column = 1)

heading = Label(front,text = "CV Builder",bg = "white")
heading.grid(row = 1,column = 2)
##technical = Label(front,text = "Technical CV")
##technical.pack()
donot2 = Label(front , text = "                  ",bg = "white")
donot2.grid(row = 1,column = 3)

donot3 = Label(front , text = "                  ",bg = "white")
donot3.grid(row = 2,column = 1)

donot4 = Label(front , text = "                  ",bg = "white")
donot4.grid(row = 4,column = 1)



press1 = Button(front,text = "Let's Get Started!",command = tech_gui_close,relief =GROOVE)
press1.grid(row = 3,column = 2)


##ntechnical = Label(front,text = "Non Technical CV")
##ntechnical.pack()
#press2 = Button(front,text = "Non Technical CV",command = ntech_gui_close,relief =GROOVE)
#press2.grid(row = 5, column = 2)



front.mainloop()
