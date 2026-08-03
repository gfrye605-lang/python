import tkinter as tk
import time

# -----------------------------------------------

# Question & Answer List
questions = {"What was the biggest promise I made to you":
             "To be here with you forever",
             "What do we always say to each other?":
             "I love you",
             "How long have we been dating for": "1 year, 3 months",
             "When do couples usually give promise rings":
             "6 months"}

# ------------------------------------------------

# Vars
question_keys = list(questions.keys())
current_index = 0
currentq = question_keys[current_index]
currentans = questions[currentq]

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
     question = tk.Label(root, text="Will you pr💍mise to ", font=("Arial", 24))
     question2 = tk.Label(root, text="go to prom with me?", font=("Arial", 24))
     question.pack (pady=10)
     question2.pack (pady=10)

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

# ------------------------------------------------

# 3. Place the parts onto the window
label.pack(pady=20)
entry.pack(pady=15)
button.pack(pady=15)

# -----------------------------------------------

# 4. Start the event loop to keep the window open
root.mainloop()