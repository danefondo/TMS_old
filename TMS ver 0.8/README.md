# Changes made in this version:
- Commented some code for future references.
- Added an option to delete tasks. 
- Changed from manually adding tasks to the list through JS to first sending the data to the database and then automatically retrieving it and adding it to the task area, which means there is no longer a need to refresh the page every time a task is added to get the data from the database.

## Resources used:
- https://stackoverflow.com/questions/27158573/how-to-delete-a-record-by-id-in-flask-sqlalchemy - for deleting by id
- https://stackoverflow.com/questions/8551952/how-to-get-last-record/8551979 - for getting last record
- https://stackoverflow.com/questions/46711379/how-to-get-the-auto-increment-id-in-flask-sqlalchemy-orm-mode - to get task id in python
