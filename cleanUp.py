#pip install Pillow
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.tix import IMAGETEXT
from PIL import Image
import jsonlines
import random
from PIL import Image, ImageTk

#need to discuss and ask whats going on
#global variables
leet_list = [] #holds potential problems (based on difficulty)
curr_idx = 0 #current idx of above list that is currently being shown
# curr_obj = None #current problem being shown
#for this I thought about just using leet_list[curr_idx] so its more nimble than using something to store the object
lang = "" #stores current language
mat = [] #stores buttons
flip = False
page_label = None
level_label= None
title = None
startGame = True

def b_click(command):
    global mat, flip, curr_idx
    if (command == "l"):
        if curr_idx-1 ==-1:
            mat[0].config(state=DISABLED)
        else:
            curr_idx -=1
            mat[2].config(state=tk.NORMAL)   
        flip = False
    elif (command == "r"):
        if curr_idx+1 == len(leet_list):
            #end_game()
            pass
        else:
            curr_idx +=1
            mat[0].config(state=tk.NORMAL)   
        flip = False
    elif(command == "f"):
        flip = not flip
    # scroll_text.delete(0,END)
    # display()
    print("" + str(curr_idx) +"\t"+leet_list[curr_idx]['id'] + "\t "+ str(flip) + "\t" + str(leet_list[curr_idx]['difficulty'])+ "\t\t" + lang)
    root.update()

def display():
    pass

def reset(difficulty):
    global curr_idx, startGame
    with jsonlines.open('leetcode-solutions.jsonl') as reader:
        if(difficulty == 'Random'): #all items to list
            for line in reader:
                leet_list.append(line)
        else:
            for line in reader:
                if(line['difficulty'] == difficulty): #only items of certain difficulty
                    leet_list.append(line)  
    curr_idx = 0
    random.shuffle(leet_list)    
    if not startGame:
        display()  


root = tk.Tk()
root.title('Leecode Flashcards')
root.geometry("1000x800")

root.mainloop()