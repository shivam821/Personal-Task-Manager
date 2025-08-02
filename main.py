from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
import os 

app = Flask(__name__)

db = mysql.connector.connect(
    host='#',
    port=3306,
    user='#',
    password='#',
    database='#'
)

# db = mysql.connector.connect (
#     host = os.environ.get("DB_HOST"),
#     user = os.environ.get("DB_USER"),
#     password = os.environ.get("DB_PASS"),
#     database = os.environ.get("DB_NAME")
# )

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name'][:20]
        review = request.form['review'][:40]
        title = request.form['title'][:80]
        cursor = db.cursor()
        cursor.execute("insert into blogs (name,title,review) values (%s,%s,%s)", (name, title, review))
        db.commit()
        cursor.close()
    
    # This part executes for both GET and POST requests
    cursor = db.cursor(dictionary=True)
    cursor.execute("select * from blogs order by id DESC")
    posts = cursor.fetchall()
    cursor.close()
    return render_template('spa.html', posts=posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)