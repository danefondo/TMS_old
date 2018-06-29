$(document).ready(function() {

// Create variables for the task submit function, and to store sent input content

var submit = $("#tasksubmit");
var inputvar = $('input[name="tasked"]');

// When submit button is clicked, manually add the task to the list without using the server

//submit.click(function() {
//	inputcontent = inputvar.val();
//	$("#taskarea").append("<li>" + inputcontent + "</li>");
//});

// When a task is clicked, make it editable

	$("body").on('click', '.task', function() {
		this.contentEditable = true;
		this.focus();
	}); // end on

// When something other than the task box is clicked, return task to default uneditable state

	$("body").on('blur', '.task', function() {
		this.contentEditable = false;
	}); // end on

// When something is changed in the task, send updated version to the server for updating the database

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

// When the delete button is clicked, notify server to delete the task from the database, then delete the html element

	$("body").on('click', '.delete', function() {

		task_id = $(this).parent().attr('id');

		$.ajax({
			data : {
				task_id : task_id
			},
			type : 'POST',
			url : '/delete'
		})
		$(this).parent().remove();
		event.preventDefault();
	});

});