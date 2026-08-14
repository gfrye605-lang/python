import os
import tkinter as tk
import pygame

# -----------------------------------------------

# Question & Answer List
questions = {"What was the biggest promise I made to you?":
             "To be here with you forever",
             "What do we always say to each other?":
             "I love you",
             "How long have we been dating for?": "1 year, 3 months",
             "When do couples usually give promise rings?":
             "6 months"}

# ------------------------------------------------

# Vars
question_keys = list(questions.keys())
current_index = 0
currentq = question_keys[current_index]
currentans = questions[currentq]

# ------------------------------------------------
# Hints
hint1 = "What is the opposite of me leaving?"
hint2 = "You know this one silly!"
hint3 = "Check the app, my love!"
hint4 = "It's honestly sooner than you'd think"

def hint():
     if current_index == 0:
          label.configure(text=hint1)
          root.after(3000, res_text)
     elif current_index == 1:
          label.configure(text=hint2)
          root.after(3000, res_text)
     elif current_index == 2:        
          label.configure(text=hint3)
          root.after(3000, res_text)
     elif current_index == 3:
          label.configure(text=hint4)
          root.after(3000, res_text)

# Reset Text
def res_text():
     label.configure(text=currentq, fg="Black")

# ------------------------------------------------
def yes_clicked():
     current_folder = os.path.dirname(os.path.abspath(__file__))
     sound = os.path.join(current_folder, "yippe.mp3")

     pygame.mixer.init()
     pygame.mixer.music.load(sound)
     pygame.mixer.music.play()
     
# ------------------------------------------------
def yes_only():
     no_button.destroy()
     yes_button.configure(font=("Arial", 50),width=27)
     backup_no_button.pack(side="right", pady=15, padx= 30)
# ------------------------------------------------

# Answer Logic
def text_submit():
    global currentans, currentq
    print(currentq,"and ", currentans) # debug
    global current_index
    print(current_index) # debug
    usertxt = entry.get()
    print(usertxt) # debug
    entry.delete(0, tk.END)
    if usertxt == currentans:
        current_index = current_index+1
    if current_index < len(question_keys):
            currentq = question_keys[current_index]
            currentans = questions[currentq]
            label.configure(text=currentq, fg="Black")
    elif current_index > 3:
         surpise()     

# ------------------------------------------------

# Special Suprise
def surpise():
     if current_index > 3:
          label.destroy()
          entry.destroy()
          button.destroy()
          hint_button.destroy()
     question = tk.Label(root, text="Will you answer this final question? ", font=("Arial", 20))
     question2 = tk.Label(root, text="Will you go to prom with me?", font=("Arial", 20))
     question.pack(pady=10)
     question2.pack(pady=10)
     yes_button.pack(side="left", pady=15, padx= 30)
     no_button.pack(side="right", pady=15, padx= 30)

# ------------------------------------------------

# Initialize GUI

# 1. Initialize the main application window
root = tk.Tk()
root.title("Prom")
root.geometry("450x250")
root.configure(background="SlateBlue2")

# ------------------------------------------------

# 2. Create a basic GUI
label = tk.Label(root, text=question_keys[current_index], font=("Arial", 16))
entry = tk.Entry(root)
entry.configure(width=27, font=("Arial", 20))
button = tk.Button(root, text="Submit!", font=("Arial", 16), command=text_submit)
hint_button = tk.Button(root, text="Hint", font=("Arial", 16), command=hint)
yes_button = tk.Button(root, text="Yes!", font=("Arial", 30), command=yes_clicked)
no_button = tk.Button(root, text="No!", font=("Arial", 8), command=yes_only)
backup_no_button = tk.Button(root, text="No!", font=("Arial", 3))
# ------------------------------------------------

# 3. Place the parts onto the window
label.pack(pady=20)
entry.pack(pady=15)
button.pack(pady=15)
hint_button.pack(side="right", padx=5,pady=5)
# -----------------------------------------------

# 4. Start the event loop to keep the window open
root.mainloop()