import pyautogui as p
import tkinter as tk
from PIL import Image, ImageTk
import time

running = True

root = tk.Tk()
root.state("zoomed")
root.title("Maze Solver")

def stop_program(event=None):
    global running
    running = False
    print("Stopped.")

root.bind("<Escape>", stop_program)

image = Image.open("maze.png")
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo, borderwidth=0)
label.pack()

def start_maze():
    global running

    print("Starting in 3 seconds...")
    print("Press ESC to stop.")

    root.update()
    time.sleep(3)

    path = [
        (621,88),
        (621,88),
        (621,88),
        (685,88),
        (684,100),
        (721,120),
        (725,96),
        (752,94),
        (767,139),
        (834,147),
        (848,49)
    ]

    for x, y in path:
        root.update()

        if running == False:
            break

        p.moveTo(x, y, duration=0.2)

    print("Maze complete or stopped.")

root.after(1000, start_maze)
root.mainloop()