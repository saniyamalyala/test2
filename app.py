from flask import *
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re,os

app=Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'Saniyasonu$55'
app.config['MYSQL_DB'] = 'db1'
app.secret_key = os.environ.get('SECRET_KEY')
mysql = MySQL(app)
@app.route('/')
def indexmethod():
	return render_template('index.html')

@app.route('/login', methods =['GET', 'POST'])
def loginmethod():
	if request.method=='POST' and 'username' in request.form and 'password' in request.form:
		username=request.form['username']
		password=request.form['password']
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM details WHERE username = % s AND passwd = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
        		return redirect(url_for('welcommethod'))
        		
	return render_template('login.html', msg='Incorrect username / password !')


@app.route('/register',methods =['GET', 'POST'])
def registermethod():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form :
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM details WHERE username = % s', (username, ))
        account = cursor.fetchone()
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers !'
        elif not username or not password or not email:
            msg = 'Please fill out the form !'
        else:
            cursor.execute('INSERT INTO details VALUES (NULL, % s, % s, % s)', (username, password, email, ))
            mysql.connection.commit()
            msg = 'You have successfully registered !'
            return redirect(url_for('loginmethod'))
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('register.html', msg = msg)

@app.route('/welcome')
def welcommethod():
	return render_template('welcome.html',msg='login successful')


if __name__=='__main__':
	app.run(debug=True,port=5003)
	
	
	
