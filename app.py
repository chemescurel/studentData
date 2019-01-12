from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)

class Student(object):
    def __init__(self, idnum, firstname, lastname, middlename,sex, Course, Yr):
        self.id_no = idnum
        self.f_name = firstname
        self.l_name = lastname
        self.mid = middlename
        self.sex = sex
        self.course = Course
        self.Yr = Yr

conn = sql.connect('newdb.db')
cur =  conn.cursor()
conn.execute('CREATE TABLE IF NOT EXISTS studentRecord(ID TEXT PRIMARY KEY  NOT NULL CHECK(length(ID)=9), First_Name TEXT  CHECK(length(First_Name)>0 AND length(First_Name)<=20 ), Last_Name TEXT CHECK(length(Last_Name)>0 AND length(Last_Name)<=20 ), Middle_Name TEXT CHECK(length(Middle_Name)>0 AND length(Middle_Name)<=20 ) , Sex TEXT CHECK(length(Sex)=1), Course TEXT CHECK(length(Course)>0 AND length(Course)<=20 ), Yr_Lvl INTEGER CHECK(length(Yr_Lvl)=1), FOREIGN KEY(Course) REFERENCES stud_Courses(course_id))')

conn.close()



@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/add",methods = ['POST','GET'])
def add():
    return render_template("login.html")

@app.route("/adding",methods = ['POST','GET'])
def adding():
    if request.method == "POST":
        try:
            id_number = request.form['id_number']
            print id_number
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            middle = request.form['Middle']
            sex =request.form['Sex']
            course = request.form['Course']
            Yr = request.form['Year']

            stud = Student(id_number,firstname,lastname,middle,sex,course,Yr)
            with sql.connect("newdb.db") as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO studentRecord(ID,First_Name,Last_Name,Middle_Name, Sex, Course,Yr_Lvl) VALUES(?,?,?,?,?,?,?)",
                    (stud.id_no, stud.f_name, stud.l_name, stud.mid, stud.sex, stud.course,stud.Yr))
                conn.commit()

                msg = "Record added successfully!"
        except:
            conn.rollback()
            msg = "Error in insertion operation. The ID number may already existed"

        finally:
            print "finally ariel happen to me"
            conn = sql.connect("newdb.db")
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM studentRecord")
            rows = cur.fetchall()
            return render_template("result.html", rows=rows, msg=msg)
            conn.close()





@app.route("/delete",methods=['POST', 'GET'])
def delete():
    conn = sql.connect("newdb.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM studentRecord")
    rows = cur.fetchall()
    conn.close()
    return render_template("delete.html",rows=rows)

@app.route("/deleting",methods = ['POST','GET'])
def deleting():
    if request.method == "POST":
        try:
            id_number = request.form['id_number']
            print id_number
            with sql.connect("newdb.db") as conn:
                print "connected"
                cur = conn.cursor()
                cur.execute("SELECT * FROM studentRecord")
                for row in cur.fetchall():
                    print row
                    if row[0] == id_number:
                        cur.execute("DELETE FROM studentRecord WHERE ID = ?", (id_number,))
                        conn.commit()
                        msg = "Successfully Deleted"
                        break
                    else:
                        msg = "That student does not exist.. Who's that pokemon!"
        except:
            msg = "Fail to delete"
        finally:
            conn = sql.connect("newdb.db")
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM studentRecord")
            rows = cur.fetchall()
            return render_template("result.html", rows=rows,msg=msg)
        conn.close()


@app.route("/update",methods = ['POST', 'GET'])
def update():
    conn = sql.connect("newdb.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM studentRecord")
    rows = cur.fetchall()
    return render_template("update.html",rows=rows)

@app.route("/updating",methods = ['POST', 'GET'])
def updating():
    if request.method == "POST":
        try:
            id_number = request.form['id_number']
            print "meeeee"
            with sql.connect("newdb.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM studentRecord")
                for row in cur.fetchall():
                    if row[0] == id_number:
                        print row
                        copied = row
                        msg = " existed"
                        break
                    else:
                        msg = "KRUUUUU"
                        copied = " "
        except:
            msg = "ERROR"
            copied=" "
        finally:
            return render_template("up.html", msg=msg, copied=copied)
            conn.close()

@app.route("/dating",methods = ['POST', 'GET'])
def dating():
    if request.method =="POST":
        try:
            id_number = request.form['id_number']
            print id_number
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            middle = request.form['Middle']
            sex = request.form['Sex']
            course = request.form['Course']
            Yr = request.form['Year']

            with sql.connect("newdb.db") as conn:
                cur = conn.cursor()
                cur.execute("SELECT * FROM studentRecord")
                for row in cur.fetchall():
                    print row
                    if row[0] == id_number:
                        print id_number
                        cur.execute("UPDATE studentRecord set First_Name = ?, Last_Name = ?, Middle_Name = ?,  Sex = ?, Course = ?, Yr_Lvl = ? where ID = ?",
                            ( firstname, lastname, middle, sex, course,Yr,id_number))
                        conn.commit()
                        msg = "successfully UPDATED"
                        break
                    elif not row[0] == id_number:
                        msg = "ERROR. You cannot Change your ID no."

        except:
            msg = "FAIL to UPDATE"
        finally:
            conn = sql.connect("newdb.db")
            conn.row_factory = sql.Row
            cur = conn.cursor()
            cur.execute("SELECT * FROM studentRecord")
            rows = cur.fetchall()
            return render_template("result.html", rows=rows, msg=msg)
            conn.close()


@app.route("/table")
def show_list():
    conn = sql.connect("newdb.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM studentRecord")
    rows = cur.fetchall()

    conn.close()
    return render_template("table.html",rows=rows)

@app.route("/CourseTable")
def CourseTable():
    conn = sql.connect("newdb.db")

    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM result")
    rows = cur.fetchall()

    conn.close()

    return render_template("cur_tab.html", rows=rows)

@app.route("/search",methods = ['POST', 'GET'])
def search():
    return render_template("search.html")

@app.route("/searching",methods = ['POST', 'GET'])
def searching():
    if request.method == "POST":
        try :
            dis = request.form["srch"]
            print dis

            conn = sql.connect("newdb.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM ALL_info where course_id = ? or First_Name = ? or c_name=? or Last_Name=? or Middle_Name=? or ID = ? or College=? or Sex=? or Yr_Lvl=?", (dis,dis,dis,dis,dis,dis,dis,dis,dis))
            print "im still performed"
            coffee = cur.fetchall()
            msg = "existed"

        except:
            msg = "ERROR"
        finally:
            print coffee
            print " copied"
            print "the message: " + msg
            return render_template("exist.html", msg=msg, coffee=coffee)


if __name__ == "__main__":
    app.run(debug=True)