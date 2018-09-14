import sqlite3

dbFile = raw_input("Enter file name:  ") + '.db'

conn = sqlite3.connect(dbFile)
dbQuer = conn.cursor()

class Student(object):
    def __init__(student, IdNumber, FirstName, LastName, Course, Year, Gender):
        student.idNum = IdNumber
        student.fstName = FirstName
        student.lstName = LastName
        student.course = Course
        student.year = Year
        student.gender = Gender



def createDB():
     dbQuer.execute('''CREATE TABLE IF NOT EXISTS records(IDnum TEXT, fname TEXT, lname TEXT, course TEXT, year TEXT, gender TEXT)''')
     print "File is ready...\n"


def addStud(stud):
    dbQuer.execute('''INSERT into records(IDnum, fname, lname, course, year, gender)VALUES(?,?,?,?,?,?)''',(stud.idNum, stud.fstName, stud.lstName, stud.course, stud.year, stud.gender))
    print  '\t\tStudent was successfully added to the database '
    conn.commit()

def deleteStud():
    delID = raw_input('Enter ID:  ')
    dbQuer.execute("DELETE from records WHERE IDnum = ?",(delID,))
    print '\t\tDELETE SUCCESS!'
    conn.commit()

def updateStud():
    updateID = raw_input('\tEnter ID:   ')
    print '\tWhat do you want to update? [Select a number]'
    print '\t\t[1]   First Name'
    print '\t\t[2]   Last Name'
    print '\t\t[3]   Course'
    print '\t\t[4]   Year'
    print '\t\t[5]   Gender'

    updateChoice = raw_input('Choice:   ')

    if updateChoice == "1":
        new_fName = raw_input("New First Name:   ")
        conn.execute("UPDATE records set fname = ? where IDnum =?",(new_fName,updateID,))
        print '\t\t\tUPDATE SUCCESS!'
        conn.commit()

    elif updateChoice == "2":
        new_lName = raw_input("New Last Name:   ")
        conn.execute("UPDATE records set lname = ? where IDnum = ?",(new_lName, updateID,))
        print '\t\t\tUPDATE SUCCESS!'
        conn.commit()

    elif updateChoice == "3":
        new_course = raw_input("New Course:   ")
        conn.execute("UPDATE records set course = ? where IDnum = ?", (new_course,updateID,))
        print '\t\t\tUPDATE SUCCESS!'
        conn.commit()

    elif updateChoice == "4":
        new_year = raw_input("New Year Level:   ")
        conn.execute("UPDATE records set level = ? where IDnum = ?", (new_level,updateID,))
        print '\t\t\tUPDATE SUCCESS!'
        conn.commit()

    elif updateChoice == "5":
        new_gender = raw_input("New Gender:   ")
        conn.execute("UPDATE records set gender = ? where IDnum = ?", (new_gender,updateID,))
        print '\t\t\tUPDATE SUCCESS!'
        conn.commit()

    else:
        print 'CHOICE IS INVALID. TRY AGAIN'


def searchStud():
    searchID = raw_input('Enter ID:  ')
    dbQuer.execute("SELECT * FROM records WHERE IDnum = ?", (searchID,))
    for row in dbQuer.fetchall():
        print "  ", row[0], "  ", row[1], "  ", row[2], "  ", row[3]


def printStud():
    dbQuer.execute('SELECT * FROM records')
    for row in dbQuer.fetchall():
        print "  ",row[0],"  ",row[1],"  ",row[2],"  ",row[3]



def sortingStud(sortChoice):

    if sortChoice == "1":
        dbQuer.execute("SELECT * FROM records ORDER BY IDnum ASC")
        for row in dbQuer.fetchall():
            print "  ", row[0], "  ", row[1], "  ", row[2], "  ", row[3]
    elif sortChoice == "2":
        dbQuer.execute("SELECT * FROM records ORDER BY IDnum DESC")
        for row in dbQuer.fetchall():
            print "  ", row[0], "  ", row[1], "  ", row[2], "  ", row[3]
    else:
        print 'CHOICE IS INVALID. TRY AGAIN'

def main():
    createDB()

    while(True):

     #   print "\n     Select Features"
        print "[1]  Add Student"
        print "[2]  Delete Student"
        print "[3]  Update Student"
        print "[4]  Search a Student"
        print "[5]  Sort by ID NUMBER"
        print "[6]  Show database"
        print "[7]  EXIT"

        feature_select = raw_input("\t\t\tSelect a number:   ")
        if feature_select == "1":
            idNum = raw_input("\t\tEnter your ID Number : ")
            fName = raw_input("\t\tEnter your First Name: ")
            lName = raw_input("\t\tEnter your Last Name: ")
            course = raw_input("\t\tEnter your Course: ")
            year = raw_input("\t\tEnter your Year: ")
            gender = raw_input("\t\tEnter your Gender: ")

            stud = Student(idNum, fName, lName, course, year, gender)
            addStud(stud)

        elif feature_select == "2":
            deleteStud()
        elif feature_select == "3":
            updateStud()
        elif feature_select == "4":
            searchStud()
        elif feature_select == "5":
            print '\t\ttSort by '
            print  '\t\t[1]   ASCENDING'
            print  '\t\t[2]   DESCENDING'
            sortChoice = raw_input("Select a number:   ")
            sortingStud(sortChoice)
        elif feature_select == "6":
            printStud()
        elif feature_select == "7":
            print '\t\tCLOSING PROGRAM...'
            quit(1)
        else:
            print '\t\tChoice is invalid. Try again'


    dbQuer.close()
    conn.close()


if __name__ == '__main__':
    main()
