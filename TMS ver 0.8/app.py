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

	return jsonify({'task' : task})

@app.route('/get')
def get():
	print("Beginning task querying...")
	tasks = Task.query.all()
	print("Queried tasks: ", tasks)

	print("Beginning converting queried SQLAlchemy objects into Python dictionary...")
	results = [task.as_dict() for task in tasks]
	print("Resulted Python dictionary: ", results)

	return jsonify({'count': len(results), 'results': results})

@app.route('/update', methods=['POST'])
def update():
	print("Beginning updating task value...")
	updated_data = request.form['updated_task']
	print("Updated data: ", updated_data)
	taskid = request.form['task_id']
	print("Taskid: ", taskid)
	task_to_update = Task.query.get(int(taskid))
	print(task_to_update)
	print(task_to_update.task)
	print(type(task_to_update.task))

	task_to_update.task = updated_data
	print("Updated task: ", task_to_update.task)

	db.session.commit()
	print("Commit complete.")

	return jsonify({'error' : 'Missing data!'})

@app.route('/delete', methods=['POST'])
def delete():
	print("Beginning deleting task...")
	taskid = request.form['task_id']
	print("Taskid: ", taskid)
	task_to_delete = Task.query.filter_by(id=taskid)
	print("Task to delete: ", task_to_delete)
	task_to_delete.delete()
	print("Task deleted.")
	db.session.commit()
	print("Commit complete.")

	return jsonify({'error' : 'Missing data!'})

@app.route('/getlast')
def getlast():
	print("Beginning getting last query...")
	lastentry = Task.query.order_by('-id').first()
	print("Retrieved last entry: ", lastentry)
	entryid = lastentry.id
	print("Retrieved entry id: ", lastentry.id)
	entrytodict = lastentry.as_dict()
	print("Retrieved entry converted into Python dictionary: ", entrytodict)
	result = entrytodict["task"]
	print("Retrieved entry ready to be sent: ", result)

	return jsonify({'result' : result, 'entryid' : entryid})


if __name__ == '__main__':
	app.run()

## ALTERNATIVELY FOR DEBUGGING: 
##  if __name__ == '__main__':
##	app.run(debug=True)