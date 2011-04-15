$('#AppConfiglet').live('click', function(e){
	e.preventDefault();
	$('#tabs').find('a').each(function(){
		$(this).removeClass('activeTab');
	});
	$(this).addClass('activeTab');
	$('#tabResultContainer').load($(this).attr('href') + ' #tabContent',function(){	
		// Add class slidecontainer to first ul find
		$('#settingTabs').find('ul:first').addClass('slidecontainer');
		// Add class tab to slides 
		$('#settingTabs').find('a').each(function(){
			$(this).addClass('tab');
		});
		$('#settingTabs').append('<div id="settingTabResultContainer"></div>');
		$('#settingTabs').find('a:first').click();
	});
});

$('#AppSettings').live('click', function(e){
	e.preventDefault();
	$('#tabs').find('a').each(function(){
		$(this).removeClass('activeTab');
	});
	$(this).addClass('activeTab');
	$('#settingTabResultContainer').load($(this).attr('href') + ' form');
});

// XXX - should be moved to mfa_core_action
$('#ActionSettings').live('click', function(e){
	e.preventDefault();
	$('#tabs').find('a').each(function(){
		$(this).removeClass('activeTab');
	});
	$(this).addClass('activeTab');
	// XXX - will be not a form later
	$('#settingTabResultContainer').load($(this).attr('href') + ' form');
});

// XXX - should be moved to mfa_core_filter
$('#FilterSettings').live('click', function(e){
	e.preventDefault();
	$('#tabs').find('a').each(function(){
		$(this).removeClass('activeTab');
	});
	$(this).addClass('activeTab');
	// XXX - will be not a form later
	$('#settingTabResultContainer').load($(this).attr('href') + ' form');
});
