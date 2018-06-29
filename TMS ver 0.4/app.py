from flask import Flask, render_template, request, jsonify, redirect, json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# MODELS 

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.Text)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return '<Task: %s>' % self.task

# INITIATE DATABASE

db.drop_all()
db.create_all()

# VIEWS

@app.route('/')
def index():
	return render_template('home.html')

@app.route('/process', methods=['POST'])
def process():

	task = request.form['task']
	print("task: ", task)

	task2 = Task(task)
	db.session.add(task2)
	db.session.commit()

	if task:
		newTask = task[::-1]
		print("newTask: ", newTask)
		return jsonify({'task' : newTask})

	return jsonify({'error' : 'Missing data!'})

@app.route('/get')
def get():
	print("Step1")
	testquery = Task.query.all()
	print("Step2")
	print(testquery)
	print("testquery.task: ", testquery)

	l = []

	dicts = []

	for u in testquery:
		print(u)
		print(u.__dict__)
		querytodict2 = u.__dict__
		print("querytodict2: ", querytodict2)
		querytodict2.pop('_sa_instance_state', None)
		print("querytodict2: ", querytodict2)
		dicts.append(querytodict2)
		print("dicts: ", dicts)

	for i in dicts:
		print("task raw: ", i)
		print("task item: ", i["task"])
		l.append(i["task"])
		print("list: ", l)

	return jsonify({'task2' : l})

if __name__ == '__main__':
	app.run()

## ALTERNATIVELY FOR DEBUGGING: 
##  if __name__ == '__main__':
##	app.run(debug=True)