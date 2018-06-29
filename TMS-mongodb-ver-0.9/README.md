Resources used:

How MongoDB's id field works:
https://www.vividcortex.com/blog/what-is-mongodbs-_id-field-and-how-to-use-it

To query database by id using PyMongo requires wrapping it inside ObjectId:
https://stackoverflow.com/questions/16073865/search-by-objectid-in-mongodb-with-pymongos

How PyMongo database collections work (as in a method such as find() gives a cursor object, which is iterable (it's a Python dictionary)):
https://stackoverflow.com/questions/39705843/pymongo-bson-to-json-dict-conversion-dumps-returns-a-json-string

Deeper explanation of how Python Cursor works:
https://stackoverflow.com/questions/28968660/how-to-convert-a-pymongo-cursor-cursor-into-a-dict/28970776

Converting document id into string:
https://stackoverflow.com/questions/45615855/object-of-type-objectid-is-not-json-serializable

Appending documents to list in PyMongo:
https://stackoverflow.com/questions/11280382/object-is-not-json-serializable?rq=1

How lists work in Python:
https://stackoverflow.com/questions/26581397/what-does-the-list-function-do-in-python

Searching PyMongo collections:
https://stackoverflow.com/questions/30333299/pymongo-bson-convert-python-cursor-cursor-object-to-serializable-json-object

Getting id of an object in PyMongo:
https://stackoverflow.com/questions/31077812/how-do-i-get-id-of-an-object-in-pymongo

Creating custom id's in PyMongo:
https://stackoverflow.com/questions/19524725/how-to-autoincrement-id-at-every-insert-in-pymongo

On collision-management for similar IDs:
https://stackoverflow.com/a/12241048/8010396

On avoiding data loss in case of servers going down:
https://stackoverflow.com/a/30786681/8010396

# Questions

- What is the difference between .find() and .find({})? What purpose do the empty brackets serve?

