$(document).ready(function(){
  var options = {
  	    target: "#output",
    beforeSubmit: beforeRequest,
    success: forResponse,
    timeout: 3000,
    error: forError
  };
  
  $('#myForm').submit(function() { 
    $(this).ajaxSubmit(options);
    return false;
  }); 
});

function beforeRequest(formData, jqForm, options) {
	    $('#error').css('display', 'none');
	    $('#output').css('display', 'none');
	    $('#loading').css('display', '');
	    disableForm(true);
    return true; 
} 

function forResponse(responseText, statusText)  { 
	$('#loading').css('display', 'none');
	$('#output').css('display', '');
	disableForm(false);
}

function forError(XMLHttpRequest, textStatus, errorThrown) {
	$('#loading').css('display', 'none');
	disableForm(false);
	var el = '<div id ="error" class="error">Some errors ' +
								'while submitting form!</div>'
	$('#loading').after(el);	
}

function disableForm(turn) {
	$('#id_name').attr('disabled', turn);
	$('#id_surname').attr('disabled', turn);
	$('#id_contacts').attr('disabled', turn);
	$('#id_bio').attr('disabled', turn);
	$('#id_birth_date').attr('disabled', turn);
	$('#id_button').attr('disabled', turn);
}