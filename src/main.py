
from tkinter import *
import time
from SoundMnager import sound

# ==================== FUNCTIONS ====================
global mins, sec

def start():
    global mins, sec
    mins = int(entry.get())
    sec = 0
    while True:
        if mins == 0 and sec == 0:
            labeltime.config(text = "Time is up!")
            sound()
            break
        elif sec == 0:
            mins -= 1
            sec = 59
        else:
            sec -= 1
        labeltime.config(text = str(mins) + ":" + str(sec))
        root.update()
        time.sleep(1)
    labeltime.config(text = "         ")
    entry.delete(0, END)
    
def stop():
    root.destroy()

# ==================== MAIN ========================

root = Tk()
root.geometry("300x200")
root.title("TIMER")
root.configure(background="light green")



labeltime = Label(root, text ="         ", font = 40)
labeltime.place(x = 125, y = 0)

entry = Entry(root)
entry.place(x = 80, y = 41)


btnStart = Button(root, text = "    START    ", command = start )
btnStart.place(x = 110, y = 67)
btnStop = Button(root, text = "     STOP     ", command = stop )
btnStop.place(x = 110, y = 105)





root.mainloop()
