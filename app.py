from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import os
app = Flask(__name__)


app.config['MYSQL_HOST'] = os.getenv('mysql_host')
app.config['MYSQL_USER'] = os.getenv('mysql_user')
app.config['MYSQL_PASSWORD'] = os.getenv('mysql_pwd')
app.config['MYSQL_DB'] = os.getenv('mysql_db')

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run(host="0.0.0.0", port=port)