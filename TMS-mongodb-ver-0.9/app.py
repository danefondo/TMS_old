from flask import Flask, render_template, request, redirect, jsonify, json, session, url_for
from flask_pymongo import PyMongo
from bson import json_util
from bson.json_util import dumps
import json
from bson import ObjectId

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'unyx-tms-db'
app.config['MONGO_URI'] = 'mongodb://robertunyx:Xr5a8u2323@ds119070.mlab.com:19070/unyx-tms-db'

# INSTANTIATE DATABASE CONNECTION
mongo = PyMongo(app)


# VIEWS
@app.route('/')
def index():
	return render_template('index.html')

# Create task
@app.route('/create', methods=['POST'])
def create():

	# To insert into a collection, you must first get that collection (or create one), below 'mongo' is the object created by PyMongo(app), 'db' is the default database, which is 'unyx-tms-db' and tasks is a new collection created on the fly (if the collection exists, it finds it, if not, it creates it and it will be called 'tasks' like below in 'mongo.db.tasks')
	tasks = mongo.db.tasks
	task = request.form['task']
	print("Task: ", task)

	tasks.insert({'task' : task})
	print("Tasks: ", tasks.find())

	return jsonify({'task' : task})

# Get tasks
@app.route('/get')
def get():
	print("Beginning getting all tasks...")
	tasks_collection = mongo.db.tasks
	tasks_search = tasks_collection.find()
	print("Printing tasks: ", tasks_search)
	tasks = []
	for document in tasks_search:
		print("Original task: ", document)
		# json_document = json.dumps(document, default=json_util.default)
		document['_id'] = str(document['_id'])
		tasks.append(document)
		print("Tasks dictionary: ", tasks)
	print("Dictionary: ", tasks)
	jsonified =  jsonify({'tasks': tasks})
	print("Jsonified: ", jsonified)
	return jsonify({'tasks': tasks})

# Update task
@app.route('/update', methods=['POST'])
def update():
	print("Beginning updating task value...")
	updated_data = request.form['updated_task']
	print("Updated data: ", updated_data)
	taskid = request.form['task_id']
	print("Taskid: ", taskid)
	tasks = mongo.db.tasks
	task_to_update = tasks.find_one({'_id' : ObjectId(taskid)})
	print("Task object about to be updated: ", task_to_update)
	print("Current task in database: ", task_to_update['task'])

	task_to_update['task'] = updated_data
	print("Updated task: ", task_to_update['task'])

	tasks.save(task_to_update)
	return jsonify({'error' : 'Missing data!'})

# Remove task
@app.route('/delete', methods=['POST'])
def delete():
	print("Beginning deleting task...")
	taskid = request.form['task_id']
	print("Taskid: ", taskid)
	tasks = mongo.db.tasks
	task_to_delete = tasks.find_one({'_id' : ObjectId(taskid)})
	print("Task to delete: ", task_to_delete)
	tasks.remove(task_to_delete)
	print("Task deleted.")

	return jsonify({'error' : 'Missing data!'})

@app.route('/getlast')
def getlast():
	print("Beginning getting last query...")
	tasks = mongo.db.tasks
	lastentry = tasks.find().sort([('_id', -1)]).limit(1)
	print("Retrieved last entry: ", lastentry)
	entryid = ''
	for document in lastentry:
		entryid = document['_id']
	print("Retrieved entry id: ", entryid)
	task_search = tasks.find_one({'_id' : entryid})
	print("Retrieved task object: ", task_search)
	task = task_search['task']
	print("Retrieved entry ready to be sent: ", task)

	return jsonify({'task' : task, 'entryid' : str(entryid)})


if __name__ == '__main__':
	app.secret_key = 'mysecret'
	app.run()