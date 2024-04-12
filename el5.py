from tkinter import *
import os
root = Tk()
root.title("rvce_bank")

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = sw / 2 - 633 / 2
y = sh / 2 - 333 / 2
root.geometry(f'{633}x{333}+{int(x)}+{int(y)}')
root.geometry("633x333")
root.config(bg='#7D0541')
"""photo = PhotoImage(file="background.png")
Label(root,image=photo)"""


def openmenu():
    account = accentry.get().upper()
    password= passentry.get().upper()
    path=os.path.exists(accentry.get())
    if(path==True):

        file = open(account, "r")
        s = file.readline().upper().strip()
        t = file.readline().upper().strip()



        u = file.readline().upper().strip()
        if (account == s and password == u):
            notif1.config(fg="light green", bg="#293241", text="Login Successfull")
            page3()
        else:
            notif1.config(fg="#FF2800", bg="#293241", text="Password does not match!")
    else:
        notif1.config(fg="#FF2800",bg="#293241",text="Account does not exist!!")



def login1():
    root2.destroy()
    login()

def login():
    global root1
    root1 = Tk()
    root1.config(bg="#293241")
    root1.title("login_page")
    sw = root1.winfo_screenwidth()
    sh = root1.winfo_screenheight()
    x = sw / 2 - 470 / 2
    y = sh / 2 - 250 / 2
    root1.geometry(f'{470}x{250}+{int(x)}+{int(y)}')
    root1.minsize(470, 250)
    root1.maxsize(470, 250)
    global accentry
    global passentry
    global accvalue
    l = Label(root1, text="Login Credentials\n", font="Times 20 bold", fg="#FE7A15",bg="#293241")
    l.grid(row=0,column=2)
    l.config(justify=CENTER)
    accno = Label(root1, text="Account Number", bg="#293241", fg="#F9D423")
    password = Label(root1, text="Password", bg="#293241", fg="#F9D423")
    Label(root1, text='     ', bg="#293241").grid(row=3, column=2)
    accno.grid(row=1, column=1)
    password.grid(row=2, column=1)
    accvalue = StringVar()
    passvalue = StringVar()
    sp = IntVar(value=1)
    global accentry
    accentry = Entry(root1, textvariable=accvalue)
    passentry = Entry(root1, textvariable=passvalue, show="*")
    accentry.grid(row=1, column=2)
    passentry.grid(row=2, column=2)
    def getvals():
        print("submitted")
    def show():
        if passentry.cget('show') == '*':
            passentry.config(show='')
        else:
            passentry.config(show='*')
    show_password = Checkbutton(root1, text="Show Password", variable=sp, onvalue=1, offvalue=0, command=show, bg="#293241", fg="#FE676E")
    show_password.grid(row=4, column=2)

    def rhome():
        root1.destroy()

    Button(root1, text="Login",bg="cyan", command=lambda:openmenu(), ).grid(row=6, column=2)
    Button(root1,text="Return to homepage",bg="greenyellow",command=lambda:rhome(),).grid(row=10,column=3)
    global notif1
    notif1=Label(root1,bg="#293241",font="comicsansms")
    notif1.grid(row=3,column=2)
    root1.mainloop()




def create():
    pass
def signup():
    global root2
    root2 = Tk()
    root2.title("signup_page")
    root2.config(bg='#2A363B')
    sw = root2.winfo_screenwidth()
    sh = root2.winfo_screenheight()
    x = sw / 2 - 550 / 2
    y = sh / 2 - 400 / 2
    root2.geometry(f'{550}x{400}+{int(x)}+{int(y)}')
    root2.minsize(550,400)
    root2.maxsize(550,400)
    global fentry
    global lentry
    global npassentry
    global amtentry
    l = Label(root2, text="SignUp Credentials\n", font="Times 20 bold", fg="orange", bg="#2A363B")
    l.grid(row=0, column=2)
    fname = Label(root2, text="First Name *", bg='#2A363B', fg="#C06C84").grid(row=2,column=1)
    fvalue = StringVar()
    fentry = Entry(root2, textvariable=fvalue)
    fentry.grid(row=2,column=2)
    lname = Label(root2, text="Last Name",bg='#2A363B', fg="#C06C84").grid(row=4,column=1)
    lvalue = StringVar()
    lentry = Entry(root2, textvariable=lvalue)
    lentry.grid(row=4,column=2)
    phno = Label(root2, text="Phone no *",bg='#2A363B', fg="#C06C84").grid(row=6,column=1)
    phvalue = StringVar()
    phentry = Entry(root2, textvariable=phvalue)
    phentry.grid(row=6,column=2)
    email = Label(root2, text="Email-Id *",bg='#2A363B', fg="#C06C84").grid(row=8,column=1)
    emailvalue = StringVar()
    emailentry = Entry(root2, textvariable=emailvalue)
    emailentry.grid(row=8,column=2)
    npass = Label(root2, text="Create New Password *",bg='#2A363B', fg="#C06C84").grid(row=10, column=1)
    npassvalue = StringVar()
    npassentry = Entry(root2, textvariable=npassvalue, show="*")
    npassentry.grid(row=10,column=2)
    cpass = Label(root2, text="Confirm Password *",bg='#2A363B', fg="#C06C84").grid(row=12, column=1)
    cpassvalue = StringVar()
    cpassentry = Entry(root2, textvariable=cpassvalue, show="*")
    cpassentry.grid(row=12, column=2)
    amt=Label(root2,text="Enter the amount to deposit * \n(minimum balance is Rs.5000)",bg='#2A363B', fg="#C06C84").grid(row=16,column=1)
    minamt=StringVar()
    amtentry=Entry(root2,textvariable=minamt)
    amtentry.grid(row=16,column=2)
    global notif
    notif = Label(root2,bg="#2A363B",font="comicsansms 10 bold")
    notif.grid(row=19,column=2)
    def show1():
        if npassentry.cget('show') == '*' or cpassentry.cget('show') == '*':
            npassentry.config(show='')
            cpassentry.config(show='')
        else:
            npassentry.config(show='*')
            cpassentry.config(show='*')




    def acc():

        if(fentry.get().strip() == "" or phentry.get().strip() == "" or emailentry.get().strip() == "" or npassentry.get().strip() == "" or cpassentry.get().strip() == "" or amtentry.get().strip()==""):
            notif.config(fg="yellow", bg="#2A363B", text="All fields marked * are compulsory!")
        elif(npassentry.get().strip() != cpassentry.get().strip()):
            notif.config(fg="yellow", bg="#2A363B", text="The passwords should match!")

        elif (len(phentry.get()) != 10):
            notif.config(fg="yellow", bg="#2A363B", text="Please enter a valid 10 digit number!")

        elif (not(phentry.get().isdigit())):
            notif.config(fg="yellow",bg="#2A363B",text="Please enter a valid 10 digit number!")

        elif("@" not in emailentry.get()):
            notif.config(fg="yellow",bg="#2A363B",text="Please enter a valid email id")
        elif(int(amtentry.get())<5000):
            notif.config(fg="yellow",bg="#2A363B",text="Minimum balance must be Rs.5000!")
        elif((amtentry.get()).isdigit()==False):
            notif.config(fg="yellow",bg="#2A363B",text="Please enter a valid amount to deposit!!")
        else:
            notif.config(bg="#2A363B",text="                                                                         ")
            newacc()
    def newacc():
            import string
            import random
            n = 10
            res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))
            global c
            c = str(res).upper().strip()
            name=fentry.get().title()+" "+lentry.get().title()
            password=npassentry.get().title()
            balance=amtentry.get()
            file=open(c,"w")
            file.write(c+"\n")
            file.write(name+"\n")
            file.write(password+"\n")
            file.write(balance)
            file.close()
            Label(root2, text=c, bg="#2A363B", fg="white", font="bold").grid(row=19, column=2)
            Label(root2, text='                                                                    ',bg="#2A363B").grid(row=18, column=2)
            Label(root2, text="Your Account number is : ", bg="#2A363B", fg="yellow").grid(row=18, column=2)


    def Close():
        root2.destroy()







    show_password = Checkbutton(root2, text="Show Password", onvalue=1, offvalue=0, command=show1,bg="#2A363B", fg="#5874DC" ).grid(row=14, column=2)
    Label(root2, text="( * : required )",bg="#2A363B", fg="white").grid(row=19, column=1)
    b2 = Button(root2, text="Click here for your account number", command=lambda:acc(),bg="light blue").grid(row=18,column=2)
    Button(root2, text="Login", command=login1, bg="greenyellow").grid(row=22, column=2)
    Button(root2, text="close", command=Close, bg="cyan").grid(row=23, column=3)

    root2.mainloop()


def page3():
    root3 = Tk()
    sw = root3.winfo_screenwidth()
    sh = root3.winfo_screenheight()
    x = sw/2 - 400/2
    y = sh/2 - 300/2
    root3.geometry(f'{400}x{300}+{int(x)}+{int(y)}')
    root3.config(bg="#582841")
    root3.minsize(400,300)
    root3.maxsize(400,300)
    root3.title("Account")
    """width = root3.winfo_screenwidth()
    height = root3.winfo_screenheight()
    root3.geometry("%dx%d" % (width, height))"""
    Label(root3, text="Welcome\n", font="Times 20 bold", bg="#582841", fg="#F99E4C", justify=CENTER).grid(row=0, column=3)
    Button(root3, text="View account balance",command=page5,borderwidth=5,anchor="w", bg="pink", relief=RIDGE).grid(row=2,column=2)
    Label(root3,text="           ", bg="#582841").grid(row=3, column=1)
    Button(root3, text="Transfer amount",command=page4, borderwidth=5, anchor="w", bg="light blue", relief=RIDGE).grid(row=4, column=2)
    Label(root3,text="           ", bg="#582841").grid(row=5, column=1)
    Button(root3, text="Withdraw amount",command=page6,borderwidth=5, bg="#EF4648", relief=RIDGE).grid(row=6,column=2)
    Label(root3,text="           ", bg="#582841").grid(row=7, column=1)
    Button(root3, text="Deposit amount",command=page7,borderwidth=5,  bg="yellowgreen", relief=RIDGE).grid(row=8,column=2)
    Button(root3, text="Logout", command=lambda:logout(),borderwidth=5, bg="gold", relief=RAISED).grid(row=10,column=7)

    def logout():
        root3.destroy()
        root1.destroy()
        #notif1.config(fg="light green",bg="#293241",text="Logout Successfull")




    root3.mainloop()
def page5():
    root5=Tk()
    root5.title("View balance")
    root5.config(bg="#305F72")
    sw = root5.winfo_screenwidth()
    sh = root5.winfo_screenheight()
    x = (sw/2) - (350/2)
    y = (sh/2) - (120/2)
    root5.geometry(f'{300}x{120}+{int(x)}+{int(y)}')
    root5.minsize(350,120)
    root5.maxsize(350,120)

    """width=root5.winfo_screenwidth()
    height=root5.winfo_screenheight()
    root5.geometry("%dx%d" % (width,height))"""
    acc=accentry.get().upper().strip()
    file=open(acc,"r")
    n=file.readlines()
    file.close()
    st=n[1].strip()+" your balance is Rs."+n[3]
    Label(root5, text="", bg="#305F72").grid(row=0)
    Label(root5,text=st, bg="#305F72", fg="white", font="Times 14", justify=CENTER).grid(row=1,column=1)
    Label(root5, text="", bg="#305F72").grid(row=2)
    Button(root5,text="Return to home",bg="greenyellow",command=lambda:home2()).grid(row=3, column=1)
    def home2():
        root5.destroy()



def page4():
    root4=Tk()
    root4.title("Transfer amount")
    root4.config(bg="#305F72")
    width = root4.winfo_screenwidth()
    height = root4.winfo_screenheight()
    x = (width/2) - (570/2)
    y = (height/2) - (180/2)
    root4.minsize(570, 180)
    root4.maxsize(570, 180)
    root4.geometry(f'{570}x{180}+{int(x)}+{int(y)}')
    Label(root4, text="Enter the receiver's account number", bg="#305F72", fg="white", font="Times 14").grid(row=1,column=1)
    Label(root4, text="Enter the amount to transfer", bg="#305F72", fg="white", font="Times 14").grid(row=2, column=1)
    Label(root4, text="Enter your password", bg="#305F72", fg="white", font="Times 14").grid(row=3, column=1)
    Button(root4, text="Return to home", command=lambda: home(), bg="light green").grid(row=6, column=1)
    Button(root4, text="Transfer", command=lambda: transfer(), bg="cyan").grid(row=4, column=2)
    taccno=StringVar()
    amtvalue = StringVar()
    pinvalue=StringVar()
    taccentry=Entry(root4,textvariable=taccno)
    taccentry.grid(row=1,column=2)
    amtentry=Entry(root4,textvariable=amtvalue)
    amtentry.grid(row=2,column=2)
    pinentry=Entry(root4,textvariable=pinvalue,show="*")
    pinentry.grid(row=3,column=2)
    notif2=Label(root4,font="Times 12", bg="#305F72")
    notif2.grid(row=5,column=2)
    account=str(accentry.get().upper().strip())
    def home():
        root4.destroy()
    def transfer():
        amt=int(amtentry.get())
        file=open(account,"r")
        n=file.readlines()
        file.close()
        bal=int(n[3])
        cpass=n[2].upper().strip()
        epass=pinentry.get().upper().strip()
        path=os.path.exists(taccentry.get().upper())
        if(epass==cpass and path==True):
            if(bal<amt):
                notif2.config(fg="yellow",bg="#305F72",text="Insufficient balance!")
            elif((bal-amt)<5000 or bal==amt):
                notif2.config(fg="yellow",bg="#305F72",text="Minimum balance should be Rs.5000")
            elif(amt<=0):
                notif2.config(fg="yellow",bg="#305F72",text="Please enter a valid amount to transfer!")
            else:
                n[3]=str(bal-amt)
                file=open(account,"w")
                file.writelines(n)
                file.close()
                text="Rs."+str(amt)+" transferred to account "+ taccentry.get().upper()
                notif2.config(fg="yellow",bg="#305F72",text=text)

        elif(path==False):
            notif2.config(fg="yellow",bg="#305F72",text="Account does not exist!")
        else:
            notif2.config(fg="yellow",bg="#305F72",text="Password does not match!")


def page6():
    root6=Tk()
    root6.title("Withdraw")
    root6.config(bg="#305F72")
    width = root6.winfo_screenwidth()
    height = root6.winfo_screenheight()
    x = (width / 2) - (570 / 2)
    y = (height / 2) - (180 / 2)
    root6.minsize(570, 180)
    root6.maxsize(570, 180)
    root6.geometry(f'{570}x{180}+{int(x)}+{int(y)}')
    Label(root6,text="Enter amount to withdraw:",bg="#305F72",fg="white", font="Times 14").grid(row=1,column=1)
    Label(root6,text="Enter your password:",bg="#305F72",fg="white", font="Times 14").grid(row=2,column=1)
    Button(root6,text="Return to home",bg="pink",command=lambda:home3()).grid(row=6,column=1)
    Button(root6,text="Withdraw",bg="greenyellow",command=lambda:withdraw()).grid(row=5,column=2)
    amtval=StringVar()
    pinval=StringVar()
    amtentry=Entry(root6,textvariable=amtval)
    amtentry.grid(row=1,column=2)
    pinentry=Entry(root6,textvariable=pinval,show="*")
    pinentry.grid(row=2,column=2)
    notif3=Label(root6,font="Times",bg="#305F72")
    notif3.grid(row=4,column=2)

    def home3():
        root6.destroy()

    def withdraw():
        amt=int(amtentry.get())
        account=accentry.get().upper()
        file=open(account,"r")
        n=file.readlines()
        file.close()
        bal=int(n[3])
        cpass=n[2].upper().strip()
        if(cpass==pinentry.get().strip().upper()):
            if(bal<amt):
                notif3.config(fg="yellow",bg="#305F72",text="Insufficient balance!!")
            elif(bal==amt or (bal-amt)<5000):
                notif3.config(fg="yellow",bg="#305F72",text="Minimum balance should be Rs.5000")
            elif(amt<=0):
                notif3.config(fg="yellow",bg="#305F72",text="Please enter valid amount to withdraw!!")
            else:
                n[3] = str(bal - amt)
                file1 = open(account, "w")
                file1.writelines(n)
                file1.close()
                text1="Withdrawal of amount Rs."+str(amt)+" successfull!"
                notif3.config(fg="yellow",bg="#305F72",text=text1)
        else:
            notif3.config(fg="yellow",bg="#305F72",text="Password mismatch!!")

def page7():
    root7=Tk()
    root7.title("Deposit")
    root7.config(bg="#305F72")
    width = root7.winfo_screenwidth()
    height = root7.winfo_screenheight()
    x = (width / 2) - (550 / 2)
    y = (height / 2) - (180 / 2)
    root7.minsize(550, 180)
    root7.maxsize(550, 180)
    root7.geometry(f'{550}x{180}+{int(x)}+{int(y)}')
    Label(root7,text="Enter amount to deposit:",bg="#305F72",fg="white",font="Times 14").grid(row=1,column=1)
    Label(root7,text="Enter your password:",bg="#305F72",font="Times 14",fg="white").grid(row=2,column=1)
    Button(root7,text="Return to home",command=lambda:home4(),bg="greenyellow").grid(row=6,column=1)
    Button(root7,text="Deposit",command=lambda:deposit(),bg="orange").grid(row=5,column=2)
    amtval=StringVar()
    pinval=StringVar()
    amtentry=Entry(root7,textvariable=amtval)
    amtentry.grid(row=1,column=2)
    pinentry=Entry(root7,textvariable=pinval,show="*")
    pinentry.grid(row=2,column=2)
    notif4=Label(root7,font="comicsansms",bg="#305F72")
    notif4.grid(row=4,column=2)

    def home4():
        root7.destroy()

    def deposit():
        amt=int(amtentry.get())
        account=accentry.get().upper()
        file=open(account,"r")
        n=file.readlines()
        file.close()
        bal=int(n[3])
        cpass=n[2].upper().strip()
        if(amt<=0):
            notif4.config(fg="yellow",text="Please enter valid amount to deposit!!",bg="#305F72")
        elif(cpass==pinentry.get().strip().upper()):
            n[3] = str(bal + amt)
            file1 = open(account, "w")
            file1.writelines(n)
            file1.close()
            text1="Deposit of amount Rs."+str(amt)+" successfull!"
            notif4.config(fg="yellow",bg="#305F72",text=text1)
        else:
            notif4.config(fg="yellow",bg="#305F72",text="Password mismatch!!")





label = Label(text="Welcome to RVCE Bank", bg="#057D41", fg="black", padx=25, font="comicsansms 20 bold", borderwidth=10,
        relief=GROOVE)
label.pack(fill="x")
frame = Frame(root, borderwidth=3, bg='grey')
frame.pack(pady=5, padx=15,anchor="nw")
frame2 = Frame(root, borderwidth=3,bg='grey')
frame2.pack(pady=5,padx=30,anchor='nw')
Button(frame, fg="red", bg="yellowgreen",font='arial 10 bold', text="Login", borderwidth=15, command=login, relief=RAISED).pack(side=RIGHT)
Button(frame, fg="red", bg="yellowgreen", font='arial 10 bold', text="SignUp", borderwidth=15, command=signup, relief=RAISED).pack(side=RIGHT)
"""widget = Canvas(root, width=400, height=400)
widget.create_line(0, 200, 400, 200, fill='black', )"""
root.mainloop()
