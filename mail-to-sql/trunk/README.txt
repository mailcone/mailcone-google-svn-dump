README
======

Installation
------------

1) Setup a postgres database. In folder sql you'll find a sql file you can import in you database called 'mails'
The name of the database as well as the name of the table are free. Just note, that you have to modify the config.py file

2) configuration
2.1) config your mail-to-sql - for that modify the config.py - this is for all mails
Overview:

* CONFIG
	
	* saveBrokenDataPath - define a path where mail-to-sql can store pipeData when script break

* CONFIG_MAIL
	
	* dbMailtableName - define the name of your database table, where mails stored
	
	* mail_id_seq_name - define the sequence name for the primary key

* CONFIG_PARSEUTIL

	* define some pattern for parse pipeData, if other results are wished or expected, 
	  you can modify them.
	  
	* timezone - define the timezone you wish to store mail date time (for example 'Europe/Amsterdam')

2.2) copy default.cfg an configure the following settings:

* CONFIG_DBUTIL

	* dbDriver - name of the python driver for database (only tested with postgresql)
	
	* dbHostname - define the hostname (tested only with localhost)
	
	* dbPort - define port on which the sql server run
	
	* dbUser - database user
	
	* dbPw - database password
	
	* dbName - define the name of the sql database 

* CONFIG_ATTUTIL
	
	* attachmentRootPath - define root for attachment storage
	
* CONFIG_LOG

	* debugmode - de-/actived debugmode	
	
	* infolog_separate / errorlog_separate - you can say if there should be one logfile for each mail
	
	* error_separatedLogs - if you wish errorlogs separated, you can force to delete empty error logs

3) test your configuration and the script:
# python2.6 test_mail_to_sql.py

	Result should be:
	....
	----------------------------------------------------------------------
	Ran 4 tests in 0.279s

	OK


4) call the script:

	pipeData | python2.6 mail_to_sql.py --config=myConfig.cfg

or if it as file
	
	python2.6 mail_to_sql.py --config=myConfig.cfg --file=filename	 

Dependencies
------------

* python2.6 and higher

* chardet

* python-dateutil

* pytz

* sqlalchemy

* psycopg2
