from email.message import EmailMessage
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import pymysql
import smtplib


# ---------------------------------------------------------------Login Function --------------------------------------


def login():
    def resetInput():
        userEntry.delete(0, END)
        passEntry.delete(0, END)

    def close():
        win.destroy()

    # signup button
    def toOptionSignUp():
        optionSignup()

    def switchTo():
        win.destroy()

    def checkOk():
        if user_name.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Enter User Name And Password", parent=win)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                cur = con.cursor()

                cur.execute("select * from user_information where username=%s and password = %s",
                            (user_name.get(), password.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid User Name And Password", parent=win)

                else:
                    messagebox.showinfo("Success", "Successfully Login", parent=win)
                    user_name.get()
                    close()
                    deshboard()
                    return
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=win)

    win = Tk()

    # app title
    win.title("VADA Quizz App")

    # window size
    win.maxsize(width=500, height=500)
    win.minsize(width=500, height=500)

    bkg_img = PhotoImage(file="sqr.png")

    labelimg = Label(win, image=bkg_img)
    labelimg.place(x=0, y=0)

    # heading label
    heading = Label(win, text="Login", bg="black", fg="cyan", font='Helvetica 25 bold', pady=5, padx=20)
    heading.place(x=80, y=100)

    username = Label(win, text="UserName :", width=11, bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    username.place(x=80, y=220)

    userpass = Label(win, text="Password :", width=11, bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    userpass.place(x=80, y=260)

    # Entry Box
    password = StringVar()
    global user_name
    user_name = StringVar()

    userEntry = Entry(win, width=30, bg='#daff96', font='segoe_ui 10 bold', textvariable=user_name)
    userEntry.place(x=200, y=223)

    passEntry = Entry(win, width=30, bg='#daff96', font='segoe_ui 10 bold', show="*", textvariable=password)
    passEntry.place(x=200, y=260)

    # button login and clear

    btn_login = Button(win, text="Login", width=12, border=3, height=1, bg="black", fg="cyan", font='Helvetica 12 bold',
                       command=checkOk)
    btn_login.place(x=85, y=343)

    btn_clear = Button(win, text="Clear", width=12, border=3, height=1, bg="black", fg="cyan", font='Helvetica 12 bold',
                       command=resetInput)
    btn_clear.place(x=250, y=343)

    sign_up_btn = Button(win, text="Switch To Sign up", border=3, bg="black", fg="magenta",
                         command=lambda: [switchTo(), toOptionSignUp()])
    sign_up_btn.place(x=365, y=24)

    win.mainloop()


# ---------------------------------------------------------------End Login Function ---------------------------------

# ---------------------------------------------------- DeshBoard Panel -----------------------------------------

def deshboard():
    def StartQuiz():

        def examPanel(user_ID, total_questions, currentQuestionNum):
            def answerExecute():
                try:
                    serve = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                    exe = serve.cursor()
                    exe.execute(
                        "INSERT INTO submission_table (user_id,quiz_id,question_id,option_selected) VALUES (" + str(
                            row[0][0]) + "," + str(questionAllData[currentQuestionNum][1]) + "," + str(
                            questionAllData[currentQuestionNum][0]) + ",%s);", user_selected.get())
                    serve.commit()
                    serve.close()
                except Exception as ES:
                    messagebox.showerror("Error", f"Error Dui to : {str(ES)}", parent=ansData)

            def switch():
                ansData.destroy()

            ansData = Tk()
            ansData.title("VADA Quiz App")
            ansData.maxsize(width=725, height=500)
            ansData.minsize(width=725, height=500)

            Label(ansData, height=500, width=725, bg="#000000").place(x=0, y=0)
            Label(ansData, height=26, width=95, bg="#fffea6").place(x=24, y=24)

            questionTxt = Label(ansData, text=f"Question    :   {questionAllData[currentQuestionNum][7]}", fg="#FFAC30", bg="black",
                                font='Helvetica 13 bold')
            questionTxt.place(x=100, y=120)

            user_selected = StringVar()
            user_selected.set('not_selected')

            opt1 = Radiobutton(ansData, variable=user_selected, highlightbackground="Black", highlightcolor="black",
                               activebackground="Black", activeforeground="magenta",
                               text=f"Option_A  :   {questionAllData[currentQuestionNum][2]}", font='Helvetica 15 bold',
                               value="Option A",
                               fg="#ff8800", bg="#fffea6",
                               command=lambda: [user_selected.set("Option A")])
            opt1.place(x=80, y=200)

            opt2 = Radiobutton(ansData, variable=user_selected, highlightbackground="Black", highlightcolor="black",
                               activebackground="Black", activeforeground="magenta",
                               text=f"Option_B  :   {questionAllData[currentQuestionNum][3]}", font='Helvetica 15 bold',
                               value="Option B",
                               fg="#ff8800", bg="#fffea6",
                               command=lambda: [user_selected.set("Option B")])
            opt2.place(x=80, y=240)

            opt3 = Radiobutton(ansData, variable=user_selected, highlightbackground="Black", highlightcolor="black",
                               activebackground="Black", activeforeground="magenta",
                               text=f"Option_C  :   {questionAllData[currentQuestionNum][4]}", font='Helvetica 15 bold',
                               value="Option C",
                               fg="#ff8800", bg="#fffea6",
                               command=lambda: [user_selected.set("Option C")])
            opt3.place(x=80, y=280)

            opt4 = Radiobutton(ansData, variable=user_selected, highlightbackground="Black", highlightcolor="black",
                               activebackground="Black", activeforeground="magenta",
                               text=f"Option_D  :   {questionAllData[currentQuestionNum][5]}", font='Helvetica 15 bold',
                               value="Option D",
                               fg="#ff8800", bg="#fffea6",
                               command=lambda: [user_selected.set("Option D")])
            opt4.place(x=80, y=320)

            opt5 = Radiobutton(ansData, variable=user_selected, highlightbackground="Black", highlightcolor="black",
                               activebackground="Black", activeforeground="magenta",
                               text=f"Option_E  :   {questionAllData[currentQuestionNum][6]}", font='Helvetica 15 bold',
                               value="Option E",
                               fg="#ff8800", bg="#fffea6",
                               command=lambda: [user_selected.set("Option E")])
            opt5.place(x=80, y=360)

            # currentQuestionNum = currentQuestionNum + 1

            questionNumTitle = Label(ansData, text=f" Question No. {currentQuestionNum + 1} ", font='Helvetica 25 bold',
                                     bg="black", fg="cyan", pady=5, padx=20)
            questionNumTitle.place(x=235, y=45)

            if (total_questions - 1) == currentQuestionNum:
                doneBtn = Button(ansData, text="Done", font='Helvetica 10 bold',  width=15, border=3, fg="#FFAC30", bg="black",
                                 command=lambda: [answerExecute(), switch()])
                doneBtn.place(x=470, y=420)
            else:
                nextBtn = Button(ansData, text="Next", font='Helvetica 13 bold', width=15, border=3, fg="#FFAC30", bg="black",
                                 command=lambda: [answerExecute(), switch(),
                                                  examPanel(user_ID, total_questions, currentQuestionNum + 1)])
                nextBtn.place(x=470, y=420)

        serverCon = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
        action = serverCon.cursor()

        action.execute("SELECT quiz_id FROM quiz_table WHERE quiz_name = '" + quiz_code.get() + "';")
        quizUniqueCode = action.fetchall()

        print(quizUniqueCode)
        emptyTuple = ()

        if quizUniqueCode == emptyTuple:
            messagebox.showerror("Error", "Incorrect Quiz Code", parent=des)
        else:
            action.execute("SELECT * FROM question_table WHERE quiz_id = '" + str(quizUniqueCode[0][0]) + "';")
            questionAllData = action.fetchall()
            action.execute("select id from user_information where username ='" + user_name.get() + "'")
            userID = cur.fetchall()
            examPanel(userID, len(questionAllData), 0)

    def ResultCheck():
        def EmailResults():
            print('Email is Sending')

            result_server = smtplib.SMTP('smtp.gmail.com', 587)
            result_server.starttls()
            result_server.login('vadaquiz@gmail.com', 'abcdefghijklmnopqrstuvwxyz')

            action.execute("SELECT quiz_id FROM quiz_table WHERE quiz_name = '" + QuizByAdminBox.get() + "';")
            quiz_primary_id = action.fetchall()

            action.execute("SELECT user_id FROM submission_table WHERE quiz_id = " + str(quiz_primary_id[0][0]) + ";")
            data_of_users = action.fetchall()

            userID_set = set()

            for each in data_of_users:
                userID_set.add(each[0])

                '''
                result_server.sendmail('vadaquiz@gmail.com', user_email[0][0], "Hello Your Result is Declared ")
                print("sent successfully to "+user_email[0][0])
                '''
            for each_user in userID_set:
                marks = 0
                action.execute("SELECT question_id, option_selected FROM submission_table WHERE user_id = " + str(
                    each_user) + " AND quiz_id = " + str(quiz_primary_id[0][0]) + ";")
                data_of_submission = action.fetchall()
                for each_submission in data_of_submission:
                    action.execute(
                        "SELECT answer FROM question_table WHERE question_id = " + str(each_submission[0]) + ";")
                    correctAns = action.fetchall()
                    if correctAns[0][0] == each_submission[1]:
                        marks = marks + 1
                action.execute(
                    "SELECT first_name, last_name, username, email_id FROM user_information WHERE id = " + str(
                        each_user) + ";")
                email_credentials = action.fetchall()

                email = EmailMessage()
                email['From'] = 'vadaquiz@gmail.com'
                email['To'] = email_credentials[0][3]
                email['Subject'] = 'Result is Out, Check Out Your Score'
                message = f'''
                Hello {email_credentials[0][0]} {email_credentials[0][1]},

                Your Result is Been Declared.
                You Tried Really Hard,
                Your Score is {marks}.
                '''
                email.set_content(message)
                result_server.send_message(email)
                '''
                result_server.sendmail()'''

                print("marks with Quiz id " + str(each_user) + " and user_name " + str(
                    email_credentials[0][2]) + " having emailID as " +
                      str(email_credentials[0][3]) + " is " + str(marks))

                print(each_user)

            action.execute(
                "UPDATE quiz_table SET result_declare = 'yes' WHERE quiz_name = '" + QuizByAdminBox.get() + "';")
            serve.commit()
            serve.close()
            messagebox.showinfo("Success", "Result Declared", parent=des)

        print("Dekh Le Bhai " + QuizByAdminBox.get())
        if QuizByAdminBox.get() == "":
            messagebox.showerror("Error", "You Don't Have Any Quiz", parent=des)

        else:
            try:
                serve = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                action = serve.cursor()
                action.execute(
                    "SELECT result_declare FROM quiz_table WHERE quiz_name = '" + QuizByAdminBox.get() + "';")
                quizToCheckResult = action.fetchall()

                ResultDeclareBtn = Button(des, text="Declare Result", font='Helvetica 10 bold', width=25, height=2,
                                          border=3, bg='black', fg='cyan',
                                          command=lambda: [EmailResults(), ResultDeclareBtn.destroy()])

                if quizToCheckResult[0][0] == "no":
                    ResultDeclareBtn.place(x=50, y=400)
                else:
                    ResultDeclareBtn.destroy()
                    DeclareText = Label(des, text="Result Already Declared", width=25, fg='cyan', bg='black',
                                        font='Helvetica 10 bold')
                    DeclareText.place(x=50, y=410)

            except Exception as ES:
                messagebox.showerror("Error", f"Error Dui to : {str(ES)}", parent=des)

    def setQuestion():

        def inputQuestion(quizID, question_num, currentQuestionNum):
            def emptyBoxes():
                question_text.delete(0, END)
                optionA_text.delete(0, END)
                optionB_text.delete(0, END)
                optionC_text.delete(0, END)
                optionD_text.delete(0, END)
                optionE_text.delete(0, END)

            def questionExecute():
                if question_text.get() == "" or optionA_text.get() == "" or optionB_text.get() == "" or optionC_text.get() == "" or optionD_text.get() == "" or optionE_text.get() == "" or answer_textBox.get() == "":
                    messagebox.showerror("Error", "All Fields Are Required", parent=qData)
                else:
                    try:

                        serve = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                        action = serve.cursor()
                        action.execute(
                            "INSERT INTO question_table (quiz_id,option1,option2,option3,option4,option5,question,answer) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);",
                            (
                                quizID,
                                optionA_text.get(),
                                optionB_text.get(),
                                optionC_text.get(),
                                optionD_text.get(),
                                optionE_text.get(),
                                question_text.get(),
                                answer_textBox.get()
                            )
                        )
                        serve.commit()
                        serve.close()
                        emptyBoxes()
                        if question_num != currentQuestionNum:
                            qData.destroy()
                            inputQuestion(quizID, question_num, currentQuestionNum)
                    except Exception as ES:
                        messagebox.showerror("Error", f"Error Dui to : {str(ES)}", parent=qData)

            def switch():
                print("qdata destroyed")
                qData.destroy()

            qData = Tk()
            qData.title("VADA Quiz App")
            qData.maxsize(width=725, height=500)
            qData.minsize(width=725, height=500)

            Label(qData, height=500, width=725, bg="magenta").place(x=0, y=0)
            Label(qData, height=26, width=95, bg="Black").place(x=24, y=24)

            currentQuestionNum = currentQuestionNum + 1
            questionNumTitle = Label(qData, text=f"Question No. {currentQuestionNum}", bg="black", fg="cyan",
                                     font='Helvetica 25 bold', pady=5, padx=20)
            questionNumTitle.place(x=235, y=45)

            questionTxt = Label(qData, text=f"Question : ", width=11, bg="black", fg="#FFAC30",
                                font='Helvetica 13 bold')
            questionTxt.place(x=85, y=100)

            optionA = Label(qData, text=f"Option A : ", width=11, bg="black", fg="#FFAC30", font='Helvetica 12 bold')
            optionA.place(x=85, y=200)

            optionB = Label(qData, text=f"Option B : ", width=11, bg="black", fg="#FFAC30", font='Helvetica 12 bold')
            optionB.place(x=85, y=230)

            optionC = Label(qData, text=f"Option C : ", width=11, bg="black", fg="#FFAC30", font='Helvetica 12 bold')
            optionC.place(x=85, y=260)

            optionD = Label(qData, text=f"Option D : ", width=11, bg="black", fg="#FFAC30", font='Helvetica 12 bold')
            optionD.place(x=85, y=290)

            optionE = Label(qData, text=f"Option E : ", width=11, bg="black", fg="#FFAC30", font='Helvetica 12 bold')
            optionE.place(x=85, y=320)

            answerTxt = Label(qData, text=f"Answer   : ", width=11, bg="black", fg="#FFAC30", font='Helvetica 13 bold')
            answerTxt.place(x=85, y=370)

            # Entry Box ------------------------------------------------------------------

            question_text = StringVar()
            optionA_text = StringVar()
            optionB_text = StringVar()
            optionC_text = StringVar()
            optionD_text = StringVar()
            optionE_text = StringVar()
            answer_text = tk.StringVar()

            question_text = Entry(qData, width=40, bg='#daff96', font='segoe_ui 12 bold', textvariable=question_text)
            question_text.place(x=200, y=100)

            optionA_text = Entry(qData, width=40, bg='#daff96', font='segoe_ui 12 bold', textvariable=optionA_text)
            optionA_text.place(x=200, y=200)

            optionB_text = Entry(qData, width=40, bg='#daff96', font='segoe_ui 12 bold', textvariable=optionB_text)
            optionB_text.place(x=200, y=230)

            optionC_text = Entry(qData, width=40, bg='#daff96', font='segoe_ui 12 bold', textvariable=optionC_text)
            optionC_text.place(x=200, y=260)

            optionD_text = Entry(qData, width=40, bg='#daff96', font='segoe_ui 12 bold', textvariable=optionD_text)
            optionD_text.place(x=200, y=290)

            optionE_text = Entry(qData, width=40, bg='#daff96', font='segoe_ui 12 bold', textvariable=optionE_text)
            optionE_text.place(x=200, y=320)

            answer_textBox = ttk.Combobox(qData, width=20, font='segoe_ui 12 bold', textvariable=answer_text,
                                          state='readonly')
            answer_textBox['values'] = ('Option A', 'Option B', 'Option C', 'Option D', 'Option E')
            answer_textBox.current(0)
            answer_textBox.place(x=200, y=370)

            if question_num == currentQuestionNum:
                doneBtn = Button(qData, text="Done", font='Helvetica 13 bold', width=15, border=3, fg="#FFAC30",
                                 bg="black",
                                 command=lambda: [questionExecute(), switch()])
                doneBtn.place(x=470, y=420)
            else:
                nextBtn = Button(qData, text="Next", font='Helvetica 13 bold', width=15, border=3, fg="#FFAC30",
                                 bg="black",
                                 command=lambda: [questionExecute(), switch()])
                nextBtn.place(x=470, y=420)

            clearBtn = Button(qData, text="Clear", font='Times 13 bold', width=15, border=3, fg="#FFAC30", bg="black",
                              command=emptyBoxes)
            clearBtn.place(x=300, y=420)

            qData.mainloop()

        # action when set button is clicked------------------------------------------------------------------
        if numQuestion.get() == "" or quizName.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=des)

        else:
            try:
                connect = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                cur1 = connect.cursor()
                cur1.execute("select * from quiz_table where quiz_name=%s", quizName.get())
                row1 = cur1.fetchone()

                if row1 is not None:
                    messagebox.showerror("Error", "Quiz Name Already Exists", parent=des)
                else:
                    cur1.execute("select id from user_information where username =  %s", user_name.get())
                    row1 = cur1.fetchone()
                    user_id = row1[0]
                    cur1.execute(
                        "INSERT INTO quiz_table(user_id, quiz_name,total_questions) VALUES (%s,%s,%s);",
                        (
                            user_id, quizName.get(), int(numQuestion.get())
                        ))
                    cur1.execute("select quiz_id,total_questions from quiz_table where quiz_name =  %s", quizName.get())
                    row1 = cur1.fetchone()
                    connect.commit()
                    connect.close()
                    inputQuestion(row1[0], row1[1], 0)
                    print(row1)

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=des)



    con = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
    cur = con.cursor()

    cur.execute("select * from user_information where username ='" + user_name.get() + "'")
    row = cur.fetchall()

    cur.execute("select isAdmin from user_information where username ='" + user_name.get() + "'")
    adminCheck = cur.fetchall()

    des = Tk()
    des.title("VADA Quiz App")

    des.maxsize(width=800, height=500)
    des.minsize(width=800, height=500)

    b_image = PhotoImage(file="threetwo.png")

    # Add image file
    label_img = Label(des, image=b_image)
    label_img.place(x=0, y=0)

    print('i am in')

    headingTitle = Label(des, text=f" UserName : {user_name.get()} ", font='Helvetica 20 bold', fg='#ff661f',
                         bg='maroon', padx=20, pady=5)
    headingTitle.place(x=230, y=18)

    f = Frame(des, height=3, width=800, bg="#20f595")
    f.place(x=0, y=80)

    a = Frame(des, height=3, width=320, bg="#20f595")
    a.place(x=0, y=195)

    b = Frame(des, height=500, width=3, bg="#20f595")
    b.place(x=320, y=83)

    # des.wm_attributes('-transparentcolor', '#ab23ff')

    for data in row:
        first_name = Label(des, text=f"First Name : {data[1]}", bg='#000000', fg='#ff0ad6', font='Helvetica 10 bold')
        first_name.place(x=20, y=100)

        last_name = Label(des, text=f"Last Name : {data[2]}", bg='#000000', fg='#ff0ad6', font='Helvetica 10 bold')
        last_name.place(x=20, y=130)

        isAdmin = Label(des, text=f"isAdmin : {data[3]}", bg='#000000', fg='#ff0ad6', font='Helvetica 10 bold')
        isAdmin.place(x=20, y=160)

        idUser = Label(des, text=f"ID : {data[0]}", bg='#000000', fg='#ff0ad6', font='Helvetica 10 bold')
        idUser.place(x=200, y=100)

        city = Label(des, text=f"Roll_No : {data[5]}", bg='#000000', fg='#ff0ad6', font='Helvetica 10 bold')
        city.place(x=200, y=130)

        add = Label(des, text=f"Topic : {data[6]}", bg='#000000', fg='#ff0ad6', font='Helvetica 10 bold')
        add.place(x=200, y=160)

    # quiz App
    if adminCheck[0][0] == 'yes':
        headingTitle = Label(des, text="Set Questions/Quiz", bg='#000000', fg='#b457eb', font='Helvetica 20 bold')
        headingTitle.place(x=425, y=130)

        # BLabel

        NumQuestion = Label(des, text="Number of Questions  :", bg='#000000', fg='#b457eb', font='Helvetica 10 bold')
        NumQuestion.place(x=350, y=207)

        QuizName = Label(des, text="Unique Quiz Name      :", bg='#000000', fg='#b457eb', font='Helvetica 10 bold')
        QuizName.place(x=350, y=247)

        # Entry Box
        # level = tk.StringVar()
        # month = tk.StringVar()
        numQuestion = StringVar()
        quizName = StringVar()

        NumQuestion = Entry(des, width=30, bg='#daff96', font='segoe_ui 10 bold', textvariable=numQuestion)
        NumQuestion.place(x=550, y=208)

        QuizName = Entry(des, width=30, bg='#daff96', font='segoe_ui 10 bold', textvariable=quizName)
        QuizName.place(x=550, y=248)

        # button
        Setbtn = Button(des, text="Set", font='Helvetica 13 bold', border=3, bg="black", fg="cyan", width=20, height=2,
                        command=setQuestion)
        Setbtn.place(x=445, y=320)

        # for left bottom

        cur.execute("SELECT id FROM user_information WHERE username ='" + user_name.get() + "'")
        AdminId = cur.fetchall()

        cur.execute("SELECT quiz_name FROM quiz_table WHERE user_id ='" + str(AdminId[0][0]) + "'")
        adminQuiz = cur.fetchall()

        headingTitle = Label(des, text=f"{user_name.get()}'s Quiz", bg='#000000', fg='Cyan', font='Helvetica 15 bold')
        headingTitle.place(x=50, y=220)

        quizByAdmin = Label(des, text=" Select Quiz  :", bg='#000000', fg='cyan', font='Helvetica 10 bold')
        quizByAdmin.place(x=20, y=290)

        QuizByAdmin = tk.StringVar()

        QuizByAdminBox = ttk.Combobox(des, width=20, textvariable=QuizByAdmin, font='Helvetica 10 bold',
                                      background='cyan', state='readonly')
        QuizByAdminBox['values'] = adminQuiz
        QuizByAdminBox.place(x=130, y=290)

        CheckBtn = Button(des, text="Result Declaration Status", font='Helvetica 10 bold', bg="black", fg="cyan",
                          border=3, width=25,
                          command=ResultCheck)
        CheckBtn.place(x=50, y=345)

    else:
        quiz_code = StringVar()

        headingTitle = Label(des, text="Attend Questions/Quiz", bg='#000000', fg='#b457eb', font='Helvetica 20 bold',
                             pady=3, padx=20)
        headingTitle.place(x=400, y=140)

        QuizCode = Label(des, text=" Enter Quiz Code :", bg='#000000', fg='#b457eb', font='Helvetica 12 bold')
        QuizCode.place(x=350, y=247)

        QuizCode = Entry(des, width=25, bg='#daff96', fg="RED", font='segoe_ui 12 bold', textvariable=quiz_code)
        QuizCode.place(x=510, y=248)

        Setbtn = Button(des, text="Start", font='Helvetica 13 bold', border=3, bg="black", fg="cyan", width=20,
                        height=2, command=StartQuiz)
        Setbtn.place(x=440, y=320)

    des.mainloop()


# -----------------------------------------------------End Right Deshboard Panel -------------------------------------

# -----------------------------------------------------Start Left Bottom Deshboard Panel -------------------------------------

# Details'''

# -----------------------------------------------------End Left Bottom Deshboard Panel -------------------------------------



# -----------------------------------------------------End Deshboard Panel -------------------------------------


# -----------------------------------------------------OptionSignup Panel -------------------------------------
def optionSignup():
    def toUser():
        signUpUser()

    def toAdmin():
        signUpAdmin()

    def switch():
        optionSignUp.destroy()

    # start Signup Window
    optionSignUp = Tk()
    optionSignUp.title("VADA Quiz App")
    optionSignUp.maxsize(width=500, height=500)
    optionSignUp.minsize(width=500, height=500)

    bkg_img = PhotoImage(file="sqr.png")

    labelimg = Label(optionSignUp, image=bkg_img)
    labelimg.place(x=0, y=0)

    # heading label
    headingTitle = Label(optionSignUp, text="Register as Admin or User", fg="#FFAC30", bg="black",
                         font='Helvetica 20 bold', pady=6, padx=25)
    headingTitle.place(x=60, y=125)
    print("in option")

    userButton = Button(optionSignUp, text="User", font='Helvetica 11 bold', border=3, width=25, height=2, bg="black",
                        fg="cyan", command=lambda: [switch(), toUser()])
    userButton.place(x=150, y=250)

    adminButton = Button(optionSignUp, text="Admin", font='Helvetica 11 bold', border=3, width=25, height=2, bg="black",
                         fg="cyan", command=lambda: [switch(), toAdmin()])
    adminButton.place(x=150, y=320)

    signUpButton = Button(optionSignUp, text="Switch To Login", bg="black", fg="magenta", border=3,
                          command=lambda: [switch(), login()])
    signUpButton.place(x=370, y=24)
    optionSignUp.mainloop()


# -----------------------------------------------------End OptionSignup Panel -------------------------------------


# -----------------------------------------------------User Signup Panel -------------------------------------
def signUpUser():
    def action():
        isAdmin = 'no'
        if first_name.get() == "" or last_name.get() == "" or emailId.get() == "" or topic.get() == "" or userName.get() == "" or passWord.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif passWord.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                cur1 = con.cursor()
                cur2 = con.cursor()
                cur1.execute("select * from user_information where username=%s", userName.get())
                cur2.execute("select * from user_information where email_id=%s", emailId.get())
                row1 = cur1.fetchone()
                row2 = cur2.fetchone()
                if row1 is not None:
                    messagebox.showerror("Error", "UserName Already Exists", parent=winsignup)
                elif row2 is not None:
                    messagebox.showerror("Error", "Email Id Already Exists", parent=winsignup)
                else:
                    cur1.execute(
                        "insert into user_information(first_name,last_name,isAdmin,email_id,roll_no,topic,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            isAdmin,
                            emailId.get(),
                            rollNo.get(),
                            topic.get(),
                            userName.get(),
                            passWord.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=winsignup)
                    emptyBoxes()
                    switch()
                    login()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def emptyBoxes():
        first_name.delete(0, END)
        last_name.delete(0, END)
        emailId.delete(0, END)
        rollNo.delete(0, END)
        topic.delete(0, END)
        userName.delete(0, END)
        passWord.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window
    winsignup = Tk()
    winsignup.title("VADA Quiz App")
    winsignup.maxsize(width=500, height=500)
    winsignup.minsize(width=500, height=500)

    bkg_img = PhotoImage(file="sqr.png")

    labelimg = Label(winsignup, image=bkg_img)
    labelimg.place(x=0, y=0)

    # heading label
    headingTitle = Label(winsignup, text="Register...", bg="black", fg="cyan", font='Helvetica 25 bold', pady=5,
                         padx=20)
    headingTitle.place(x=60, y=40)

    # form data label
    first_name = Label(winsignup, text="First Name :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    first_name.place(x=70, y=113)

    last_name = Label(winsignup, text="Last Name :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    last_name.place(x=70, y=143)

    emailId = Label(winsignup, text="Email Id :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    emailId.place(x=70, y=173)

    rollNo = Label(winsignup, text="Roll No. :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    rollNo.place(x=70, y=203)

    topic = Label(winsignup, text="Topic :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    topic.place(x=70, y=233)

    userName = Label(winsignup, text="User Name :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    userName.place(x=70, y=303)

    passWord = Label(winsignup, text="Password :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    passWord.place(x=70, y=333)

    very_pass = Label(winsignup, text="Verify Password:", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    very_pass.place(x=70, y=363)

    # Entry Box ------------------------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    emailId = StringVar()
    rollNo = StringVar()
    topic = StringVar()
    userName = StringVar()
    passWord = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=first_name)
    first_name.place(x=200, y=113)

    last_name = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=last_name)
    last_name.place(x=200, y=143)

    emailId = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=emailId)
    emailId.place(x=200, y=173)

    rollNo = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=rollNo)
    rollNo.place(x=200, y=203)

    topic = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=topic)
    topic.place(x=200, y=233)

    userName = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=userName)
    userName.place(x=200, y=303)

    passWord = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=passWord)
    passWord.place(x=200, y=333)

    very_pass = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', show="*", textvariable=very_pass)
    very_pass.place(x=200, y=363)

    # button login and clear

    btn_signup = Button(winsignup, text="Register", width=15, border=3, height=1, bg="black", fg="cyan",
                        font='Helvetica 12 bold', command=action)
    btn_signup.place(x=85, y=413)

    logInButton = Button(winsignup, text="Clear", width=15, border=3, height=1, bg="black", fg="cyan",
                         font='Helvetica 12 bold', command=emptyBoxes)
    logInButton.place(x=260, y=413)

    signUpButton = Button(winsignup, text="Go Back", border=3, bg="black", fg="magenta",
                          command=lambda: [switch(), optionSignup()])
    signUpButton.place(x=430, y=15)

    winsignup.mainloop()


# -----------------------------------------------------End User Signup Panel -------------------------------------

# -----------------------------------------------------------Admin Signup Window --------------------------------------------------

def signUpAdmin():
    # signup database connect
    def action():
        isAdmin = 'yes'

        if first_name.get() == "" or last_name.get() == "" or emailId.get() == "" or topic.get() == "" or userName.get() == "" or passWord.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif passWord.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="QuizApp")
                cur1 = con.cursor()
                cur2 = con.cursor()
                cur1.execute("select * from user_information where username=%s", userName.get())
                cur2.execute("select * from user_information where email_id=%s", emailId.get())
                row1 = cur1.fetchone()
                row2 = cur2.fetchone()
                if row1 is not None:
                    messagebox.showerror("Error", "User Name Already Exists", parent=winsignup)
                elif row2 is not None:
                    messagebox.showerror("Error", "Email Id Already Exists", parent=winsignup)
                else:
                    cur1.execute(
                        "insert into user_information(first_name,last_name,isAdmin,email_id,roll_no,topic,username,password) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            first_name.get(),
                            last_name.get(),
                            isAdmin,
                            emailId.get(),
                            rollNo.get(),
                            topic.get(),
                            userName.get(),
                            passWord.get()
                        ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Ragistration Successfull", parent=winsignup)
                    emptyBoxes()
                    switch()
                    login()

            except Exception as es:
                messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=winsignup)

    # close signup function
    def switch():
        winsignup.destroy()

    # clear data function
    def emptyBoxes():
        first_name.delete(0, END)
        last_name.delete(0, END)
        emailId.delete(0, END)
        rollNo.delete(0, END)
        topic.delete(0, END)
        userName.delete(0, END)
        passWord.delete(0, END)
        very_pass.delete(0, END)

    # start Signup Window
    winsignup = Tk()
    winsignup.title("VADA Quiz App")
    winsignup.maxsize(width=500, height=500)
    winsignup.minsize(width=500, height=500)

    bkg_img = PhotoImage(file="sqr.png")

    labelimg = Label(winsignup, image=bkg_img)
    labelimg.place(x=0, y=0)

    # heading label
    headingTitle = Label(winsignup, text="Register...", bg="black", fg="cyan", font='Helvetica 25 bold', pady=5,
                         padx=20)
    headingTitle.place(x=60, y=40)

    # form data label
    first_name = Label(winsignup, text="First Name :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    first_name.place(x=70, y=113)

    last_name = Label(winsignup, text="Last Name :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    last_name.place(x=70, y=143)

    emailId = Label(winsignup, text="Email Id :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    emailId.place(x=70, y=173)

    rollNo = Label(winsignup, text="Roll No. :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    rollNo.place(x=70, y=203)

    topic = Label(winsignup, text="Topic :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    topic.place(x=70, y=233)

    userName = Label(winsignup, text="User Name :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    userName.place(x=70, y=303)

    passWord = Label(winsignup, text="Password :", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    passWord.place(x=70, y=333)

    very_pass = Label(winsignup, text="Verify Password:", bg="black", fg="#FFAC30", font='Helvetica 10 bold')
    very_pass.place(x=70, y=363)

    # Entry Box ------------------------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    emailId = StringVar()
    rollNo = StringVar()
    topic = StringVar()
    userName = StringVar()
    passWord = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=first_name)
    first_name.place(x=200, y=113)

    last_name = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=last_name)
    last_name.place(x=200, y=143)

    emailId = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=emailId)
    emailId.place(x=200, y=173)

    rollNo = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=rollNo)
    rollNo.place(x=200, y=203)

    topic = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=topic)
    topic.place(x=200, y=233)

    userName = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=userName)
    userName.place(x=200, y=303)

    passWord = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', textvariable=passWord)
    passWord.place(x=200, y=333)

    very_pass = Entry(winsignup, width=30, bg='#daff96', font='Segoe 10 bold', show="*", textvariable=very_pass)
    very_pass.place(x=200, y=363)

    # button login and clear

    btn_signup = Button(winsignup, text="Register", width=15, border=3, height=1, bg="black", fg="cyan",
                        font='Helvetica 12 bold', command=action)
    btn_signup.place(x=85, y=413)

    logInButton = Button(winsignup, text="Clear", width=15, border=3, height=1, bg="black", fg="cyan",
                         font='Helvetica 12 bold', command=emptyBoxes)
    logInButton.place(x=260, y=413)

    signUpButton = Button(winsignup, text="Go Back", border=3, bg="black", fg="magenta",
                          command=lambda: [switch(), optionSignup()])
    signUpButton.place(x=430, y=15)

    winsignup.mainloop()


# ---------------------------------------------------------------------------End Admin SignUp Window-----------------------------------


# ------------------------------------------------------------ Login Window -----------------------------------------
def start():
    def toLogin():
        login()

    def toOptionSignUp():
        optionSignup()

    def switch():
        win.destroy()

    win = Tk()
    # app title
    win.title("VADA Quiz App")

    # window size
    win.maxsize(width=800, height=500)
    win.minsize(width=800, height=500)

    # Add image file
    bg_image = PhotoImage(file="threetwo.png")

    label = Label(win, image=bg_image)
    label.place(x=0, y=0)

    # global user_name

    # heading label
    heading = Label(win, anchor="center", text="Lets Get Started..!!", bg="black", fg="cyan", width=18, height=1,
                    font='Helvetica 30 bold', pady=3)
    heading.place(x=185, y=130)

    btn_login = Button(win, text="Log in", border=3, font='Times 20 bold', width=12, height=1, fg="#FFAC30", bg="black",
                       command=lambda: [switch(), toLogin()])
    btn_login.place(x=190, y=293)

    btn_login = Button(win, text="Register", border=3, font='Times 20 bold', width=12, height=1, fg="#FFAC30",
                       bg="black",
                       command=lambda: [switch(), toOptionSignUp()])
    btn_login.place(x=410, y=293)

    win.mainloop()


# -------------------------------------------------------------------------- End Login Window ---------------------------------------------------
def endStart():
    wind.destroy()


wind = Tk()

# app title
wind.title("Welcome To VADA Quiz App")

# window size
wind.maxsize(width=500, height=500)
wind.minsize(width=500, height=500)

# Add image file
bg_img = PhotoImage(file="sqr.png")

# Show image using label
label1 = Label(wind, image=bg_img)
label1.place(x=0, y=0)

startLabel = Label(wind, text=" WELCOME..!! ", border=3, bg="black", fg="cyan", font='Times 30 bold')
startLabel.pack(ipady=50)
startLabel.place(x=110, y=150)

startButton = Button(wind, text="Click To Begin", border=3, font='Times 10 bold', width=20, height=3, fg="#FFAC30",
                     bg="black",
                     command=lambda: [endStart(), start()])
startButton.place(x=180, y=300)
wind.mainloop()
