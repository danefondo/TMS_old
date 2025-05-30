$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				task : $('#taskname').val(),
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.task).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});