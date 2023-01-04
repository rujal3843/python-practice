from tkinter import *
import guest
import compete

# create a window
window = Tk()
# change the name of the window
window.title("Speed test")

# set the size of the window
screen_width, screen_height = window.winfo_screenwidth(), window.winfo_screenheight()
x_cordinate = int((screen_width/2) - (800/2))
y_cordinate = int((screen_height/2) - (500/2))

window.geometry(f"800x500+{x_cordinate}+{y_cordinate}")
window.title("Typing speed test.")

# change the background color of the
window.configure(background="black")

# create a label upper middle of the window
label = Label(window, text="Typing Speed Tester ",
              bg="black", fg="white", font=("Arial Bold", 20))

# place the label in the window
label.pack()

# create a button in the middle of the window
guest = Button(window, text="Guest", bg="red", command=guest.game)
compete = Button(window, text="Compete", bg="red", command=compete.game)

# change the colour of the text on the button
guest.config(fg="white", font=("Arial Bold", 15))
compete.config(fg="white", font=("Arial Bold", 15))

# place the button in the window
guest.pack()
compete.pack()

# place the button in the middle of the window
guest.place(x=450, y=200)
compete.place(x=200, y=200)

# increase the size of the button
guest.config(width=13, height=5)
compete.config(width=13, height=5)

# display a message in the window
message = Label(window, text="Please choose a mode", bg="white",)
message.pack()
# place the message in the middle of the window
message.place(x=275, y=150)
message.config(height=2, width=40)


window.mainloop()