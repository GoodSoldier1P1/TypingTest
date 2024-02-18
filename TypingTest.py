from tkinter import *
from timeit import default_timer as timer
import random

# creating window with gui
window = Tk()

# define the size of the window
window.geometry("450x200")

x = 0

# define function for test
def game():
    global x

    #loop for destroying window, after on test
    if x == 0:
        window.destroy()
        x = x+1
    
    #define function for test results
    def checkResult():
        if entry.get() == words[word]:

            #start time is from window opening --> window closing
            end = timer()

            #deduct start time from end time
            print(end-start)
        else:
            print("Wrong Input")
    
    words = ['programming', 'coding', 'algorithm', 'systems', 'python', 'software']

    #giving random words
    word = random.randint(0, (len(words)-1))

    #start timer
    start = timer()
    windows = Tk()
    windows.geometry("450x200")

    #use label method from tkinter to label window
    x2 = Label(windows, text=words[word], font="times 20")

    #place labeling in window
    x2.place(x=150, y=10)
    x3 = Label(windows, text="Start Typing", font="times 20")
    x3.place(x=280, y=55)

    entry = Entry(windows)
    entry.place(x=280, y=55)

    #buttons to submit output and check results
    b2 = Button(windows, text="Done",
                command=checkResult, width=12, bg="grey")
    b2.place(x=150, y=100)

    b3 = Button(windows, text="Try Again",
                command=game, width=12, bg="grey")
    b3.place(x=250, y=100)
    windows.mainloop()


x1 = Label(window, text="Let's start it up!!!", font="times 20")
x1.place(x=10, y=50)

b1 = Button(window, text="Go", command=game, width=12, bg="grey")
b1.place(x=150, y=100)

#call window
window.mainloop()