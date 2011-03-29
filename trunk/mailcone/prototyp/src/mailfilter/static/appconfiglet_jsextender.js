$('#AppConfiglet').live('click', function(e){
	e.preventDefault();
	$('#tabs').find('a').each(function(){
		$(this).removeClass('activeTab');
	});
	$(this).addClass('activeTab');
	$('#tabResultContainer').load($(this).attr('href') + ' form');
});

$("input[name='form.actions.saveAppSettings']").live('click', function(e){
	e.preventDefault();
	
	var container = $(this).parents('#tabResultContainer:first');
	var form = $(container).find('form:first');
	
	var title = $("input[name=form.title]").val();
	var default_mail = $("input[name=form.default_mail]").val();
	
	var buttonId = $(form).find("input[type=submit]").val();
	var dataString = 'form.title='+ title + 
	 				 '&form.default_mail=' + default_mail +
	 				 '&form.actions.saveAppSettings=' + buttonId;
	
	$.ajax({  
		type: "POST",  
		url: $(form).attr('action'),  
		data: dataString,
		success: function(data){
			resultData = data;
			$(container).html($(resultData).find('form:first'));
		}
	});
});