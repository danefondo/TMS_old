$(document).ready(function() {

var submit = $("#tasksubmit");
var inputvar = $('input[name="tasked"]');


submit.click(function() {
	inputcontent = inputvar.val();
	$("#taskarea").append("<li>" + inputcontent + "</li>");
});

	$("body").on('click', '.task', function() {
		this.contentEditable = true;
		this.focus();
	}); // end on

	$("body").on('blur', '.task', function() {
		this.contentEditable = false;
	}); // end on

	$("body").on('propertychange change input paste', '.task', function() {

		updated_task = $(this).text();
		task_id = $(this).attr('id');

		$.ajax({
			data : {
				updated_task : updated_task, 
				task_id : task_id
			},
			type : 'POST',
			url : '/update'
		})
		event.preventDefault();
	});

});