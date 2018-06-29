var submit = $("#tasksubmit");
var inputvar = $('input[name="taskname"]');


submit.click(function() {
	inputcontent = inputvar.val();
	$("#taskarea").append("<p>" + inputcontent + "</p>");
});