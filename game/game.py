words = ["mango", "apple","banana","cat","dog","deforestation","man","head","sun","noble"]

def time():
    global timeLeft
    if (timeLeft>0):
        timeLeft -= 1
        timeLabelCount.configure(text = timeLeft)
        timeLabelCount.after(1000,time)
    else:
        gameplay  

def startGame(event):
    global score,miss 
    if wordEntry.get() == wordLabel['text']:
       score += 1
       scoreLabelCount.configure(text = score)
    else:
       miss += 1
       print("miss :",miss)
    random.shuffle(words)      
    wordLabel.configure(text=words[0]) 
    wordEntry.delete(0,END)

from tkinter import *
import random


################################# root methods
root = Tk()
root.geometry('800x600+400+100') # works on height and weidth 
root.configure(bg = 'powder blue')  # change the background  colour
root.title("typing speed ") # display the title 

################################# variables 
score = 0
timeLeft = 60
miss = 0
################################# label methods
fontLabel = Label(root, text= "welcome in  typing speed test", font =( "arial", 25, "italic bold"),
 bg = "powder blue", fg = "red" )
fontLabel.place(x = 10, y = 10)
random.shuffle(words)
wordLabel = Label(root,text = "mango",font =( "arial", 40, "italic bold"),bg = "powder blue")
wordLabel.place(x = 300, y = 200)

scoreLabel = Label(root, text = "your score :", font =( "arial", 25, "italic bold"),bg = "powder blue")
scoreLabel.place(x = 10, y = 100)

scoreLabelCount = Label(root, text = score, font =( "arial", 25, "italic bold"),bg = "powder blue", fg = "blue")
scoreLabelCount.place(x = 80, y = 180)

timerLabel =  Label(root, text = "Time left", font =( "arial", 25, "italic bold"),bg = "powder blue")
timerLabel.place(x = 600, y = 100)

timeLabelCount = Label(root, text = timeLeft, font =( "arial", 25, "italic bold"),bg = "powder blue", fg = "blue")
timeLabelCount.place(x = 680, y = 180)


############################ entry method
wordEntry = Entry(root, font =( "arial", 25, "italic bold"), bd = 10, justify = "center")
wordEntry.place(x = 200, y = 300)
wordEntry.focus_set() # without no click with mouse we can type 
######################################
root.bind('<Return>',startGame)

root.mainloop() 