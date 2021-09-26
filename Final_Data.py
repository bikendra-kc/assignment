import sqlite3

def studentData():
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Lastname text,Address text, Age text, City text, Contact text, Email text) ")
    con.commit()
    con.close()

def addStdRec( StdID , Firstname , Lastname ,Address , Age, City, Contact, Email ):
    con=sqlite3.connect('student.db')
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL,?,?,?,?,?,?,?,?)",(StdID , Firstname , Lastname ,Address , Age, City, Contact, Email))
    con.commit()
    con.close()

def viewData():
    con=sqlite3.connect('student.db')
    cur=con.cursor()
    cur.execute("SELECT * FROM student")
    rows =cur.fetchall()
    con.close
    return rows

def deleteRec(id):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("DELETE FROM student WHERE id=?",(id,))
    con.commit()
    con.close

def searchData( StdID ='' , Firstname ='' , Lastname ='' ,Address ='' , Age ='', City ='', Contact ='', Email ='' ):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=?  OR  Firstname =? OR Lastname =? OR Address =? OR \
      Age =? OR City =? OR  Contact =? OR  Email =?",(StdID , Firstname , Lastname ,Address , Age, City, Contact, Email))
    rows=cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, StdID ='' , Firstname ='' , Lastname ='' ,Address ='' , Age ='', City ='', Contact ='', Email ='' ):
    con=sqlite3.connect("student.db")
    cur=con.cursor()
    cur.execute("UPGRADE  student SET StdID=? OR  Firstname =? OR Lastname =? OR Address =? OR \
      Age =? OR City =? OR  Contact =? OR  Email =?",(StdID , Firstname , Lastname ,Address , Age, City, Contact, Email,id))
    con.commit()
    con.close()

studentData()