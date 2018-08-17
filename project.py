from peewee import *
from datetime import date

try:
    db = PostgresqlDatabase('project', host='localhost', user='postgres', password=12345)

except:
    print('connection unsucessful')


class Project(Model):
    name = CharField()
    type = CharField()
    start_date = DateField()
    end_date = DateField()
    amount = IntegerField()

    description = TextField()

    class Meta:
        database = db  # this model uses the "Project.db" database
        # table = "Projects"
        table_name = 'projects'


db.connect()

Project.create_table(fail_silently="true")

print("table created")


# record_one = Project.create(name="project uno", type="internal", start_date = date(2018,8,10), end_date=date(2018,9,10), amount=120000,description='Am happy')
#
#  print(Project.select().get())
# for project in Project.select():
#     print(project)




