import tkinter as tk

gui = tk.Tk()
gui.title("Calculator User Interface")
gui.geometry("420x540+100+100")
gui.resizable(False, False)
gui.configure(bg="#4C4A48")

def nothing():
    pass

def click():
    pass

menu_frame = tk.Frame(gui)
menu_frame.pack(anchor=tk.NW)
options_list = ["Save", "Help", "View Code", "Exit"]
options = tk.StringVar(menu_frame)
options.set("Options")
if options == "Exit":
    gui.destroy
elif options == "Save":
    nothing()
elif options == "Help":
    nothing()
elif options == "View Code":
    nothing()
menu = tk.OptionMenu(menu_frame, options, *options_list)
menu.config(highlightthickness=0, bd=0, width=10, font=("Segoe 11"), bg="#4C4A48", fg="white")
menu.pack(side=tk.LEFT, anchor=tk.W)

display_frame = tk.Frame(gui)
display_frame.pack(anchor=tk.N)
display = tk.Text(display_frame, height=7, width=45, bg="black", fg="white")
display.pack(expand=1,anchor=tk.W)

separator_frame = tk.Frame(gui,bg="#4C4A48")
separator_frame.pack(anchor=tk.N)
invis_label = tk.Label(separator_frame,text="YOU CANT SEE MEEEEE!",bg="#4C4A48",fg="#4C4A48")
invis_label.pack()

functions_frame = tk.Frame(gui, bg="#4C4A48")
functions_frame.pack(side=tk.TOP, anchor=tk.N)
func_list = [tk.Button(functions_frame,text=s,height=2,width=8,bg="silver",font=("none 12 bold"),command=click)
for s in ["𝑥ⁿ","ⁿ√𝑥","(",")",".↔/","x10ⁿ","Ans"]]

for i,btn in enumerate(func_list):
    tk.Grid.rowconfigure(functions_frame,1,weight=1)
    tk.Grid.columnconfigure(functions_frame,i,weight=1)
    btn.grid(row=0,column=i,padx=5,pady=5,sticky="NSEW")
btn_frame = tk.Frame(gui,bg="#4C4A48")
btn_frame.pack()

number_frame = tk.Frame(btn_frame, bg="#4C4A48")
number_frame.grid(row=0,column=0)
number_list = []
for i in range(9,0,-1):
    number_list.append(tk.Button(number_frame,text=str(i),width=4,height=2,bg="white",font=("none 14 bold"),command=click))
number_list.append(tk.Button(number_frame,text="π",bg="white",width=4,height=2,command=click,font=("none 14 bold")))
number_list.append(tk.Button(number_frame,text=".",bg="white",width=4,height=2,command=click,font=("none 14 bold")))
number_list.append(tk.Button(number_frame,text="0",bg="white",width=4,height=2,command=click,font=("none 14 bold")))
for i, btn in enumerate(number_list):
    c = 2-(i % 3)
    r = int(i/3)
    tk.Grid.rowconfigure(number_frame,r,weight=1)
    tk.Grid.columnconfigure(number_frame,c,weight=1)
    btn.grid(row=r,column=c,padx=5,pady=5,sticky="NSEW")

operations_frame = tk.Frame(btn_frame,bg="#4C4A48")
operations_frame.grid(row=0,column=1)

main_ops = []
main_ops.append(tk.Button(operations_frame,text="+",bg="silver",font=("none 12 bold"),height=5,width=5,command=click))
main_ops.append(tk.Button(operations_frame,text="-",bg="silver",font=("none 12 bold"),height=5,width=5,command=click))
main_ops.append(tk.Button(operations_frame,text="x",bg="silver",font=("none 12 bold"),height=5,width=5,command=click))
main_ops.append(tk.Button(operations_frame,text="÷",bg="silver",font=("none 12 bold"),height=5,width=5,command=click))
for i, btn in enumerate(main_ops):
    c = i % 2
    r = int(i/2)
    tk.Grid.rowconfigure(operations_frame,r,weight=1)
    tk.Grid.columnconfigure(operations_frame,c,weight=1)
    btn.grid(row=r,column=c,padx=5,pady=5,sticky="NSEW")

gui.mainloop()
