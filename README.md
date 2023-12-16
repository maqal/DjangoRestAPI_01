## '# Django Rest API'

    A complete CRUD restful API build for Django
    using generic class-based view

## Packages and commands

## 1. create python virtual environment
        py -m venv virtualEnvName

## 2. activate virtual env
        virtualEnvName\Scripts\activate.bat

## 3. Install Django (inside virtual environment)
        py -m pip install Django
        OR
	    pip install django
## 4. Check django version
	    django-admin --version

## 5. Create Django project (inside virtualEnvName)
	    django-admin startproject projectName
        # create new app
	    py manage.py startapp appname

## 6. Run the project
	    py manage.py runserver

## 7. Install rest-framework
    	pip install djangorestframework

## 8. Install cors-header
    	pip install django-cors-headers

## 9. Database drivers
    	# postgress
	    pip install pyscopg2

	    #solve improperly configured
	    pip install psycopg2-binary --force-reinstall --no-cache-dir

## 10. revert migration
		py manage.py app_name xxxx_migration_before_that+you_want_to_apply

		## revert all existing migrations
		py manage.py migrate app_name -- zero





