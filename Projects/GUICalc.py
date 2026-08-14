import tkinter as tk
import asyncio
from async_tkinter_loop import async_handler, async_mainloop

# Vars
current_total = None
current_num = None
current_float = None
pending_op = None
currently_floating = False
currentans = None
firstpassednum = None
taking_num = False

# Number pass logic
def take_num(passed_num):
    global firstpassednum
    global taking_num
    global current_num

    if taking_num == True and current_num != None:
        print(passed_num)
        print(currently_floating)
        if currently_floating == False:
            current_num = int(str(current_num) + str(passed_num))
            print(current_num)
            update_gui(text= current_num)
            print(firstpassednum)
        elif currently_floating:
            print("float", current_float)
            print("passednum:",passed_num)
            current_num = float(str(current_float) + "." + str(passed_num))
            update_gui(text= current_num)
            print("Floating", current_num)

    elif firstpassednum == None or current_num == None:
        firstpassednum = passed_num
        current_num = firstpassednum
        update_gui(text= current_num)
        taking_num = True

# OP pass logic
def take_op(passed_op):
    global pending_op
    global current_total
    global currently_floating
    global current_num
    save_first_num()
    if passed_op == "+":
        pending_op = "+"
    elif passed_op == "-":
        pending_op = "-"
    elif passed_op == "*":
        pending_op = "*"
    elif passed_op == "/":
        pending_op = "/"
    elif passed_op == "//":
        pending_op = "//"
    elif passed_op == "%":
        pending_op = "%"
    update_gui(text=pending_op)
    print(pending_op)
    print(current_float)

# Save num
def save_first_num():
    global current_total
    global current_num
    global currently_floating
    print("Current Total: ", current_total)
    if currently_floating == False and current_total == None:
        current_total = current_num
        current_num = None    
    elif currently_floating == False and current_total != None:
        back_eq()
        print(current_total)
    if currently_floating and current_total == None:
            current_total = current_num
            print("Saved Total", current_total)
            current_float == None
            currently_floating = False
            current_num = None
    elif currently_floating and current_num != None:
            back_eq()
            currently_floating = False
            current_num = None
    return current_total

def handle_floats():
    global currently_floating
    global current_float
    global current_num
    
    if current_num == None:
        current_num = 0
    current_float = current_num
    currently_floating = True

# Background answer logic // held in backend
def back_eq():
    global current_total
    global current_num
    global pending_op
    if current_total != None and current_num != None:
        if pending_op == "+":
            current_total = current_total + current_num
            current_num = None
            print("BG ANS: ", current_total)
        elif pending_op == "-":
            current_total = current_total - current_num
            current_num = None
            print("BG ANS: ", current_total)
        elif pending_op == "*":
            current_total = current_total * current_num
            current_num = None
            print("BG ANS: ", current_total)
        elif pending_op == "/":
            current_total = current_total / current_num
            current_num = None
            print("BG ANS: ", current_total)
        elif pending_op == "//":
            current_total = current_total // current_num
            current_num = None
            print("BG ANS: ", current_total)
        elif pending_op == "%":
            current_total = current_total % current_num
            current_num = None
            print("BG ANS: ", current_total)
        

# Final answer logic // shown on GUI
def final_eq():
    final_ans = None
    global currently_floating
    global current_num
    global pending_op
    global current_float
    if current_total != None and current_num != None:
        if pending_op == "+":
            final_ans = current_total + current_num
            update_gui(text=final_ans)
            currently_floating = False
            current_float = None
            pending_op = None
            current_num = None
        if pending_op == "-":
            final_ans = current_total - current_num
            update_gui(text=final_ans)
            currently_floating = False
            current_float = None
            pending_op = None
            current_num = None
        if pending_op == "*":
            final_ans = current_total * current_num
            update_gui(text=final_ans)
            currently_floating = False
            current_float = None
            pending_op = None
            current_num = None
        if pending_op == "/":
            final_ans = current_total / current_num
            update_gui(text=final_ans)
            currently_floating = False
            current_float = None
            pending_op = None
            current_num = None
        if pending_op == "//":
            final_ans = current_total // current_num
            update_gui(text=final_ans)
            currently_floating = False
            current_float = None
            pending_op = None
            current_num = None
        if pending_op == "%":
            final_ans = current_total % current_num
            update_gui(text=final_ans)
            currently_floating = False
            current_float = None
            pending_op = None
            current_num = None
        
# Update GUI
def update_gui(text):
    num_label.configure(text=text, fg="Light Green")

# Clear button logic
def clr_num():
    global current_num
    global taking_num
    global firstpassednum
    global currently_floating
    global current_total

    firstpassednum = None
    current_num = None
    current_total = None
    taking_num  = False
    currently_floating = False

    num_label.configure(text="")

# Initialize main window
root = tk.Tk()
root.title("Calcuator")
root.geometry("1080x985")
root.configure(background="Grey")

# Main Objects
# Labels
num_label = tk.Label(root, text=None)
num_label.configure(background="Black", width=90, height=4, font=("Helvetica", 16))
num_label.grid(row=0, column=0, columnspan=5, sticky="ew")
credits = tk.Label(root, text="By: \nGarrett Fryer" ,font=("Helvetica", 20, "bold"), background="Grey")
credits.grid(row=5,column=4)


# Buttons
Button_1 = tk.Button(root, width=15, height=7, text="1", bd=5,relief="groove", command=lambda: take_num(passed_num=1))
Button_2 = tk.Button(root, width=15, height=7, text="2", bd=5,relief="groove", command=lambda: take_num(passed_num=2))
Button_3 = tk.Button(root, width=15, height=7, text="3", bd=5,relief="groove", command=lambda: take_num(passed_num=3))
Button_4 = tk.Button(root, width=15, height=7, text="4", bd=5,relief="groove", command=lambda: take_num(passed_num=4))
Button_5 = tk.Button(root, width=15, height=7, text="5", bd=5,relief="groove", command=lambda: take_num(passed_num=5))
Button_6 = tk.Button(root, width=15, height=7, text="6", bd=5,relief="groove", command=lambda: take_num(passed_num=6))
Button_7 = tk.Button(root, width=15, height=7, text="7", bd=5,relief="groove", command=lambda: take_num(passed_num=7))
Button_8 = tk.Button(root, width=15, height=7, text="8", bd=5,relief="groove", command=lambda: take_num(passed_num=8))
Button_9 = tk.Button(root, width=15, height=7, text="9", bd=5,relief="groove", command=lambda: take_num(passed_num=9))
Button_dot = tk.Button(root, width=15, height=7, text=".", bd=5,relief="groove", command=lambda: handle_floats())
Button_0 = tk.Button(root, width=15, height=7, text="0", bd=5,relief="groove", command=lambda: take_num(passed_num=0))
Button_Equals = tk.Button(root, width=15, height=7, text="=", bd=5,relief="solid", command=lambda: final_eq())
Button_Plus = tk.Button(root, width=15, height=7, text="+", bd=5,relief="groove", command=lambda: take_op(passed_op="+"))
Button_Minus = tk.Button(root, width=15, height=7, text="-", bd=5,relief="groove", command=lambda: take_op(passed_op="-"))
Button_FloorDiv = tk.Button(root, width=15, height=7, text="//", bd=5,relief="groove", command=lambda: take_op(passed_op="//"))
Button_Modulus = tk.Button(root, width=15, height=7, text="%", bd=5,relief="groove", command=lambda: take_op(passed_op="%"))
Button_Div = tk.Button(root, width=15, height=7, text="/", bd=5,relief="groove", command=lambda: take_op(passed_op="/"))
Button_Multiplication = tk.Button(root, width=15, height=7, text="*", bd=5,relief="groove", command=lambda: take_op(passed_op="*"))
Button_CLR = tk.Button(root, width=15, height=7, text="CLR", bd=5,relief="groove", command=lambda: clr_num())

Button_Multiplication.grid(row=4, column=3, padx=0, pady=10)
Button_Div.grid(row=2, column=3, padx=5, pady=10)
Button_FloorDiv.grid(row=2, column=4, padx=5, pady=10)
Button_Modulus.grid(row=3, column=4, padx=5, pady=10)
Button_Plus.grid(row=4, column=4, padx=5, pady=10)
Button_Minus.grid(row=3, column=3, padx=5, pady=10)
Button_Equals.grid(row=5, column=3, padx=5, pady=10)

Button_1.grid(row=4, column=0, padx=0, pady=10)
Button_2.grid(row=4, column=1, padx=0, pady=10)
Button_3.grid(row=4, column=2, padx=0, pady=10)

Button_4.grid(row=3, column=0, padx=0, pady=10)
Button_5.grid(row=3, column=1, padx=0, pady=10)
Button_6.grid(row=3, column=2, padx=0, pady=10)

Button_7.grid(row=2, column=0, padx=0, pady=10)
Button_8.grid(row=2, column=1, padx=0, pady=10)
Button_9.grid(row=2, column=2, padx=0, pady=10)

Button_dot.grid(row=5, column=1, padx=0, pady=10)
Button_0.grid(row=5, column=0, padx=0, pady=10)
Button_CLR.grid(row=5, column=2, padx=0, pady=10)

# Credits

def rgb_to_hex(rgb):
    return "#%02x%02x%02x" % rgb

async def rgb_credits():
    credit = True
    while credit:
        for g in range(0, 255, 15):
            credits.config(foreground=rgb_to_hex((255, g, 0)))
            await asyncio.sleep(0.03)
        # Transition Green -> Blue
        for r in range(255, 0, -15):
            credits.config(foreground=rgb_to_hex((r, 255, 0)))
            await asyncio.sleep(0.03)
        # Transition Blue -> Red
        for b in range(255, 0, -15):
            credits.config(foreground=rgb_to_hex((0, r if 'r' in locals() else 0, b)))
            await asyncio.sleep(0.03)


start_loop = async_handler(rgb_credits)

root.after(100, start_loop)

async_mainloop(root)
