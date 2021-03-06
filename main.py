from tkinter import *
import Final_Data
import os


# Designing window for registration


def register():
    global register_screen
    register_screen = Toplevel(mainRoot)
    register_screen.title("Register")
    register_screen.geometry("600x550")
    register_screen.config(bg='sky blue')


    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Please Register For Your school ID",bg='black',fg='white',font=("Times", "20", "bold italic")).pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen,bg='yellow', text="Username * ",font=('STYLE_BRACEBAD, 20'))
    username_lable.pack()
    username_entry = Entry(register_screen ,bg='white',fg='black', textvariable=username,font=("Times", "25", "bold italic"))
    username_entry.pack()
    password_lable = Label(register_screen,bg='yellow', text="Password * ",font=('STYLE_BRACEBAD, 20'))
    password_lable.pack()
    password_entry = Entry(register_screen,bg='white',fg='black',textvariable=password, show='*',font=("Times", "25", "bold italic"))

    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=2, fg='white',bg="red",font=('STYLE_BRACEBAD, 13'), command=registerNewUser).pack()


#different windows for loging

def signup():
    global signupScreen
    signupScreen = Toplevel(mainRoot)
    signupScreen.title("sign-up")
    signupScreen.geometry("400x350")
    Label(signupScreen, text="Please Enter School ID",bg='green',font=("Times", "20", "bold italic")).pack()
    Label(signupScreen, text="").pack()
    signupScreen.config(bg="wheat")

    global usernameVerify
    global passwordVerify

    usernameVerify = StringVar()
    passwordVerify = StringVar()

    global usernameSignupEntry
    global passwordSignupENtry

    Label(signupScreen, text="Username * ",font=('STYLE_BRACEBAD, 20')).pack()
    usernameSignupEntry = Entry(signupScreen,bg='yellow' ,font=('STYLE_BRACEBAD, 20'), textvariable=usernameVerify)
    usernameSignupEntry.pack()
    Label(signupScreen, text="",font=('STYLE_BRACEBAD, 20')).pack()
    Label(signupScreen, text="Password * ",font=('STYLE_BRACEBAD, 20')).pack()
    passwordSignupENtry = Entry(signupScreen,bg='yellow' ,font=('STYLE_BRACEBAD, 20'),textvariable=passwordVerify, show='*')
    passwordSignupENtry.pack()
    Label(signupScreen, text="",font=('STYLE_BRACEBAD, 20')).pack()
    Button(signupScreen, text="Login",bg='red'  ,width=10, height=1, font=('STYLE_BRACEBAD,20'),command=signupVerify).pack()


# Implementing event on register button

def registerNewUser():
    usernameInformatio = username.get()
    passwordInformaion = password.get()

    file = open(usernameInformatio, "w")
    file.write(usernameInformatio + "\n")
    file.write(passwordInformaion)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button

def signupVerify():
    username1 = usernameVerify.get()
    password1 = passwordVerify.get()
    usernameSignupEntry.delete(0, END)
    passwordSignupENtry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            signupSucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def signupSucess():
    global signupSuccessScreen
    signupSuccessScreen = Toplevel(signupScreen)
    signupSuccessScreen.title("Success")
    signupSuccessScreen.geometry("500x500")
    Label(signupSuccessScreen, text="Login Success").pack()
    Button(signupSuccessScreen, text="OK", command=delete_login_success).pack()



# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(signupScreen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("800x800")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="exit", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(signuScreen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    signupSuccessScreen.destroy()





def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# showing the first screen
def mainRootScreen():
    global mainRoot
    mainRoot = Tk()
    mainRoot.geometry("700x400")

    mainRoot.title("ABC SCHOOL")
    mainRoot.config(bg="yellow")
    mylabel=Label(mainRoot)
    mylabel.place(x=0,y=0)
    Label(text="ABC SCHOOL",bg="red",fg='white', width="300", height="2",font=("Times", "40", "bold italic") ).pack()
    Label(text="").pack()
    Button(text="Sign UP", fg='blue',bg='yellow', height="2", width="30",font=('STYLE_BRACEBAD, 15'), command=signup).pack()
    Label(text="").pack()
    Button(text="Register",fg='blue', bg='yellow',height="2", width="30",font=('STYLE_BRACEBAD, 15'), command=register).pack()

    mainRoot.mainloop()


mainRootScreen()

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1450x750+0+0")
        self.root.config(bg="white")

#======================= declaring the variables ============================

        StdID=StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        Age = StringVar()
        City = StringVar()
        Contact = StringVar()
        Email = StringVar()
#======================= functions ===========================================
        def iExit():
            iExit=tkinter.messagebox.askyesno("student management system","confirm if you want to exit")
            if iExit >0:
                root.destroy()
                return
        def clearData():
            self.e1.delete(0,END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
            self.e5.delete(0, END)
            self.e6.delete(0, END)
            self.e7.delete(0, END)
            self.e8.delete(0, END)

        def addData():
            if(len(StdID.get())!=0):
                Final_Data.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Address.get(), Age.get(), City.get(), Contact.get(), Email.get())
                student_list.delete(0,END)
                student_list.insert(END,(StdID.get() , Firstname.get(), Lastname.get() ,Address.get() , Age.get(), City.get(), Contact.get(), Email.get()))

        def displayData():
            student_list.delete(0,END)
            for row in Final_Data.viewData():
                student_list.insert(END,row,str(""))

        def StudentRec(event):
            global sd
            searchStd = student_list.curselection()[0]
            sd=student_list.get(searchStd)

            self.e1.delete(0, END)
            self.e1.insert(END,sd[1])
            self.e2.delete(0, END)
            self.e2.insert(END, sd[2])
            self.e3.delete(0, END)
            self.e3.insert(END, sd[3])
            self.e4.delete(0, END)
            self.e4.insert(END, sd[4])
            self.e5.delete(0, END)
            self.e5.insert(END, sd[5])
            self.e6.delete(0, END)
            self.e6.insert(END, sd[6])
            self.e7.delete(0, END)
            self.e7.insert(END, sd[7])
            self.e8.delete(0, END)
            self.e8.insert(END, sd[8])
        def deleteData():
            if (len(StdID.get()) != 0):
                Final_Data.deleteRec(sd[0])

                clearData()
                displayData()

        def search():
            student_list.delete(0,END)
            for row in Final_Data.searchData(StdID.get(), Firstname.get(), Lastname.get(), Address.get(), Age.get(), City.get(), \
                                             Contact.get(), Email.get()):
                student_list.insert(END,row,str(""))

        def update():
            if (len(StdID.get()) != 0):
                Final_Data.deleteRec(sd[0])
            if (len(StdID.get()) != 0):
                Final_Data.addStdRec(StdID.get(), Firstname.get(), Lastname.get(), Address.get(), Age.get(), City.get(), \
                                     Contact.get(), Email.get())
                student_list.delete(0, END)
                student_list.insert(END,(StdID.get(), Firstname.get(), Lastname.get(), Address.get(), Age.get(), City.get(),\
                        Contact.get(), Email.get()))

        #=========================== creating the frames ================================


        First_frame = Frame(self.root, bg="cadet blue",width=1200,height=1200)
        First_frame.grid()

        Information_frame = Frame(First_frame,padx=54,pady=8,bg="ghost white",bd=2,relief=RIDGE)
        Information_frame.pack(side=TOP)

        a1 = Label(Information_frame,font=("times", "57", "bold"),text="Simple Student Management System  ",bg="ghost white")
        a1.grid()

        Button_frame = Frame(First_frame, bd=2, width=13550, height=70, padx=18, pady=10, bg="ghost white", relief=RIDGE)
        Button_frame.pack(side=BOTTOM)

        Details_frame = Frame(First_frame, bd=1, width=2400, height=900, padx=20, pady=20, relief=RIDGE, bg="ghost white")
        Details_frame.pack(side=BOTTOM)

        Dataframeleft =LabelFrame(Details_frame,bd=1, width=1800, height=1000, padx=20, relief=RIDGE, bg="ghost white",font=('ariel',35,"bold"),text="Student Information\n")
        Dataframeleft.pack(side=LEFT)

        Dataframeright = LabelFrame(Details_frame, bd=1, width=1200, height=1000, padx=31, pady=3, relief=RIDGE, bg="ghost white",font=('ariel',35,"bold"),text="Student Details\n")
        Dataframeright.pack(side=RIGHT)

#==================================== creating labels and entries ==============================================
        self.student_id = Label(Dataframeleft, text="Student ID", font=("times", "20", "bold"), padx=2, pady=3, bg="ghost white")
        self.student_id.grid(row=0, column=0, sticky="w")
        self.e1 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=StdID, width=39)
        self.e1.grid(row=0, column=1, sticky="w")

        self.First_name = Label(Dataframeleft, text="Name", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.First_name.grid(row=1, column=0, sticky="w")
        self.e2 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=Firstname, width=39)
        self.e2.grid(row=1, column=1, sticky="w")

        self.last_name = Label(Dataframeleft, text="Last Name", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.last_name.grid(row=2, column=0, sticky="w")
        self.e3 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=Lastname, width=39)
        self.e3.grid(row=2, column=1, sticky="w")

        self.Address_label = Label(Dataframeleft, text="Address", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.Address_label.grid(row=3, column=0, sticky="w")
        self.e4 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=Address, width=39)
        self.e4.grid(row=3, column=1, sticky="w")

        self.Age_label = Label(Dataframeleft, text="Age", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.Age_label.grid(row=4, column=0, sticky="w")
        self.e5 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=Age, width=39)
        self.e5.grid(row=4, column=1, sticky="w")

        self.city_label = Label(Dataframeleft, text="City", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.city_label.grid(row=5, column=0, sticky="w")
        self.e6 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=City, width=39)
        self.e6.grid(row=5, column=1, sticky="w")

        self.contact_label = Label(Dataframeleft, text="Contact", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.contact_label.grid(row=6, column=0, sticky="w")
        self.e7 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=Contact, width=39)
        self.e7.grid(row=6, column=1, sticky="w")

        self.Email_label = Label(Dataframeleft, text="Email", font=("times", "20", "bold"), padx=2, pady=3,
                                bg="ghost white")
        self.Email_label.grid(row=7, column=0, sticky="w")
        self.e8 = Entry(Dataframeleft, font=("times", "20", "bold"), textvariable=Email, width=39)
        self.e8.grid(row=7, column=1, sticky="w")

#====================================creating scrollbar ===========================
        scrollbar = Scrollbar(Dataframeright)
        scrollbar.grid(row=0,column=1, sticky='ns')

        student_list= Listbox(Dataframeright, width=41, height=16, font=("times", "12", "bold"), yscrollcommand=scrollbar.set)
        student_list.bind('<<ListboxSelect>>',StudentRec)
        student_list.grid(row=0, column=0, padx=8)
        scrollbar.config(command= student_list.yview)


#====================================== creating the buttons ========================
        self.Add_button = Button(Button_frame, text="Add Data", font=("times", "20", "bold"),height=1,width=10,bd=4, command=addData)
        self.Add_button.grid(row=0,column=0)

        self.display_button = Button(Button_frame, text="display", font=("times", "20", "bold"), height=1, width=10, bd=4, command=displayData)
        self.display_button.grid(row=0, column=1)

        self.clear_button = Button(Button_frame, text="clear", font=("times", "20", "bold"), height=1, width=10, bd=4, command=clearData)
        self.clear_button.grid(row=0, column=2)

        self.delete_button = Button(Button_frame, text="Delete", font=("times", "20", "bold"), height=1, width=10, bd=4,command=deleteData)
        self.delete_button.grid(row=0, column=3)

        self.update_button = Button(Button_frame, text="Update", font=("times", "20", "bold"), height=1, width=10, bd=4, command=update)
        self.update_button.grid(row=0, column=4)

        self.exit_button = Button(Button_frame, text="Exit", font=("times", "20", "bold"), height=1, width=10, bd=4, command=iExit)
        self.exit_button.grid(row=0, column=5)

        self.search_button = Button(Button_frame, text="search", font=("times", "20", "bold"), height=1, width=10, bd=4, command=search)
        self.search_button.grid(row=0, column=6)





