An improved implementation of TMS ver 0.4, where the queried SQLAlchemy objects are more elegantly convereted into a Python dictionary, and that Python dictionary presented to the browser in a useful format that enables effectively displaying the information on the client side. It also provides more safety.

Resources used to accomplish latest changes:
- https://stackoverflow.com/questions/23420275/flask-converting-python-dict-to-json-object-for-client-api
- http://flask.pocoo.org/docs/0.12/api/#flask.json.jsonify
- https://codingnetworker.com/2015/10/python-dictionaries-json-crash-course/
- https://stackoverflow.com/questions/7907596/json-dumps-vs-flask-jsonify
