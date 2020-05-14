$(document).ready(function () {
    $("INPUT#btn_translate").on("click", function (event) {
	const x = $("INPUT#language_code").val();
	$.ajax({
	    type: 'GET',
	    url: 'https://fourtonfish.com/hellosalut/?lang='+ x ,
	    success: function(data) {
		$('DIV#hello').text(data.hello);
	    }
	});
    });
});
