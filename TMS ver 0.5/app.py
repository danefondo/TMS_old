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

    def as_dict(self):
    	obj_d = {
    		'id': self.id,
    		'task': self.task
    	}
    	return obj_d

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
	print("Beginning task querying...")
	tasks = Task.query.all()
	print("Queried tasks: ", tasks)

	print("Beginning converting queried SQLAlchemy objects into Python dictionary...")
	results = [task.as_dict() for task in tasks]
	print("Resulted Python dictionary: ", results)

	return jsonify({'count': len(results), 'results': results})

if __name__ == '__main__':
	app.run()

## ALTERNATIVELY FOR DEBUGGING: 
##  if __name__ == '__main__':
##	app.run(debug=True)
