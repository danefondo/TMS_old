$(document).ready(function() {
	$('#buttonid').click(function() {
		console.log("I made it here.");
		$.get("/get", function(data) {
			console.log(data.results)
			final = (JSON.stringify(data.results));
			$('#testanswer').text(final).show();
			alert(JSON.stringify(data.results) );
		}) // end function(data)
	}); // end click
}); // end ready

