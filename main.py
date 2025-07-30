from flask import Flask, render_template,request
import mysql.connector
import os 

app = Flask(__name__)

db = mysql.connector.connect (
    host = os.environ.get("DB_HOST"),
    user = os.environ.get("DB_USER"),
    password = os.environ.get("DB_PASS"),
    database = os.environ.get("DB_NAME")
)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        task = request.form['task']
        cursor = db.cursor()
        cursor.execute("insert into tasks (tasks_name) values (%s)",(task,))
        db.commit()
        cursor.close()
        return 'Task Added Sucessfully'
    return render_template ('home.html')

if __name__ == '__main__' : 
    app.run(host='0.0.0.0',port=5000,debug=True)