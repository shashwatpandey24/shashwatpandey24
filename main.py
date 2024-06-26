from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
from tkinter import ttk
import smtplib

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("1366x768+0+0")


root.config(bg="#ffc400")
#bg = ImageTk.PhotoImage(file="library.jpg")

photo = PhotoImage(file="buttons.png")
resizeImg = photo.subsample(6,6)

frame = Frame(root,bg="white")
frame.place(relx=0,rely=0.05,relwidth=1,relheight=0.1)

frameBottom = Frame(root,bg="#ffc400")
frameBottom.place(rely=0.2, relwidth=1, relheight=0.8)
mainLabel = Label(frameBottom,text="Welcome to The Marwar Business\n School Library",bg="#ffc400",fg="#0077ff",font=("Helvetica",30,"bold"))
mainLabel.place(rely=0.3,relx=0.3)

def bookRegister():
    
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status =selected.get()
    def issue():
        issueto = int(inf1.get())
        print("Enter in issued to")
        if issueto !="":
            con = sqlite3.connect("main.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM students WHERE student_id=?",(issueto,))
            result = cur.fetchone()
            print(result)
            if result!=None:
                con.execute("CREATE TABLE IF NOT EXISTS issuebook (book_id varchar(20) primary key,issuedto integer(20))")
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS bookTable (book_id varchar(20) PRIMARY KEY,
                                                                book_title varchar(50),
                                                                author varchar(30),
                                                                status varchar(10))""")
                cur.execute("INSERT INTO bookTable (book_id,book_title,author,status) VALUES (?,?,?,?)",(bid,title,author,status))
                cur.execute("INSERT INTO issuebook (book_id,issuedto) VALUES(?,?)",(bid,issueto))
                messagebox.showinfo('Success',"Book added successfully")
                con.commit()
                con.close()
                root1.destroy()
            else:
                messagebox.showerror("Error","Student is not registerd")
        else:
            messagebox.showerror("Error","Empty field !")    
        

    if bid =="" or title =="" or author =="" or status =="":
        messagebox.showerror("Error","All fields are required !")
    else:
        try:
            if status == "issued":
                root1 = Tk()
                root1.title("Library")
                root1.minsize(width=400,height=400)
                root1.geometry("600x500")

                headingFrame1 = Frame(root1,bg="black",bd=5)
                headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
                    
                headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='#c48c12', font=('Courier',25,"bold"))
                headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
                
                labelFrame = Frame(root1,bg='black')
                labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
                    
                # Book ID
                lb1 = Label(labelFrame,text="Student ID : ", bg='black', fg='#c48c12',font=("Arial",15))
                lb1.place(relx=0.05,rely=0.2)
                    
                inf1 = Entry(labelFrame,font=("Arial",15))
                inf1.place(relx=0.3,rely=0.2, relwidth=0.62)

                issueBtn = Button(root1,text="Issue",bg='#d1ccc0', fg='black',command=issue)
                issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
                
                quitBtn = Button(root1,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
                quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
            else:
                con = sqlite3.connect("main.db")
                cur = con.cursor()
                cur.execute("""CREATE TABLE IF NOT EXISTS bookTable (book_id varchar(20) PRIMARY KEY,
                                                                    book_title varchar(50),
                                                                    author varchar(30),
                                                                    status varchar(10))""")
                cur.execute("insert into bookTable (book_id,book_title,author,status) values(?,?,?,?)",(bid,title,author,status))
                con.commit()
                cur.close()
                con.close()
                messagebox.showinfo('Success',"Book added successfully")
        except Exception as e:
            print(e)
            messagebox.showerror("Error","Can't add data into Database")
    bookInfo1.delete(0,END)
    bookInfo2.delete(0,END)
    bookInfo3.delete(0,END)
    r1.deselect()
    r2.deselect()


def addBook(): 
    
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root, selected, r1, r2
    selected = StringVar()
    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)
    
    headingFrame = Frame(frameBottom,bd=5,bg="black")
    headingFrame.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)

    headingLabel = Label(headingFrame, text="Add Books", fg='green', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(frameBottom,bg="navy")
    labelFrame.place(relx=0.1,rely=0.13,relwidth=0.8,relheight=0.6)
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='navy', fg='white',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.5,rely=0.2, relwidth=0.45,relheight=0.08)
        
    # Title
    lb2 = Label(labelFrame,text="Title : ", bg='navy', fg='white',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame,font=("Arial",15))
    bookInfo2.place(relx=0.5,rely=0.35, relwidth=0.45, relheight=0.08)
        
    # Book Author
    lb3 = Label(labelFrame,text="Author : ", bg='navy', fg='white',font=("Arial",15))
    lb3.place(relx=0.05,rely=0.50, relheight=0.08)
        
    bookInfo3 = Entry(labelFrame,font=("Arial",15))
    bookInfo3.place(relx=0.5,rely=0.50, relwidth=0.45, relheight=0.08)
        
    # Book Status
    lb4 = Label(labelFrame,text="Status : ", bg='navy', fg='white',font=("Arial",15))
    lb4.place(relx=0.05,rely=0.65, relheight=0.08)
    
    s = ttk.Style()
    s.configure('Wild.TRadiobutton',    # First argument is the name of style. Needs to end with: .TRadiobutton
        background="navy",         # Setting background to our specified color above
        foreground = "white")
    r1 = ttk.Radiobutton(labelFrame, text='Avaliable', value="avaliable", variable=selected, style = 'Wild.TRadiobutton')
    r1.place(relx =.5, rely=0.66 ,relwidth=.17)

    r2 = ttk.Radiobutton(labelFrame, text='Issued', value="issued", variable=selected, style = 'Wild.TRadiobutton')
    r2.place(relx =.71, rely=0.66 ,relwidth=.17)
        
    #Submit Button
    SubmitBtn = Button(labelFrame,text="SUBMIT",bg='#d1ccc0', fg='black',command=bookRegister)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # root.mainloop()
btn1 = Button(frame,text="Add Book Details",bg='black',image=resizeImg, fg='white', command=addBook,relief='ridge',bd=0,compound=CENTER)
btn1.place(relx=0.01,rely=0.18)

def deleteBook():
    
    bid = bookInfo1.get()
    

    try:
        con = sqlite3.connect("main.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM bookTable WHERE book_id=?",(bid,))
        result = cur.fetchone()
        if result[3] == "issued":
            cur.execute("DELETE FROM bookTable WHERE book_id=?",(bid,))
            cur.execute("DELETE FROM issuebook WHERE book_id=?",(bid,))
            con.commit()
            con.close()
        else:
            cur.execute("DELETE FROM bookTable WHERE book_id=?",(bid,))
            con.commit()
            # cur.execute(deleteIssue)
            con.close()
        messagebox.showinfo('Success',"Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)

    headingFrame1 = Frame(frameBottom,bg="#050245",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.1)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='#050245', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)
    
    labelFrame = Frame(frameBottom,bg="#050245")
    labelFrame.place(relx=0.1,rely=0.13,relwidth=0.8,relheight=0.6)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='#050245', fg='white',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.5)
    
    #Submit Button
    SubmitBtn = Button(labelFrame,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # root.mainloop()

btn2 = Button(frame,text="Delete Book",bg='black', fg='white',image=resizeImg, command=delete,relief='ridge',bd=0,compound=CENTER)
btn2.place(relx=0.12,rely=0.18)


def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("",END,values=i)

def View(): 
    con = sqlite3.connect("main.db")
    cur = con.cursor()
    global trv
    
    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)
        
    headingFrame1 = Frame(frameBottom,bg="#12a4d9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)
        
    headingLabel = Label(headingFrame1, text="View Books", bg='#12a4d9', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)
    
    labelFrame = Frame(frameBottom,bg='black')
    labelFrame.place(relx=0.1,rely=0.13,relwidth=0.8,relheight=0.6)
    
    scroll_v = Scrollbar(labelFrame)
    scroll_v.pack(side= RIGHT,fill="y")

    #Add a Horizontal Scrollbar
    scroll_h = Scrollbar(labelFrame, orient= HORIZONTAL)
    scroll_h.pack(side= BOTTOM, fill= "x")

    trv = ttk.Treeview(labelFrame,columns=(1,2,3,4),show="headings",height="0.4",yscrollcommand=scroll_v.set,xscrollcommand=scroll_h.set)
    trv.pack(fill=BOTH,expand=1)
    trv.heading(1,text="Book ID")
    trv.heading(2,text="Title")
    trv.heading(3,text="Author")
    trv.heading(4,text="Status")

    try:
        cur.execute("SELECT * FROM bookTable")
        rows = cur.fetchall()
        con.commit()
        update(rows)
        cur.close()
        con.close()
    except:
        messagebox.showinfo("Failed to fetch files from database")
    
    quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

    # root.mainloop()

btn3 = Button(frame,text="View Book List",bg='black', fg='white',image=resizeImg, command=View,relief='ridge',bd=0,compound=CENTER)
btn3.place(relx=0.23,rely=0.18)

def issue():
    bid = inf1.get()
    issueto = int(inf2.get())
    
    print(type(issueto))
    if bid=="" or issueto=="":
        messagebox.showinfo("Unsuccessful","Book id or issued to is missing")
    else:
        con = sqlite3.connect("main.db")
        con.execute("CREATE TABLE IF NOT EXISTS issuebook (book_id varchar(20) primary key,issuedto integer(20))")
        cur = con.cursor()
        cur.execute("SELECT * FROM bookTable WHERE book_id=?",(bid,))
        bid_detail = cur.fetchone()
        if bid_detail !=None:
            if bid_detail[3] == 'avaliable':
                cur.execute("SELECT * FROM students WHERE student_id=?",(issueto,))
                result = cur.fetchone()
                if result!=None:
                    cur.execute("UPDATE bookTable SET status ='issued' WHERE book_id=?",(bid,))
                    con.commit()
                    cur.execute("INSERT INTO issuebook (book_id,issuedto) VALUES(?,?)",(bid,issueto))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Successful","Book has been issued successfully")
                else:
                    messagebox.showinfo("Unregisterd","Not Registerd User")
                    print("Student is not registerd")
                
            else:
                messagebox.showinfo("Unsuccessful","Book already issued")
        else:
            print("Didn't get any data")
    inf1.delete(0,END)
    inf2.delete(0,END)

def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)

    headingFrame1 = Frame(frameBottom,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='#c48c12', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(frameBottom,bg='black')
    labelFrame.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='#c48c12',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame,font=("Arial",15))
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='#c48c12',font=("Arial",15))
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame,font=("Arial",15))
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)
    
    #Issue Button
    issueBtn = Button(labelFrame,text="Issue",bg='#d1ccc0', fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(labelFrame,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # root.mainloop()

btn4 = Button(frame,text="Issue Book to Student",bg='black', fg='white',image=resizeImg, command = issueBook,relief='ridge',bd=0,compound=CENTER)
btn4.place(relx=0.34,rely=0.18)

def returnBtn():
    bid = bookInfo1.get()
    if bid=="":
        messagebox.showinfo("Unsuccessful","Book id is missing")
    else:
        con = sqlite3.connect("main.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM bookTable WHERE book_id=?",(bid,))
        bid_detail = cur.fetchone()
        if bid_detail != None:
            if bid_detail[3] == 'issued':
                cur.execute("UPDATE bookTable SET status ='avaliable' WHERE book_id=?",(bid,))
                con.commit()
                cur.execute("DELETE FROM issuebook WHERE book_id=?",(bid,))
                con.commit()
                con.close()
                messagebox.showinfo("Successful","You have successfully returned book")
            else:
                messagebox.showinfo("Unsuccessful","Book already returned")
        else:
            print("Didn't not get any data")
    bookInfo1.delete(0,END)


def returnBook(): 
    
    global bookInfo1,SubmitBtn,quitBtn,Canvas1,con,cur,root,labelFrame, lb1

    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)

    headingFrame1 = Frame(frameBottom,bg="#bf1c19",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)
        
    headingLabel = Label(headingFrame1, text="Return Book", bg='#bf1c19', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(frameBottom,bg='#bf1c19')
    labelFrame.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)   
        
    # Book ID to Delete
    lb1 = Label(labelFrame,text="Book ID : ", bg='#bf1c19', fg='white',font=("Arial",15))
    lb1.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame,font=("Arial",15))
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(labelFrame,text="Return",bg='#d1ccc0', fg='black',command=returnBtn)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # root.mainloop()

btn5 = Button(frame,text="Return Book",bg='black', fg='white',image=resizeImg, command = returnBook,relief='ridge',bd=0,compound=CENTER)
btn5.place(relx=0.45,rely=0.18)

def submit():
    if Name.get()=="" or Class.get()=="" or Contact.get()=="" or Email.get()=="":
        messagebox.showerror("Error","All fields are required")

    else:
        conn = sqlite3.connect("main.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS students(student_id PRIMARY KEY,
                                                            name NOT NULL,
                                                            class NOT NULL,
                                                            contact NOT NULL UNIQUE,
                                                            email NOT NULL UNIQUE)""")
        cur.execute("SELECT * FROM students")
        student_id = len(cur.fetchall())
        cur.execute("""INSERT INTO students(student_id,name,class,contact,email)
        VALUES(?,?,?,?,?)""",(student_id,Name.get(),Class.get(),Contact.get(),Email.get()))
        messagebox.showinfo("Successfull",f"You are successfully registerd your student id is {student_id}")
        conn.commit()
        cur.close()
        conn.close()
        nameEntry.delete(0,END)
        classComboBox.delete(0,END)
        contactEntry.delete(0,END)
        emailEntry.delete(0,END)
        

def addStudent():
    global Name, Class, Contact, Email, nameEntry, classComboBox, contactEntry, emailEntry
    # root = tk.Tk()
    # root.title("Add student")
    # root.geometry("1366x720+0+0")
    Name = StringVar()
    Class = StringVar()
    Contact = StringVar()
    Email = StringVar()

    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)

    headingFrame1 = Frame(frameBottom,bg="light blue",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)
        
    headingLabel = Label(headingFrame1, text="Add Student", bg='light blue', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    mainFrame = Frame(frameBottom,bg="light blue")
    mainFrame.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)

    nameLabel = Label(mainFrame,text="Name :",bg="light blue",font=("Arial",15))
    nameLabel.place(relx=0.05,rely=0.15)
    nameEntry = Entry(mainFrame,width=15,font=("Arial",15),textvariable=Name)
    nameEntry.place(relx=0.5,rely=0.15,relwidth=0.45, relheight=0.08)


    classLabel = Label(mainFrame,text="Class :",bg="light blue",font=("Arial",15))
    classLabel.place(relx=0.05,rely=0.3)
    classComboBox = ttk.Combobox(mainFrame,width=13,font=("Arial",15),textvariable=Class)
    classComboBox['values'] = ('BCA',
                            'BCom',
                            'BBA',
                            'BSc')
    classComboBox.place(relx=0.5,rely=0.3,relwidth=0.45, relheight=0.08)


    contactLabel = Label(mainFrame,text="Contact :",font=("Arial",15),bg="light blue")
    contactLabel.place(relx=0.05,rely=0.45)
    contactEntry = Entry(mainFrame,width=15,font=("Arial",15),textvariable=Contact)
    contactEntry.place(relx=0.5,rely=.45,relwidth=0.45, relheight=0.08)


    emailLabel = Label(mainFrame,text="Email :",font=("Arial",15),bg="light blue")
    emailLabel.place(relx=0.05,rely=0.60)
    emailEntry = Entry(mainFrame,width=15,font=("Arial",15),textvariable=Email)
    emailEntry.place(relx=0.5,rely=.60,relwidth=0.45, relheight=0.08)

    submitBtn = Button(mainFrame,text="Submit",command = submit)
    submitBtn.place(rely=0.85,relx=0.4,relwidth=0.18,relheight=0.08)
    # root.mainloop()


btn6 = Button(frame,text="Add Student",bg='black', fg='white',image=resizeImg, command = addStudent,relief='ridge',bd=0,compound=CENTER)
btn6.place(relx=0.56,rely=0.18)

def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("",END,values=i)

def viewStudent(): 
    global trv
    con = sqlite3.connect("main.db")
    cur = con.cursor()

    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)

    headingFrame1 = Frame(frameBottom,bg="#12a4d9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)
        
    headingLabel = Label(headingFrame1, text="View Students", bg='#12a4d9', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(frameBottom,bg='black')
    labelFrame.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)

    scroll_v = Scrollbar(labelFrame)
    scroll_v.pack(side= RIGHT,fill="y")

    #Add a Horizontal Scrollbar
    scroll_h = Scrollbar(labelFrame, orient= HORIZONTAL)
    scroll_h.pack(side= BOTTOM, fill= "x")

    trv = ttk.Treeview(labelFrame,columns=(1,2,3,4,5),show="headings",height="0.4",yscrollcommand=scroll_v.set,xscrollcommand=scroll_h.set)
    trv.pack(fill=BOTH,expand=1)
    trv.heading(1,text="Student ID")
    trv.heading(2,text="Name")
    trv.heading(3,text="Class")
    trv.heading(4,text="Contact")
    trv.heading(5,text="Email")

    try:
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        con.commit()
        update(rows)
    except Exception as e:
        print(e)
        messagebox.showerror("Error","Failed to fetch data from database.")
    
    quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    # root.mainloop()


btn7 = Button(frame,text="View Student",bg='black', fg='white',image=resizeImg, command = viewStudent,relief='ridge',bd=0,compound=CENTER)
btn7.place(relx=0.67,rely=0.18)

def updateIssuedTable(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("",END,values=i)

def issuedTable(): 
    global trv
    
    con = sqlite3.connect("main.db")
    cur = con.cursor()

    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)

    headingFrame1 = Frame(frameBottom,bg="#12a4d9",bd=5)
    headingFrame1.place(relx=0.25,rely=0.02,relwidth=0.5,relheight=0.10)
        
    headingLabel = Label(headingFrame1, text="View Students", bg='#12a4d9', fg='white', font=('Courier',25,"bold"))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(frameBottom,bg='black')
    labelFrame.place(relx=0.1,rely=0.13, relwidth=0.8, relheight=0.6)
    
    scroll_v = Scrollbar(labelFrame)
    scroll_v.pack(side= RIGHT,fill="y")

    #Add a Horizontal Scrollbar
    scroll_h = Scrollbar(labelFrame, orient= HORIZONTAL)
    scroll_h.pack(side= BOTTOM, fill= "x")

    trv = ttk.Treeview(labelFrame,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="0.4",yscrollcommand=scroll_v.set,xscrollcommand=scroll_h.set)
    scroll_v.config(command=trv.yview)
    scroll_h.config(command=trv.xview)
    trv.pack(fill=BOTH,expand=1)
    trv.heading(1,text="Book ID")
    trv.heading(2,text="Book Name")
    trv.heading(3,text="Author")
    trv.heading(4,text="Status")
    trv.heading(5,text="Student Id")
    trv.heading(6,text="Student Name")
    trv.heading(7,text="Class")
    trv.heading(8,text="Contact")
    trv.heading(9,text="Email")
    lst = []
    try:
        
        cur.execute("SELECT * FROM issuebook")
        rows = cur.fetchall()
        for i in rows:
            cur.execute("SELECT * FROM bookTable WHERE book_id = ?",(i[0],))
            bookData = cur.fetchone()
            cur.execute("SELECT * FROM students WHERE student_id = ?",(i[1],))
            studentData = cur.fetchone()
            issueBookDetails = (bookData + studentData)
            print(issueBookDetails)
            lst.append(issueBookDetails)
        print(lst)
        updateIssuedTable(lst)
        con.commit()
        
    except Exception as e:
        print(e)
        messagebox.showerror("Error","Failed to fetch files from database")
    
    quitBtn = Button(labelFrame,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    

btn8 = Button(frame,text="Issued Table",bg='black', fg='white',image=resizeImg, command = issuedTable,relief='ridge',bd=0,compound=CENTER)
btn8.place(relx=0.78,rely=0.18)

def sendErrorReport():
    errorMessage = textBox.get("1.0",END)
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("officalmailtesting@gmail.com", "nnrtlgucocjcfhao")

    # sending the mail
    s.sendmail("officalmailtesting@gmail.com", "vikas84450@gmail.com", errorMessage)

    # terminating the session
    s.quit()
    messagebox.showinfo("Thank you","Thank You for sending your valueable feedback.")
    print(errorMessage)

def contactUs():
    global textBox
    frameBottom = Frame(root,bg="white")
    frameBottom.place(relx=0.2,rely=0.2, relwidth=1, relheight=1)
    rightFrame = Frame(frameBottom,bg="black")
    rightFrame.place(rely=0,relwidth=1,relheight=1)

    text = "If you face any problem you can contact with us, we will always there for you. You can mail us on the given\nemail or send whatsapp message with screenshot of the problem you faced."

    textFrame = Frame(rightFrame,bg="black")
    textFrame.place(relx=0.05,rely=0.1,relwidth=0.7,relheight=0.2)

    textLable = Label(textFrame,text=text,fg="#24f0ff",bg="black",font=("arial",15))
    textLable.place(rely=0.1)
    emailLabel = Label(rightFrame,text = "Email :",fg="#fa0070",font=("arial",15),bg="black")
    emailLabel.place(relx=0.3,rely=0.25)
    email = Label(rightFrame,text="vikas84450@gmail.com",fg="white",font=("arial",15),bg="black")
    email.place(relx=0.4,rely=0.25)
    contactLabel = Label(rightFrame,text = "Contact :",fg="#fa0070",font=("arial",15),bg="black")
    contactLabel.place(relx=0.3,rely=0.35)
    contact = Label(rightFrame,text="7985587087",fg="white",font=("arial",15),bg="black")
    contact.place(relx=0.4,rely=0.35)
    textBox = Text(rightFrame,height=10,width=50)
    textBox.place(relx=0.1,rely=0.5)
    sendBtn = Button(rightFrame,text="Send",width=25,bg="white",command=sendErrorReport)
    sendBtn.place(relx=0.5,rely=0.6)


def aboutUs():
    frameBottom = Frame(root,bg="black")
    frameBottom.place(relx=0.2,rely=0.2, relwidth=0.8, relheight=0.8)

    rightFrame = Frame(frameBottom,bg="black")
    rightFrame.place(relwidth=1,relheight=1)

    innerFrame = Frame(rightFrame,bg="black")
    innerFrame.place(relx=0.1,relwidth=0.8,relheight=0.2)
    whoWeareLabel = Label(innerFrame,text="Who We Are",bg="black",fg="#fa0070",font=("helvetica",20,"bold"))
    whoWeareLabel.pack(pady=(15,0))
    teamText = Label(innerFrame,text="We are a team of passionate coders whose are creating software to make it's users life easier. We have not worlds best \ndevelopers and testers but we have the best team and this team can do anything.",bg="black",fg="white",font=("Arial",13))
    teamText.pack()

    teamLabel = Label(rightFrame,text="Meet Our Team - Team EDITH",bg="black",fg="#fa0070",font=("helvetica",20,"bold"))
    teamLabel.place(rely=0.2,relx=0.3)

    imgGalleryFrame = Frame(rightFrame)

    imgGalleryFrame.place(rely=0.3,relx=0,relheight=0.7,relwidth=1)



    #############################################################################################

    imgFrame1 = Frame(imgGalleryFrame,bg="black",relief=RIDGE)
    imgFrame1.place(relwidth=0.33,relheight=0.5,relx=0)

    image = Image.open("vikas2.jpg")
 
    # Resize the image using resize() method
    resize_image = image.resize((170, 200))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(imgFrame1,image=img)
    label1.image = img
    label1.place(x=0,y=0)
    label2 = Label(imgFrame1,text="Vikas Rai",bg="black",fg="#24f0ff",font=("Arial",16,"bold"))
    label2.place(x=190,y=30)
    label3 = Label(imgFrame1,text="Team Leader",bg="black",fg="white")
    label3.place(x=190,y=60)

    ##############################################################################

    imgFrame2 = Frame(imgGalleryFrame,bg="black",relief=RIDGE)
    imgFrame2.place(relwidth=0.33,relheight=0.5, relx=0.33)

    image = Image.open("vikas1.jpg")
 
    # Resize the image using resize() method
    resize_image = image.resize((170, 200))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(imgFrame2,image=img)
    label1.image = img
    label1.place(x=0,y=0)

    label2 = Label(imgFrame2,text="Shaswat Pandey",bg="black",fg="#24f0ff",font=("Arial",16,"bold"))
    label2.place(x=180,y=30)
    label3 = Label(imgFrame2,text="Developer",bg="black",fg="white")
    label3.place(x=180,y=60)

    ############################################################################
    imgFrame3 = Frame(imgGalleryFrame,bg="black",relief=RIDGE)
    imgFrame3.place(relwidth=0.34, relheight=0.5, relx=0.66)

    image = Image.open("vikas3.jpg")
 
    # Resize the image using resize() method
    resize_image = image.resize((170, 200))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(imgFrame3,image=img)
    label1.image = img
    label1.place(x=0,y=0)
    label2 = Label(imgFrame3,text="Siddhart Gaurav",bg="black",fg="#24f0ff",font=("Arial",16,"bold"))
    label2.place(x=190,y=30)
    label3 = Label(imgFrame3,text="Technical Writer",bg="black",fg="white")
    label3.place(x=190,y=60)

    ############################################################################
    imgFrame4 = Frame(imgGalleryFrame,bg="black")
    imgFrame4.place(relwidth=0.33, relheight=0.5, relx=0, rely=0.5)


    image = Image.open("reetika1.jpg")
 
    # Resize the image using resize() method
    resize_image = image.resize((170, 200))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(imgFrame4,image=img)
    label1.image = img
    label1.place(x=0,y=0)
    label2 = Label(imgFrame4,text="Reetika Khare",bg="black",fg="#24f0ff",font=("Arial",16,"bold"))
    label2.place(x=190,y=30)
    label3 = Label(imgFrame4,text="Project Manager",bg="black",fg="white")
    label3.place(x=190,y=60)

    #############################################################################
    imgFrame5 = Frame(imgGalleryFrame,bg="black")
    imgFrame5.place(relwidth=0.33, relheight=0.5, relx=0.33, rely=0.5)
    image = Image.open("reet3.jpg")
 
    # Resize the image using resize() method
    resize_image = image.resize((170, 200))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(imgFrame5,image=img)
    label1.image = img
    label1.place(x=0,y=0)
    label2 = Label(imgFrame5,text="Kritika Singh",bg="black",fg="#24f0ff",font=("Arial",16,"bold"))
    label2.place(x=190,y=30)
    label3 = Label(imgFrame5,text="Tester",bg="black",fg="white")
    label3.place(x=190,y=60)

    #################################################################################
    imgFrame6 = Frame(imgGalleryFrame,bg="black")
    imgFrame6.place(relwidth=0.34, relheight=0.5, relx=0.66, rely=0.5)
    image = Image.open("reet3.jpg")
 
    # Resize the image using resize() method
    resize_image = image.resize((170, 200))
    
    img = ImageTk.PhotoImage(resize_image)
    
    # create label and add resize image
    label1 = Label(imgFrame6,image=img)
    label1.image = img
    label1.place(x=0,y=0)
    label2 = Label(imgFrame6,text="Asmita pandey",bg="black",fg="#24f0ff",font=("Arial",16,"bold"))
    label2.place(x=190,y=30)
    label3 = Label(imgFrame6,text="Tester",bg="black",fg="white")
    label3.place(x=190,y=60)
 

def contact():

    frameBottom = Frame(root,bg="white")
    frameBottom.place(rely=0.2, relwidth=1, relheight=1)
    
    sideFrame = Frame(frameBottom,bg="#24f0ff")                          # #f5cf51 #2b99ba
    sideFrame.place(relx=0,rely=0,relwidth=0.2,relheight=1)

    rightFrame = Frame(frameBottom,bg="black")
    rightFrame.place(relx=0.2,relwidth=0.8,relheight=0.8)

    pageLabel = Label(rightFrame,text="This project is created by team EDITH",bg="black",fg="#fa0070",font=("Arial",25,"bold"))
    pageLabel.place(relx=0.3,rely=0.4)
    aboutUsBtn = Button(sideFrame,text="About Us",bg="#24f0ff",fg="white",font=("Courier New",25,"bold"),bd=0,command=aboutUs)
    aboutUsBtn.place(rely=0.3,relx=0.17)
    
    contactUsBtn = Button(sideFrame,text="Contact Us",bg="#24f0ff",fg="white",font=("Courier New",25,"bold"),bd=0,command=contactUs)
    contactUsBtn.place(rely=0.5,relx=0.1)


btn9 = Button(frame,text="About us",bg='black', fg='white',image=resizeImg, command = contact,relief='ridge',bd=0,compound=CENTER)
btn9.place(relx=0.89,rely=0.18)

root.mainloop()