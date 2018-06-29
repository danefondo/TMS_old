# Practice App: Task Management System

This application deals with tasks. 
Every primary manipulatable object is a task.
Tasks can belong to categories.
Tasks can belong to projects.
Tasks can have meta data, such as tags.
But they will always be tasks.
Hence the main functionality of this application is dealing with tasks.

App features, sections, requirements, components that make up ver 1.0:

- Categories: 
	Tasks to be done, 
	Completed tasks,
	Pending tasks,
	Abandoned tasks (require explanation to be able to abandon a task, match against a goal),
	Today's tasks / Current tasks (reset every 24h, return incomplete tasks to Tasks to be done),
	Next/Upcoming task(s)
- Separate meta for each task:
	Next steps to take (task breakdown into smaller steps, + some kind of system to make it easier to break tasks down, or some guide on the side),
	Date of creation,
	Project,
	Tags & Joint-tags,
	Priority
- Option to create new meta fields for tasks
	
App features, sections, requirements, components that make up ver 2.0:
- Reminders section
- Reviews / thoughts section
- Notes section
- Structured task formatting template (a fill in the blanks kind of template, e.g. "I want to do X, by Z" for creating SMART tasks):
	Option to start with a structure-free template
	Option to create new templates for re-use
	Task formatting requirement checklists for more effective task creation
- Settings:
	Option to limit the amount of Current / Today's tasks or the amount of them visible (the rest can be greyed out further, whereas tasks marked as short or mini-tasks can be more visible),
	Automatic saving
	
For next versions:
- New features meant for the UNYX Ecosystems -- where it is integrated into the whole

First basic functions breakdown:
- There is a div that will contain other divs that are the tasks
- There is an input form and a submit button
- By clicking the submit button, actions happen
- If the submit button is clicked, and there is no content in the form, or the content type is checked to not match our accepted data type, the process is halted and a notice is displayed
- If the submit button is clicked, and the form content passes all tests, the content is selected and then displayed and positioned in the list, using HTML & JS DOM manipulation (HTML element manipulation with JS)sent to the server through AJAX to then be sent and organized in the database using an SQLAlchemy model; 
- If the page is reloaded, it will check to see if there are any entries in the database, and then if there are, it will load all the task entries from the database
- It should also be possible to update (change) and delete task content
- It should be possible to change task name just by clicking on the task (if editing is enabled)
- Saving should happen automatically, multiple saved draft versions should be available and previewable; but default final saving should happen through a button (or it can be more like the google docs autosave feature)

# To-do:
Features and their breakdown into programmable tasks.
1. Basic functioning task application
	1. Displaying tasks
	- [ ] Divs
	
- [x] Properly display the tasks on the client side in an ordered list that lists the tasks by their ID in the database
- [x] Add the option to change the name of the task and update the database accordingly
- [x] Add the option to delete a task, and then update the database accordingly
- [x] Add custom id/class for each list element, or make it the original task id, which could include a keyword + id, to make it different from other list items.
- [x] Add function to automatically create divs using a for loop that will contain the task, and its id -- which get added to the taskarea div.
- [x] Turn task div into contenteditable upon clicking it, and add an option to end editing (either by hitting enter, clicking somewhere else or clicking the Done symbol) 

# Next steps
- [ ] Add a cancel button that appears when editing. 
- [ ] Add a Done symbol for ending finishing editing yourself.
- [ ] Add a cross instead of the current delete button to delete a task
- [ ] Add an option to select tasks (to later be able to perform functions on multiple tasks at once, such as deleting them)
- [ ] Add option to "undo"  certain functions (such as a recent delete or change) -- and then on either one of those events (enter, click elsewhere, done), it will update the database as well
- [ ] Add the option to add meta data to new and existing tasks, categories and other organization aiding data -- this - [ ] requires learning about one-to-one, one-to-many, many-to-one and many-to-many relationships and database models and schemas
- [ ] Add the option to display the data based on the filters you choose
- [ ] Add the option to create new filter combinations
- [ ] Add the option to search the displayed data
- [ ] Add the option to move a task to another taskarea (and update div, and later also have it organized by category, the taskarea is category 1, by changing it to taskarea2, it should organize the task in the database accordingly, and form the proper relationship)
- [ ] Add the option to create new taskareas (they will be categories or sections and components if thinking in terms of Xavar).
- [ ] Properly display the tasks on the client side in an ordered list that lists the tasks by their ID in the database
- [ ] Add the option to change the name of the task and update the database accordingly
- [ ] Add the option to delete a task, and then update the database accordingly
- [ ] Add the option to add meta data to new and existing tasks, categories and other organization aiding data -- this requires learning about one-to-one, one-to-many, many-to-one and many-to-many relationships and database models and schemas
- [ ] Add the option to display the data based on the filters you choose
- [ ] Add the option to create new filter combinations
- [ ] Add the option to search the displayed data
- [ ] Rename variables in the code to make them more relevant, tidy up the code in general
- [ ] Add option for unlimited parameters in function
- [ ] Add something that counts all the to-do's in the list
- [ ] Possibility of dragging and dropping tasks between category areas
- [ ] Settings feature: Option to enable or disable the possibility of drag and drop
- [ ] Settings feature: Option to enable or disable the possibility of live editing (non-live editing requires first clicking the edit button to enable editing)
- [ ] Settings feature: Option to enable or disable autosaving when editing or making changes

# Choice explanations:
- Using custom divs instead of list items for more flexibility
- Currently using JS & Ajax instead of Jinja2 to update frontend

# Elementary Software Checklist:

## 1. Making the program safe
### Input validation
- [ ] Check if type is valid (decide which types are safe types)
- [ ] Don't enable pure code in the input or transform it something safe
- [ ] Don't enable some ridiculously long line of whatever keycode, purely to main aesthetic qualities.
	
# To run this app:
On Apple computers:
1. Install homebrew
2. Deinstall Python3 (brew uninstall python3)
3. Install Python3 (brew install python3), comes with pip3
4. Install Flask (pip3 install Flask)
5. Install Flask-PyMongo (pip3 install Flask-PyMongo)
(for SQLAlchemy versions: (pip3 install flask-sqlalchemy))
6. Install bson (pip3 install bson)

# Examples of to-do web apps
- http://task5.herokuapp.com/
  - the code for the app: https://github.com/helloflask/todo
- http://todomvc.com/examples/vanillajs/
