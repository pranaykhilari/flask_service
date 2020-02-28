# Setup application
* Create python3 virtual environment
   * ```python3 -m venv /path/to/new/virtual/environment```

* Activate environment
    * ```source new_environment_name/bin/activate```

* Install requirements from requirements.txt file
    * ```pip install -r requirements.txt```
    
# Migration commands

   * ```python manage.py db init```
   * ```python manage.py db migrate```
   * ```python manage.py db upgrade```

# Delete alembic_folder

* Connect to postgresql DB

    * sudo –i –u postgres psql
* List the Databases
    * \list or \l: list all databases

* To switch Database
    * \connect database_name or \c database_name
    
* List tables in selected database
    * \dt
    
* Drop table
    * DROP table **table_name**
    