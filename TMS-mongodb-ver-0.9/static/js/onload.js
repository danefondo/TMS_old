$(document).ready(function() {


// FUNCTIONS
// DISPLAY DATA
// Function created to display data retireved from the database.
	function myTasks(input, task_field, id_field) {
		console.log(input);
		for(var i=0; i < input.length; ++i)
			$("#taskarea").append("<li id=" + input[i][id_field] + "><p class='task'>" + input[i][task_field] + "</p><button class='delete' contenteditable='false'>delete</button></li>");
	};
// GET ALL DATA	
// First retrieve all tasks from the database, if there are none, do nothing, if there are any, activate myTasks() function
		$.get("/get", function(data) {
			console.log("Made it here.");
			tasks = data.tasks;
			tx = "task";
			ti = "_id";
			console.log(tasks);
			if (tasks.length < 1) {
				alert("No tasks.");
			} else {
				myTasks(tasks, tx, ti);
			}; 
			event.preventDefault();
		});

// FUNCTION GET LAST ENTRY
// Function created to add new tasks to the list immediately, without updating the page

	function getLast() {

		$.get("/getlast", function(data) {
			task = data.task;
			id = data.entryid;
			stringified_task = (JSON.stringify(data.task));
			$("#taskarea").append("<li id=" + id + "><p class='task'>" + task + "</p><button class='delete'>delete</button></li>");			
		});
	};	


// POST DATA
// Retrieves the content of the input field and sends it to the server, then activates getLast() function

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				task : $('#taskname').val(),
			},
			type : 'POST',
			url : '/create'
		})
		$("#taskname").val('');
		getLast();
		event.preventDefault();
	});


}); // end ready
