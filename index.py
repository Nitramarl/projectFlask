from flask import Flask, render_template,request
from project import Project

app = Flask(__name__)

@app.route('/')

def morning():
   return  render_template('index.html')

@app.route('/add', methods=['POST'])
def login():
    name = request.form['name_form']
    type = request.form['type_form']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    amount = request.form['amount']
    description= request.form['description']

    Project.create(name=name, type=type, start_date=start_date,end_date=end_date, amount=amount, description=description)

    return 'Project added sucessfully'
app.run(debug='true')

