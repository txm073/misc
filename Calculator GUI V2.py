import tkinter as tk

gui = tk.Tk()
gui.title("Calculator User Interface")
gui.geometry("400x539+100+100")
gui.resizable(False, False)
gui.configure(bg="#4C4A48")

def plus_click():
    display.insert(tk.END, "+")

def minus_click():
    display.insert(tk.END, "-")

def times_click():
    display.insert(tk.END, "x")

def divide_click():
    display.insert(tk.END, "÷")

def equals_click():
    for x in range(6):
        display.insert(tk.END,("\n "))
    display.insert(tk.END,f"Answer = ")

def pi_click():
    display.insert(tk.END, "π")

def zero_click():
    display.insert(tk.END, "0")

def dot_click():
    display.insert(tk.END, ".")

def one_click():
    display.insert(tk.END, "1")

def two_click():
    display.insert(tk.END, "2")

def three_click():
    display.insert(tk.END, "3")

def four_click():
    display.insert(tk.END, "4")

def five_click():
    display.insert(tk.END, "5")

def six_click():
    display.insert(tk.END, "6")

def seven_click():
    display.insert(tk.END, "7")

def eight_click():
    display.insert(tk.END, "8")

def nine_click():
    display.insert(tk.END, "9")

def nothing():
    pass

def clear():
    display.delete(1.0, tk.END)

def click():
    pass

def del_click():
    x = display.get(1.0,tk.END)
    display.delete(1.0,tk.END)
    display.insert(tk.END,x[:len(x)-2])

menu_frame = tk.Frame(gui)
menu_frame.pack(anchor=tk.NW)
options_list = ["Save", "Help", "View Code", "Exit"]
options = tk.StringVar()
options.set("Options")

if options == "Exit":
    print("yes")
    gui.quit()
elif options == "Save":
    nothing()
elif options == "Help":
    nothing()
elif options == "View Code":
    nothing()
menu = tk.OptionMenu(menu_frame, options, *options_list)
menu.config(highlightthickness=0, bd=0, width=10, font=("Segoe 10 bold"), bg="#4C4A48", fg="white")
menu.pack(side=tk.LEFT, anchor=tk.W)

display_frame = tk.Frame(gui)
display_frame.config(pady=15,padx=15,bg="#4C4A48")
display_frame.pack(anchor=tk.N)
display = tk.Text(display_frame, height=7, width=45, bg="black", fg="white", font=("none 12"))
display.pack(expand=1,anchor=tk.W)

separator_frame = tk.Frame(gui)
separator_frame.pack(side=tk.LEFT,anchor=tk.W)
invis_label = tk.Label(separator_frame,text="HI",width=1,bg="#4C4A48",fg="#4C4A48")
invis_label.pack()

separator_frame_2 = tk.Frame(gui)
separator_frame_2.pack(side=tk.RIGHT,anchor=tk.W)
invis_label_2 = tk.Label(separator_frame_2,text="HI",width=1,bg="#4C4A48",fg="#4C4A48")
invis_label_2.pack()

separator_frame_3 = tk.Frame(gui,bg="#4C4A48")
separator_frame_3.pack(side=tk.BOTTOM,anchor=tk.S,fill=tk.X)
invis_label_3 = tk.Label(separator_frame_3,text="HI",bg="#4C4A48",fg="#4C4A48",font=("helvetica 4"))
invis_label_3.pack()

functions_frame = tk.Frame(gui, bg="#4C4A48")
functions_frame.pack(side=tk.TOP, anchor=tk.N)
func_list = [tk.Button(functions_frame,text=s,height=1,width=8,bg="silver",font=("none 12 bold"),command=click)
for s in ["𝑥ⁿ","ⁿ√𝑥","(",")",".↔/","x10ⁿ","Ans"]]

for i,btn in enumerate(func_list):
    tk.Grid.rowconfigure(functions_frame,1,weight=1)
    tk.Grid.columnconfigure(functions_frame,i,weight=1)
    btn.grid(row=0,column=i,padx=5,pady=5,sticky="NSEW")
btn_frame = tk.Frame(gui,bg="#4C4A48")
btn_frame.pack(fill=tk.BOTH)

number_frame = tk.Frame(btn_frame, bg="#4C4A48")
number_frame.pack(side=tk.LEFT,anchor=tk.W,fill=tk.Y)

one = tk.Button(number_frame,text=("1"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=one_click).grid(row=2,column=0,padx=5,pady=6,sticky="NSEW")
two = tk.Button(number_frame,text=("2"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=two_click).grid(row=2,column=1,padx=5,pady=6,sticky="NSEW")
three = tk.Button(number_frame,text=("3"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=three_click).grid(row=2,column=2,padx=5,pady=6,sticky="NSEW")
four = tk.Button(number_frame,text=("4"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=four_click).grid(row=1,column=0,padx=5,pady=6,sticky="NSEW")
five = tk.Button(number_frame,text=("5"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=five_click).grid(row=1,column=1,padx=5,pady=6,sticky="NSEW")
six = tk.Button(number_frame,text=("6"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=six_click).grid(row=1,column=2,padx=5,pady=6,sticky="NSEW")
seven = tk.Button(number_frame,text=("7"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=seven_click).grid(row=0,column=0,padx=5,pady=6,sticky="NSEW")
eight = tk.Button(number_frame,text=("8"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=eight_click).grid(row=0,column=1,padx=5,pady=6,sticky="NSEW")
nine = tk.Button(number_frame,text=("9"),padx=5,pady=2,width=4,height=2,bg="white",font=("none 14 bold"),command=nine_click).grid(row=0,column=2,padx=5,pady=6,sticky="NSEW")
pi = tk.Button(number_frame,text="π",padx=5,pady=2,bg="white",width=4,height=2,command=pi_click,font=("none 14 bold")).grid(row=3,column=2,padx=5,pady=6,sticky="NSEW")
dot = tk.Button(number_frame,text=".",padx=5,pady=2,bg="white",width=4,height=2,command=dot_click,font=("none 14 bold")).grid(row=3,column=1,padx=5,pady=6,sticky="NSEW")
zero = tk.Button(number_frame,text="0",padx=5,pady=2,bg="white",width=4,height=2,command=zero_click,font=("none 14 bold")).grid(row=3,column=0,padx=5,pady=6,sticky="NSEW")

operations_frame = tk.Frame(btn_frame,bg="#4C4A48")
operations_frame.pack(fill=tk.BOTH)

clear = tk.Button(operations_frame,text="Clear",bg="silver",font=("none 12 bold"),height=2,command=clear)
clear.pack(fill=tk.BOTH,padx=5,pady=5)

delete = tk.Button(operations_frame,text="Delete",bg="silver",font=("none 12 bold"),height=2,command=del_click)
delete.pack(fill=tk.BOTH,padx=5,pady=5)

top_operations = tk.Frame(operations_frame,bg="#4C4A48")
top_operations.pack(fill=tk.X)

sub_operations = tk.Frame(operations_frame,bg="#4C4A48")
sub_operations.pack(fill=tk.X)

plus_frame = tk.Frame(top_operations,bg="#4C4A48")
plus_frame.pack(anchor=tk.W,side=tk.LEFT)
plus = tk.Button(plus_frame,text="+",bg="silver",font=("none 12 bold"),width=5,height=2,command=plus_click)
plus.pack(padx=5,pady=5)

minus_frame = tk.Frame(sub_operations,bg="#4C4A48")
minus_frame.pack(anchor=tk.W,side=tk.LEFT)
minus = tk.Button(minus_frame,text="-",bg="silver",font=("none 12 bold"),width=5,height=2,command=minus_click)
minus.pack(padx=5,pady=5)

times_frame = tk.Frame(top_operations,bg="#4C4A48")
times_frame.pack(anchor=tk.E,side=tk.RIGHT)
times = tk.Button(times_frame,text="x",bg="silver",font=("none 12 bold"),width=5,height=2,command=times_click)
times.pack(padx=5,pady=5)

divide_frame = tk.Frame(sub_operations,bg="#4C4A48")
divide_frame.pack(anchor=tk.E,side=tk.RIGHT)
divide = tk.Button(divide_frame,text="÷",bg="silver",font=("none 12 bold"),width=5,height=2,command=divide_click)
divide.pack(padx=5,pady=5)

equals_frame = tk.Frame(btn_frame,bg="#4C4A48")
equals_frame.pack(fill=tk.BOTH)
equals = tk.Button(equals_frame,text="=",bg="silver",font=("none 12 bold"),height=2,command=equals_click)
equals.pack(fill=tk.BOTH,padx=5,pady=6)

gui.mainloop()
