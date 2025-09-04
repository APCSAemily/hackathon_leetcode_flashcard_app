#pip install Pillow
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.tix import IMAGETEXT
from PIL import Image
import jsonlines
import random
from PIL import Image, ImageTk
# import playsound    #need to do pip install playsound

#https://www.geeksforgeeks.org/node-js-process-stdin-property/

def reset_diff(difficulty):
    global curr_idx
    leet_list = []
    if difficulty != 'Random':
        with jsonlines.open('leetcode-solutions.jsonl') as reader:
            for line in reader:
                if(line['difficulty'] == difficulty): 
                    leet_list.append(line)
    elif difficulty == 'Random':
        with jsonlines.open('leetcode-solutions.jsonl') as reader:
                for line in reader:
                    leet_list.append(line)
    curr_idx = 0
    random.shuffle(leet_list)    
    print("displayed")
    print(str(len(leet_list) )) 

reset_diff("Medium")
