from tkinter import *
import guest
import compete

# read the data from the file and dispaly in window


def display_high_score():

    # create a window
    window = Tk()
    # change the name of the window
    window.title("High Score")

    screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (800/2))
    y_cordinate = int((screen_height/2) - (500/2))
    window.geometry(f"800x500+{x_cordinate}+{y_cordinate}")

    with open("user.txt", "r") as f:
        for line in f:
            print(line)
            label = Label(window, text=line, bg="black",
                          fg="white", font=("Arial Bold", 20))
            label.pack()
            label.place(x=50, y=50)