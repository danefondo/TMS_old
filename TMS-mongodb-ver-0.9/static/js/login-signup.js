$(document).ready(function() {

	// LOGIN

	$('#login').on('submit', function(event) {
		$.ajax({
			data : {
				username : $('#username').val(),
				pass : $('#password').val()
			},
			type : 'POST',
			url : '/login'
		}).done(function(data) {
			console.log(data.error);
			if (data.error) {
				x = data.error;
				$('#testbox2').append('<p>' + x + '</p>');
			};

		});

		$('#username').val('');
		$('#password').val('');
		event.preventDefault();
	});

	// REGISTER

	$('#register').on('submit', function(event) {
		$.ajax({
			data : {
				username : $('#username').val(),
				pass : $('#password').val()
			},
			type : 'POST',
			url : '/register'
		}).done(function(data) {
			console.log(data);
			console.log(data.error);
			if (data.error) {
				console.log(data.error);
				x = data.error;
				$('#testbox').append('<p>' + x + '</p>');
			};
		});

		$('#username').val('');
		$('#password').val('');
		event.preventDefault();
	});


});