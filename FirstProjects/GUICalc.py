import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Calcuator")
root.geometry("450x700")
root.configure(background="Grey")

# Main Objects
# Labels
num_label = tk.Label(root, text=None)
num_label.configure(background="Black", width=64, height=4)
num_label.grid(row=0, column=0, columnspan=3, sticky="ew")

# Buttons
Button_1 = tk.Button(root, width=15, height=7, text="1")
Button_2 = tk.Button(root, width=15, height=7, text="2")
Button_3 = tk.Button(root, width=15, height=7, text="3")
Button_4 = tk.Button(root, width=15, height=7, text="4")
Button_5 = tk.Button(root, width=15, height=7, text="5")
Button_6 = tk.Button(root, width=15, height=7, text="6")
Button_7 = tk.Button(root, width=15, height=7, text="7")
Button_8 = tk.Button(root, width=15, height=7, text="8")
Button_9 = tk.Button(root, width=15, height=7, text="9")
Button_dot = tk.Button(root, width=15, height=7, text=".")
Button_0 = tk.Button(root, width=15, height=7, text="0")
Button_Equals = tk.Button(root, width=15, height=7, text="=")
Button_Plus = tk.Button(root, width=15, height=2, text="+")

Button_Plus.grid(row =1, column=0, padx=(0,240), pady=(15,0))
Button_1.grid(row=2, column= 0, padx=(0,240), pady=(15,0))
Button_2.grid(row=2, column= 0, padx=(27,0) ,pady=(15,0))
Button_3.grid(row=2, column= 0, padx=(293,0) ,pady=(15,0))
Button_4.grid(row=3, column= 0, padx=(0,240), pady=(15,0))
Button_5.grid(row=3, column= 0, padx=(27,0) ,pady=(15,0))
Button_6.grid(row=3, column= 0, padx=(293,0) ,pady=(15,0))
Button_7.grid(row=4, column= 0, padx=(0,240), pady=(15,0))
Button_8.grid(row=4, column= 0, padx=(27,0) ,pady=(15,0))
Button_9.grid(row=4, column= 0, padx=(293,0) ,pady=(15,0))
Button_dot.grid(row=5, column= 0, padx=(0,240), pady=(15,0))
Button_0.grid(row=5, column= 0, padx=(27,0) ,pady=(15,0))
Button_Equals.grid(row=5, column= 0, padx=(293,0) ,pady=(15,0))

root.mainloop()