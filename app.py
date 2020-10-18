from flask import Flask, render_template, request, g, redirect
import sqlite3

#conn = sqlite3.connect('CRUD.db')

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('CRUD.db')
    return db

# A name for the table and statements
#def create_table():
#	c.execute("""CREATE TABLE students(
#		IDNUM TEXT PRIMARY KEY NOT NULL,
#		NAME TEXT NOT NULL,
#		COURSE TEXT NOT NULL,
#		YR_LEVEL TEXT NOT NULL)""")
#	conn.commit()
#	conn.close()

@app.route('/', methods =['GET','POST'])
def home():
	if request.method == 'POST':
		userDetails = request.form
		idnum = userDetails['idnum']
		name = userDetails['name']
		yearlv = userDetails['yearlv']
		course = userDetails['course']
		cur = get_db().cursor()
		cur.execute("INSERT INTO students VALUES (:idnum, :name, :course, :year_level)",
			{'idnum': idnum, 'name': name, 'course': course, 'year_level': yearlv})
		get_db().commit()
		get_db().close()
		return '<h1>Task Successful<h1> type /List_page to see the list'
	return render_template('index.html')

@app.route('/List_page')
def student_list():
	cur = get_db().cursor()
	everyone = cur.execute('SELECT * FROM students')
	userDetails = cur.fetchall()
	return render_template('home.html',userDetails=userDetails)

@app.route('/delete', methods =['GET','POST'])
def delete_profile():
	cur = get_db().cursor()
	userDetails = request.form
	if request.method == 'POST':
		idnum = userDetails['idnum']
		cur.execute("DELETE FROM students WHERE IDNUM = :idnum",
			{'idnum': idnum})
		get_db().commit()
		get_db().close()
		return redirect('/List_page')
	return render_template('delete.html',userDetails=userDetails)

@app.route('/new_name', methods =['GET','POST'])
def rename_profile():
	cur =get_db().cursor()
	userDetails = request.form
	if request.method == 'POST':
		idnum = userDetails['idnum']
		new_name = userDetails['new']
		cur.execute("""UPDATE students
			SET NAME = :name
			WHERE IDNUM = :idnum""",
			{'name': new_name, 'idnum': idnum})
		get_db().commit()
		get_db().close()
		return redirect('/List_page')
	return render_template('new_name.html', userDetails=userDetails)

@app.route('/new_id', methods =['GET','POST'])
def reID_profile():
	cur =get_db().cursor()
	userDetails = request.form
	if request.method == 'POST':
		idnum = userDetails['idnum']
		new = userDetails['new']
		cur.execute("""UPDATE students
			SET IDNUM = :newid
			WHERE IDNUM = :idnum""",
			{'newid': new, 'idnum': idnum})
		get_db().commit()
		get_db().close()
		return redirect('/List_page')
	return render_template('new_id.html', userDetails=userDetails)

@app.route('/new_course', methods =['GET','POST'])
def recourse_profile():
	cur =get_db().cursor()
	userDetails = request.form
	if request.method == 'POST':
		idnum = userDetails['idnum']
		new_course = userDetails['new']
		cur.execute("""UPDATE students
			SET COURSE = :course
			WHERE IDNUM = :idnum""",
			{'course': new_course, 'idnum': idnum})
		get_db().commit()
		get_db().close()
		return redirect('/List_page')
	return render_template('new_course.html', userDetails=userDetails)

@app.route('/new_yearlv', methods =['GET','POST'])
def newylv_profile():
	cur =get_db().cursor()
	userDetails = request.form
	if request.method == 'POST':
		idnum = userDetails['idnum']
		new_yrlv = userDetails['new']
		cur.execute("""UPDATE students
			SET YR_LEVEL = :yrlv
			WHERE IDNUM = :idnum""",
			{'yrlv': new_yrlv, 'idnum': idnum})
		get_db().commit()
		get_db().close()
		return redirect('/List_page')
	return render_template('new_yearlv.html', userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
