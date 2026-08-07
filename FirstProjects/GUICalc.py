import tkinter as tk

# Vars
current_num = None
current_op  = None
op = None
equate = False
passednum1 = None
firstpassednum = None
taking_part1 = False
stored_num = None
num_groups = {}
op_groups = []

# Number pass logic
def take_num(passed_num):
    global firstpassednum
    global taking_part1
    global current_num

    if taking_part1 == True:
        print(passed_num)
        current_num = int(str(current_num) + str(passed_num))
        print(current_num)
        update_gui(text= current_num)
        print(firstpassednum)
    elif firstpassednum == None:
        firstpassednum = passed_num
        current_num = firstpassednum
        update_gui(text= current_num)
        taking_part1 = True

# Infinitly store numbers
def store_numbers(savednum):
    global stored_num
    i = 1
    while f"group_{i}" in num_groups:
        i += 1  

    num_groups[f"group_{i}"] = savednum
    print("Updated Groups:", num_groups)
    stored_num = i


# OP pass logic

def take_op(passed_op):
    savednum = current_num
    print(savednum)
    store_numbers(savednum)
    print("Num groups: ", num_groups)
    clr_num()
    if passed_op == "+":
        op_groups.append("+")
        print(op_groups)
    elif passed_op == "-":
        op_groups.append("-")
        print(op_groups)
    update_gui(text=op)
    return savednum

# Equate logic
def eq():
    global stored_num
    i = stored_num
    for count in range(1, i + 1):
        group_key = f"group_{count}"
        
        locals()[f"num{count}"] = num_groups[group_key]
        print(locals)


# Update GUI
def update_gui(text):
    text = current_num
    num_label.configure(text=text, fg="White")

# Clear button logic
def clr_num():
    global current_num
    global taking_part1
    global firstpassednum

    firstpassednum = None
    current_num = None
    taking_part1 = False

    num_label.configure(text="")

# Initialize main window
root = tk.Tk()
root.title("Calcuator")
root.geometry("1280x680")
root.configure(background="Grey")

# Main Objects
# Labels
num_label = tk.Label(root, text=None)
num_label.configure(background="Black", width=64, height=4, font=("Helvetica", 16))
num_label.grid(row=0, column=0, columnspan=3, sticky="ew")

# Buttons
Button_1 = tk.Button(root, width=15, height=7, text="1", command=lambda: take_num(passed_num=1))
Button_2 = tk.Button(root, width=15, height=7, text="2", command=lambda: take_num(passed_num=2))
Button_3 = tk.Button(root, width=15, height=7, text="3", command=lambda: take_num(passed_num=3))
Button_4 = tk.Button(root, width=15, height=7, text="4", command=lambda: take_num(passed_num=4))
Button_5 = tk.Button(root, width=15, height=7, text="5", command=lambda: take_num(passed_num=5))
Button_6 = tk.Button(root, width=15, height=7, text="6", command=lambda: take_num(passed_num=6))
Button_7 = tk.Button(root, width=15, height=7, text="7", command=lambda: take_num(passed_num=7))
Button_8 = tk.Button(root, width=15, height=7, text="8", command=lambda: take_num(passed_num=8))
Button_9 = tk.Button(root, width=15, height=7, text="9", command=lambda: take_num(passed_num=9))
Button_dot = tk.Button(root, width=15, height=7, text=".")
Button_0 = tk.Button(root, width=15, height=7, text="0", command=lambda: take_num(passed_num=0))
Button_Equals = tk.Button(root, width=15, height=7, text="=", command=lambda: eq())
Button_Plus = tk.Button(root, width=15, height=7, text="+", command=lambda: take_op(passed_op="+"))
Button_Minus = tk.Button(root, width=15, height=7, text="-", command=lambda: take_op(passed_op="-"))
Button_FloorDiv = tk.Button(root, width=15, height=7, text="//", command=lambda: take_op(passed_op="//"))
Button_Modulus = tk.Button(root, width=15, height=7, text="%", command=lambda: take_op(passed_op="%"))
Button_Div = tk.Button(root, width=15, height=7, text="/", command=lambda: take_op(passed_op="/"))
Button_Multiplication = tk.Button(root, width=15, height=7, text="*", command=lambda: take_op(passed_op="*"))
Button_CLR = tk.Button(root, width=15, height=7, text="CLR", command=lambda: clr_num())

Button_Multiplication.grid(row=4, column=3, padx=5, pady=5)
Button_Div.grid(row=2, column=3, padx=5, pady=5)
Button_FloorDiv.grid(row=2, column=4, padx=5, pady=5)
Button_Modulus.grid(row=3, column=4, padx=5, pady=5)
Button_Plus.grid(row=4, column=4, padx=5, pady=5)
Button_Minus.grid(row=3, column=3, padx=5, pady=5)
Button_Equals.grid(row=5, column=3, padx=5, pady=5)

Button_1.grid(row=4, column=0, padx=5, pady=5)
Button_2.grid(row=4, column=1, padx=5, pady=5)
Button_3.grid(row=4, column=2, padx=5, pady=5)

Button_4.grid(row=3, column=0, padx=5, pady=5)
Button_5.grid(row=3, column=1, padx=5, pady=5)
Button_6.grid(row=3, column=2, padx=5, pady=5)

Button_7.grid(row=2, column=0, padx=5, pady=5)
Button_8.grid(row=2, column=1, padx=5, pady=5)
Button_9.grid(row=2, column=2, padx=5, pady=5)

Button_dot.grid(row=5, column=1, padx=5, pady=5)
Button_0.grid(row=5, column=0, padx=5, pady=5)
Button_CLR.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()