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


#need to discuss and ask whats going on
#global variables
leet_list = [] #holds potential problems (based on difficulty)
curr_idx = 0 #current idx of above list that is currently being shown
#curr_obj = None #current problem being shown
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
    scroll_text.delete(0,END)
    display()
    print("" + str(curr_idx) +"\t"+leet_list[curr_idx]['id'] + "\t "+ str(flip) + "\t" + str(leet_list[curr_idx]['difficulty'])+ "\t\t" + lang)
    root.update()


# DISPLAYING
def display():
    page_label.config(text= str("Question " + str(curr_idx+1) + " / "+ str(len(leet_list)+1)))
    level_label.config(text = "Current Difficulty: " + str(leet_list[curr_idx]['difficulty']) + "\t" + "Current Language: " + str(lang))
    cardwords = ""
    if flip:
        scroll_text.config(bg='#dbfff2')  # it works :0 
        title.config(text = str(leet_list[curr_idx]["title"] + "  (Answer)"))
        cardwords = str(leet_list[curr_idx]["answer"][str(lang)])
        list_str = str(cardwords).split("\n")
        list_str = list_str[1:]
        i = 1
        for string in list_str:
            string = "     "+str(i) + "          "+ string
            string = string.replace("`","")
            i+=1
            scroll_text.insert(END,string)
        mat[1].config(bg = '#b0ffe2') #it works :0
        
    else:
        scroll_text.config(bg='#f0dcfc')
        title.config(text = str(leet_list[curr_idx]["title"] + "  (Question)"))
        cardwords = leet_list[curr_idx]["content"]
        #question.config(text = str(leet_list[curr_idx]["answer"][str(lang)]))
        mat[1].config(bg = '#e1b0ff')
        list_str = str(cardwords).split("\n")
        scroll_text.delete(0,END)
        for string in list_str:
            string = "     "+ string
            string = string.replace("**","   |   ")
            string = string.replace("*","       - ")
            string = string.replace("_", " ")
            string = string.replace("`","")
            string = string.replace("\\"," ")
            scroll_text.insert(END,string)
    root.update()

def reset_diff(difficulty):
    global curr_idx,leet_list
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
    if not startGame:
        display()
    print(str(len(leet_list) ))    
        

def reset_lang(language):
    global lang, curr_idx
    languageStr = str(language)  
    curr_idx = 0
    lang = language
    if not startGame:
        print("not start game")
        display()
    pass

def add_frame():
    global bottomFrame, topFrame, page_label, level_label
    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    level_label = tk.Label(topFrame,  
        text="Current Difficulty: " + str(leet_list[curr_idx]['difficulty']) + "\t" + "Current Language: " + str(lang),
        anchor="e",
        justify="right",
        width=1000,
        height = 1,
        bg="white"
    )
    level_label.pack()
    add_flashcard_label()
    add_scroll_bar()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)
    page_label = tk.Label(bottomFrame,
        text="Question " + str(curr_idx) + " / "+ str(len(leet_list)),
        anchor="s",
        justify="right",
        width=1000,
        height = 1,
        # side = TOP
        bg="gray",
        fg= "white",
        font =("Helvetica20 italic", 18)
    )
    page_label.pack(side = TOP)

def add_menu ():
    my_menu = Menu(root)
    root.config(menu=my_menu)

    lang_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Languages", menu=lang_menu)
    lang_menu.add_command(label="C++", command=lambda: reset_lang("c++"))
    lang_menu.add_command(label="Java", command=lambda: reset_lang("java"))
    lang_menu.add_command(label="Python", command=lambda: reset_lang("python"))
    lang_menu.add_command(label="Javascript", command=lambda: reset_lang("javascript"))

    diff_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="Difficulty", menu=diff_menu)
    diff_menu.add_command(label="Easy", command = lambda: reset_diff("Easy"))
    diff_menu.add_command(label="Medium", command=lambda: reset_diff("Medium"))
    diff_menu.add_command(label="Hard", command=lambda: reset_diff("Hard"))
    diff_menu.add_command(label="Random", command=lambda: reset_diff("Random"))

def add_buttons():
    left = Button(bottomFrame, text=str("<"), font=('helvetica', 20), height=1, width=11, bg="SystemButtonFace", command=lambda: b_click("l"))
    left.pack(side = LEFT,padx=1, pady=1)
    left.config(justify= "center", anchor="center")
    mat.append(left)
    flip = Button(bottomFrame, text=str("Flip Floop"), font=('helvetica', 20), height=1, width=38, bg="SystemButtonFace", command=lambda: b_click("f"))
    flip.pack(side = LEFT,padx=1, pady=1)
    flip.config(justify= "center", anchor="center")
    flip.config(bg = '#e1b0ff')
    mat.append(flip)
    right = Button(bottomFrame, text=str(">"), font=('helvetica', 20), height=1, width=11, bg="SystemButtonFace", command=lambda: b_click("r"))
    right.pack(side = LEFT,padx=1, pady=1)
    right.config(justify= "center", anchor="center")
    mat.append(right)

def add_flashcard_label():
    global title, question
    title = tk.Label(topFrame, text = "\n"+str(leet_list[curr_idx]["title"] + "  (Question)"))
    title.config(font =("Helvetica20 italic", 22))
    title.pack()

def add_scroll_bar():
    global scroll_text
    
    Main = Canvas(topFrame,background="blue", height = 10000,width =5000)
    Main.configure(scrollregion=Main.bbox("all"),)
    scroll_text = Listbox(Main,  width=800, height=31) 
    list_str = str(leet_list[curr_idx]["content"]).split("\n")
    scroll_text.config(bg='#f0dcfc')
    #title.config(text = str(leet_list[curr_idx]["title"] + "\t(Answer)"))
    cardwords = leet_list[curr_idx]["content"]
    list_str = str(cardwords).split("\n")
    scroll_text.delete(0,END)
    for string in list_str:
        string = "     "+ string
        string = string.replace("**","   |   ")
        string = string.replace("*","       - ")
        string = string.replace("_", " ")
        string = string.replace("`","")
        string = string.replace("\\"," ")
        scroll_text.insert(END,string)
    scroll_text.pack(side = LEFT) 
    
    Main.pack()
""" Main Instantiations """

root = tk.Tk()
root.title('Leecode Flashcards')
root.geometry("1000x680")

print("page" +  "  \tflip   \tdifficulty     \tlanguage")
reset_lang("c++")
reset_diff("Random")
add_frame()
add_menu()
add_buttons()

startGame = False

root.mainloop()
# HIIIIIIdklrgjoisrrshjgsejbgj,khhjfhg,jmuiehguieggdsfgnknknkjnlnklnl - hi hi hi

"""
- color buttons :}
- noooope >> split screen? ???
- SCROLL!
- fix justification
- fix lagging
- pray
"""