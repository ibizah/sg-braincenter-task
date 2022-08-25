# sg-braincenter-task

Django app - Requirements:
=========================
1. Create the following models:
	a). Series_type:
			- id => Primary key, Auto increment
			- Name => Varchar with max_length = 30
			- Mnemonic => Varchar with max_length = 4
	b). Series:
			- id => Primary key, Auto increment
			- Name => Varchar with max_length = 255
			- Series_type => Foreign key refererring from Series_type.id
	b). Series_set:
			- id => Primary key, Auto increment
			- Name => Varchar with max_length = 255
			- Series => Forign key refererring from Series.id
			
2. All the models should have a Seriealizer and ViewSet based functiionalities
	SOLUTION PATH:
	braincenter\views.py | line 68

3. REST call for Create or Update functionality to "Series" table:
	a). POST method, with parameters of (Name, Series_type) 
	 i). If the posted record is not found on the exisiting records, insert the record
	 ii). If the posted record not on the database, create a new record

4. Write a REST call for get the following details:
	a). Series.id, Series.Name, Series_type.Name, Series_type.Mnemonic
	
	SOLUTION PATH:
	braincenter\views.py | line 68

5. Write a REST call for get the following details:
	a). Count of unique Series_type from Series table, and list of series names for each Series_set
	b). parameters: Series_set.id
	c). example output:
				[
					{
						"serieses_count": 2,
						"serieses": [ "NISL", "HEOS"]
					},
					{
						"serieses_count": 4,
						"serieses": [ "NISL", "HEOS", "IHC", "BFI"]
					},
				]
