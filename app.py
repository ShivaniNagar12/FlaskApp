from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Loveulife@12",
    database="py_pro"
)

if db.is_connected():
    print("Connected to MySQL database")

cursor = db.cursor()

@app.route('/mypage', methods=[ 'GET'])
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    contact_number = request.form['contact_number']
    date = request.form['date']
    specialist = request.form['specialist']

    # Insert data into the database
    insert_query = "INSERT INTO form (name, age,contact_number, date, specialist) VALUES (%s, %s,%s, %s, %s)"
    data = (name, age, contact_number, date, specialist)
    #data = ("krusha", "23", "0987654321", "2023-01-09", "Phsiotherapist")
    cursor.execute(insert_query, data)
    db.commit()


    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
