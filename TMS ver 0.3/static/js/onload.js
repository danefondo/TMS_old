$(document).ready(function() {
	$('#buttonid').click(function() {
		console.log("I made it here.");
		$.get("/get", function(data) {
			console.log(data.task2)
			$('#testanswer').text(data.task2).show();
		}) // end function(data)
	}); // end click
}); // end ready

