$(document).ready(function() {

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
	
});