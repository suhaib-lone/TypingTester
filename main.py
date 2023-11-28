import curses
import time
import random
import tkinter as tk
from tkinter import Label, Button
from curses import wrapper
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("PRESS ANY KEY TO CONTINUE:")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM= {wpm}")
    for i, char in enumerate(current):
        if current[i] == target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(2))

def texts():
    with open("sent.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = texts()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    while True:
        time_elapsed = max((time.time() - start_time), 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()
        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to play again:")
        key = stdscr.getkey()
        if ord(key) == 27:
            break

def start_game():
    root.destroy()  # Close the tkinter window
    wrapper(main)

# Create a tkinter window for the main menu
root = tk.Tk()
root.title("Typing Game")

# Add a title label
title_label = Label(root, text="Typing Game", font=("Helvetica", 18))
title_label.pack(pady=10)

# Add an instructions label
instruction_label = Label(root, text="Press the button to start the game", font=("Helvetica", 12))
instruction_label.pack(pady=10)

# Add a start button
start_button = Button(root, text="Start Game", command=start_game, font=("Helvetica", 14))
start_button.pack(pady=10)

root.mainloop()




'''import curses
from curses import wrapper
import time 
import random
import tkinter as tk


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("PRESS ANY KEY TO CONTINUE:")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0, f"WPM= {wpm}")
    for i, char in enumerate(current):
        if current[i]==target[i]:
            stdscr.addstr(0, i, char, curses.color_pair(1))
        else:
            stdscr.addstr(0, i, char, curses.color_pair(2))

def texts():
    with open("sent.txt", "r") as f:
        lines=f.readlines()
        return random.choice(lines).strip()





     
def wpm_test(stdscr):
    target_text=texts()
    current_text=[]
    wpm=0
    start_time=time.time()
    stdscr.nodelay(True)
    while True:
        time_elapsed=max((time.time() - start_time),1)
        wpm=round((len(current_text) / (time_elapsed/60))/5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text,wpm)
        stdscr.refresh()
        if  "".join(current_text)==target_text:
            stdscr.nodelay(False)
            break
        try:
            key=stdscr.getkey()
        except:
            continue

        if ord(key)== 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f' ):
            if len(current_text)>0:
                current_text.pop()
        elif len(current_text)<len(target_text):
            current_text.append(key)
       



def  main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)


    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0, "You completed the text! Press any key to play again:")
        key=stdscr.getkey()
        if ord(key)==27:
            break
        


    
wrapper(main)'''
