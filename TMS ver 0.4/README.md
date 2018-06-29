A full implementation of a CRUD application that queries ALL the items in the created database, and then displays them. The biggest breakthrough was being able to convert the SQLAlchemy row object into a dictionary, removing unnecessary SQLAlchemy model parts, finding a way to access the desired parts of the dictionary (selecting the actual tasks), and then sending them back to the browser, client-side JS file to be displayed on the website. The success is seen by refreshing the page; when the page is refreshed, and you ask for your tasks to be displayed, they are successully displayed from the database, demonstrating a successful implementation of creating and reading and displaying data.

A test.db file is created in the process of creating the database, in fact, that is the demo database.

Stack: Python, Flask, Flask-SQLAlchemy, jsonify, JSON, Ajax, JavaScript, jQuery
