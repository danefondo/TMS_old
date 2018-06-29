$(document).ready(function() {


// FUNCTIONS
// DISPLAY DATA
// Function created to display data retireved from the database.

	function myTasks(input, task_field, id_field) {
		for(var i=0; i < input.length; ++i)
			$("#taskarea").append("<li class='task' id=" + input[i][id_field] + ">" + input[i][task_field] + "<button class='delete'>delete</button></li>");
	};

// GET ALL DATA	
// First retrieve all tasks from the database, if there are none, do nothing, if there are any, activate myTasks() function

		$.get("/get", function(data) {
			tasks = data.results;
			stringified_tasks = (JSON.stringify(data.results));
			tx = "task";
			ti = "id";

			if (tasks.length < 1) {
				alert("No tasks.");
			} else {
				myTasks(tasks, tx, ti);
			};
		});

// FUNCTION GET LAST ENTRY
// Function created to add new tasks to the list immediately, without updating the page

	function getLast() {

		$.get("/getlast", function(data) {
			task = data.result;
			id = data.entryid;
			stringified_task = (JSON.stringify(data.result));
			$("#taskarea").append("<li class='task' id=" + id + ">" + task + "<button class='delete'>delete</button></li>");			
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
			url : '/process'
		})
		$("#taskname").val('');
		getLast();
		event.preventDefault();
	});


}); // end ready
