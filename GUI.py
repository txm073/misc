import time
import threading
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import sys
import os
import re

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.title("Send Messages!")
        self.geometry("400x500+100+100")
        self.resizable(False,False)
        self.container = tk.Frame(self,height=50,width=50)
        self.container.pack(anchor=tk.N,fill=tk.BOTH,expand=True,side=tk.TOP)

        image_exists = True
        try:
            self.image = ImageTk.PhotoImage(Image.open("D:\\Python\\Socket Server\\background.png"))
        except FileNotFoundError:
            print("Could not find background image.")
            image_exists = False
        self.background = tk.Frame(self.container,bg="silver")
        self.background.place(x=0,y=0,relwidth=1,relheight=1)
        if image_exists == True:
            self.img_label = tk.Label(self.background,image=self.image)
            self.img_label.pack(anchor=tk.NW)

        self.login_frame = tk.Frame(self.container,bg="silver")
        self.login_frame.place(x=50,y=50,relwidth=0.75,relheight=0.8)

        self.info_btn = tk.Button(self.login_frame,text="i",width=2,
            font=("times new roman",15,"bold"),command=lambda: self.show_frame("info"))
        self.info_btn.pack(padx=5,pady=5,anchor=tk.NW)

        self.separator = tk.Frame(self.login_frame,bg="silver")
        self.separator.pack(side=tk.TOP,anchor=tk.N)
        self.sep_label = tk.Label(self.separator,text="YOU CAN'T SEE ME!",fg="silver",bg="silver",height=1)
        self.sep_label.pack()

        self.title_label = tk.Label(self.login_frame,text="Log In To The Server",fg="black",bg="silver",font=("calibri",18,"bold"))
        self.title_label.pack(padx=30,pady=10,anchor=tk.CENTER)

        self.user_label = tk.Label(self.login_frame,width=15,bg="silver",text="Enter Username:")
        self.user_label.pack(padx=45,anchor=tk.W)
        self.user_entry = tk.Entry(self.login_frame,width=55)
        self.user_entry.pack(padx=50,pady=3)

        self.pass_label = tk.Label(self.login_frame,width=15,bg="silver",text="Enter Password:")
        self.pass_label.pack(padx=45,anchor=tk.W)
        self.pass_entry = tk.Entry(self.login_frame,width=55,show="*")
        self.pass_entry.pack(padx=50,pady=3)

        self.login_btns_frame = tk.Frame(self.login_frame,bg="silver")
        self.login_btns_frame.pack(padx=44,pady=10,fill=tk.X)

        self.login_btn = tk.Button(self.login_btns_frame,text="Login",font=("calibri",10,"bold"),width=12,command=self.show_main)
        self.login_btn.grid(row=0,column=0,padx=6,pady=5,sticky=tk.W)
        self.exit_btn = tk.Button(self.login_btns_frame,text="Exit",font=("calibri",10,"bold"),width=12,command=sys.exit)
        self.exit_btn.grid(row=0,column=1,padx=6,pady=5,sticky=tk.E)

        self.text = ("Welcome to the Overhill Drive \n"
                        "Local Area Network Server!\n"
                    "You can request to join the server \n"
                    "by clicking the button below and \n"
                        "filling out the form.")

        self.info_frame = tk.Frame(self.container,bg="silver")
        self.info_frame.place(x=50,y=50,relwidth=0.75,relheight=0.8)
        
        self.return_btn = tk.Button(self.info_frame,text="Back",font=("calibri",10,"bold"),command=self.show_login)
        self.return_btn.pack(anchor=tk.NW,padx=5,pady=5)
        self.info_label = tk.Label(self.info_frame,bg="silver",text=self.text,font=("calibri",14,"bold"))
        self.info_label.pack(anchor=tk.CENTER,padx=10,pady=50)
        self.request_btn = tk.Button(self.info_frame,text="Request To Join",font=("calibri",10,"bold"),width=12,command=lambda: self.show_frame("sign up"))
        self.request_btn.pack(anchor=tk.CENTER,padx=30)

        self.request_frame = tk.Frame(self.container,bg="silver")
        self.request_frame.place(x=50,y=50,relwidth=0.75,relheight=0.8)
        self.return_btn = tk.Button(self.request_frame,text="Back",font=("calibri",10,"bold"),command=lambda:self.show_frame("info"))
        self.return_btn.pack(anchor=tk.NW,padx=5,pady=5)
        self.label = tk.Label(self.request_frame,text="Coming soon!")
        self.label.pack()

        self.login_response = tk.Frame(self.container,bg="silver")
        self.login_response.place(x=100,y=320,relwidth=0.5,relheight=0.05)
        self.invalid_label = tk.Label(self.login_response,text="Invalid username or password.",fg="red",bg="silver",font=("calibri",11,"bold"))
        self.invalid_label.pack(anchor=tk.CENTER)
        
        self.main_win = tk.Frame(self.container,bg="blue")
        self.main_win.place(x=0,y=0,relwidth=1,relheight=1)
        self.label2 = tk.Label(self.main_win,text="You are at the main page",fg="black")
        self.label2.pack(anchor=tk.CENTER)
        self.btn2 = tk.Button(self.main_win,text="Back",width=5,command=self.show_login)
        self.btn2.pack(anchor=tk.CENTER)
        self.btn3 = tk.Button(self.main_win,text="Exit",width=5,command=sys.exit)
        self.btn3.pack(anchor=tk.CENTER)

        self.frames = {}
        self.frames["login"] = self.login_frame
        self.frames["main"] = self.main_win
        self.frames["background"] = self.background
        self.frames["wrong credentials"] = self.login_response
        self.frames["info"] = self.info_frame
        self.frames["sign up"] = self.request_frame

        self.show_login()

        self.mainloop()

    def show_login(self):
        self.show_frame("background")
        self.show_frame("login")

    def show_main(self):
        credentials = self.check_login()
        self.reset_fields()
        if credentials == True:
            self.show_frame("main")
        else:
            self.show_login()
            self.show_frame("wrong credentials")

    def check_login(self):
        username = self.user_entry.get()
        password = self.pass_entry.get()

        with open("E:\\Python\\Socket Server\\users.txt","r") as file:
            users = str(file.read()).split(", ")
        with open("E:\\Python\\Socket Server\\passwords.txt","r") as file:
            passwords = str(file.read()).split(", ")

        if not username in users:
            return False
        if not password in passwords:
            return False

        valid_username = False
        valid_password = False
        user_index = 0
        password_index = 0
        for i, x in enumerate(users):
            if x == username:
                user_index = i
                break
        for i, x in enumerate(passwords):
            if x == password:
                password_index = i
                break
        if user_index == password_index:
            return True
        return False

    def show_frame(self,page):
        frame = self.frames[page]
        frame.tkraise()

    def reset_fields(self):
        self.pass_entry.delete(0,tk.END)
        self.user_entry.delete(0,tk.END)


win1 = threading.Thread(target=App)
win1.start()
time.sleep(1)
win1.join()





