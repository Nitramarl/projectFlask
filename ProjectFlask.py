from flask import Flask,render_template,request, redirect
from project import Project
from pygal import Pie,Bar


app = Flask(__name__)

# @app.route('/')
# def dashboard():
#     # projects=Project.select()
#     return render_template('index.html', projects_to_send=Project.select())

@app.route('/add', methods=['POST'])
def login():
    name = request.form['name_form']
    type = request.form['type_form']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    amount = request.form['amount']
    description= request.form['description']

    Project.create(name=name, type=type, start_date=start_date,end_date=end_date, amount=amount, description=description)

    return redirect('/')

@app.route('/delete/<int>/')
def delet(int):
    Project.delete_by_id(int)
    return redirect('/')

@app.route('/')
def pie_route():
    projects = Project.select()
    pie_chart = Pie()
    pie_chart.title = 'Browser usage in February 2012 (in %)'

    # instatiating two variables internal and external
    internal = 0
    external = 0

    for project in projects:
        if(project.type == 'internal'):
            internal += 1
        else:
            external += 1
    pie_chart.add('internal', internal)
    pie_chart.add('external', external)


    pie_chart.render()
    chart = pie_chart.render_data_uri()

    return render_template('index.html', projects_to_send= projects, chart=chart)

@app.route('/bar')
def bar_route():
    projects = Project.select()
    bar_chart = Bar()
    bar_chart.title = 'Bar graphs (in %)'

      # instatiating two variables internal and external
    title = 0
    amount = 0

    for project in projects:
        if(project.type == 'title'):
            title += 1
        else:
            amount += 1
    bar_chart.add('title', title)
    bar_chart.add('amount', amount)


    bar_chart.render()
    chart = bar_chart.render_data_uri()

    return render_template('index.html', projects_to_send= projects, chart=chart)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    name = request.form['name_edit']
    type = request.form['type_form_edit']
    start_date = request.form['start_date_edit']
    end_date = request.form['end_date_edit']
    amount = request.form['amount_edit']
    description = request.form['description_edit']

    project = Project.get(Project.id == id)
    project.name = name
    project.type = type
    project.start_date = start_date
    project.end_date = end_date
    project.amount = amount
    project.description = description
    project.save()

    return redirect('/')


app.run(debug='true')
