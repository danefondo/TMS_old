$(document).ready(function() {


// DISPLAY DATA

	function myTasks(input, task_field, id_field) {
		for(var i=0; i < input.length; ++i)
			$("#taskarea").append("<li class='task' id=" + input[i][id_field] + ">" + input[i][task_field] + "</li>");
	};

// POST DATA

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				task : $('#taskname').val(),
			},
			type : 'POST',
			url : '/process'
		})
		$("#taskname").val('');
		event.preventDefault();
	});

// GET DATA	

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
}); // end ready

