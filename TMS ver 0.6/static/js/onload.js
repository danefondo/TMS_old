$(document).ready(function() {

	function getFields(input, field) {
    	var output = [];
    	for (var i=0; i < input.length ; ++i)
        	output.push(input[i][field]);
    	return output;
	};

	function myTasks(input, field) {
		for(var i=0; i < input.length; ++i)
			$("#taskarea").append("<li>" + input[i][field] + "</li>");
	};

	$.get("/get", function(data) {
		tasks = data.results;
		stringified_tasks = (JSON.stringify(data.results));
		tx = "task";
		
		myTasks(tasks, tx);
	});

	$('#buttonid').click(function() {
		console.log("I made it here.");
		$.get("/get", function(data) {
			console.log(data.results);
			tasks = data.results;
			
			// Turning the retrieved data into a string for printing the JS object as is. However, getFields and myTasks functions both use loops to work with the actual data and objects.
			stringified_tasks = (JSON.stringify(data.results));
			console.log(tasks);
			$('#testanswer').text(stringified_tasks).show();

			id = tasks[0]["id"];

			$('#testanswer2').text(id).show();

			var result = getFields(tasks, "id")
			$('#testanswer2').text(result).show();
		}) // end function(data)
	}); // end click
}); // end ready

