var submit = $("#tasksubmit");
var inputvar = $('input[name="tasked"]');


submit.click(function() {
	inputcontent = inputvar.val();
	$("#taskarea").append("<li>" + inputcontent + "</li>");
});