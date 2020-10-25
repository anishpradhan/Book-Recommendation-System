# Installation Guide
## 1. Install Python 3.x

The BRS project requires that you have Python 3.x installed. 

## 2. Create a virtual environment for the project

Before you run the code, create a virtual environment.
Use this command to verify it’s installed:

`> virtualenv --version`

Once you have confirmed you have virtualenv installed, create the virtual environment using the following commands:

```bash
> python -m venv BRS
> cd BRS
> Scripts\activate
```

## 3. Download source code

You have two choices for downloading the source code – downloading a zip file of the source code or using Git.

* *Downloading a zip file*

    From the main [BRS directory on GitHub](https://github.com/anishpradhan/BRS.git) click the green “Clone or download” button and choose to download a zip file to your computer.

* *Using Git*

    Clone this repository or create a fork in your GitHub, and then clone that instead. Clone this inside the Virtual Environment Directory created earlier. The following command will create a copy on your computer. 
    
```bash
> git clone https://github.com/anishpradhan/BRS.git
```

### Get the required packages

Use pip to install the required files:

`> pip install -r requirements.txt`

## 4. Database setup

Django is setup to run with Sqllite3 out of the box, which is enough to run everything. However, some 
things will be considerably faster if you install MySQL.

*   If you do want to install MySQL, follow the MySQL installation steps before you create the databases.
*   If you don’t want to install MySQL, jump to Create and populate the BRS databases section.

    Assuming that you have XAMPP server installed, we can use its MySQL for our database, but we need mysql client to connect that db to our django project.
    So, at first start the MySQL server from your XAMPP.

### Install the mysql client driver i.e. Python database driver.

Once the MySQL database is spinning, it’s time for the Python driver, which enables Django to talk with the database. 
Download it from here -> https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient. 
Download the correct mysql client version for your operating system and redownload another version if that doesnot work.  
Once the mysql client is downloaded go to that folder, open cmd and type this command to install mysql client.

`> pip install (mysql client version whichever you downloaded)`
  
For eg. 
  
`> pip install mysqlclient-1.3.13-cp37-cp37m-win_amd64.whl`

For further instrustions you can follow this youtube video guide. https://www.youtube.com/watch?v=6SnE0r7g2lE

### Create the database for BRS

Use MySQL’s admin tool phpmyadmin to create a database. Name it brs. Write down which username and password you used to create the database. 
Or you can simply leave it as default username as 'root' and no password. You will use that information in two steps from now when you change the Django settings.

### Configure the Django database connection to connect to MySQL.
	
If you use a MySQL (or another db) you need to configure the Django database connection for BRS, follow these steps.

Open `BRS/settings.py`
	
Update the following:

```bash
DATABASES = {
   	    'default': {
        	'ENGINE': 'django.db.backends.mysql',
        	'NAME': brs',                      
        	'USER': 'root',
        	'PASSWORD': '',
        	'HOST': 'localhost',
        	'PORT': '3306',  (this is your mysql port number, you can find it from xampp control panel just beside MySQL)
   	    	       }	
		   }
```
If its already done in project then you can skip the above part

But if you have different username and password for you db,

Update the USER, PASSWORD, HOST, and PORT fields:

* USER(root): Use the user name you created with the BRS database
* PASSWORD(): Use the password you created with the BRS database
* HOST (localhost): localhost (if you have have installed it on your private machine)
* PORT (db_port_number): 3306 (this is your mysql port number, you can find it from xampp control panel just beside MySQL)


## Create and populate the BRS databases

Everyone must follow these steps, whether or not you are using MySQL.

### Run this script to create a necessary correlation file for your ML algorithm

`> python create_correlation.py`

WARNING: This might take a few seconds or even a minute.

### Create the BRS databases.
		
When the database connection is configured, you can run the following commands to create the databases that Django and this project need to run.

```bash
	> python manage.py makemigrations
	> python manage.py migrate (if this command doesnot work then use this > python3 manage.py migrate --run-syncdb)
```

### Populate the database.
	
Run the script by using these command to populate the databases with all the books and its information.
	
`> python populate_db.py`

## Create Superuser for your project.

To create superuser for the project use this command.

`> python manage.py createsuperuser`

Enter all the required fields and create the superuser

## Start the web server

To start the development server, run this command:\

`> python manage.py runserver `

## Closing down

When you are finished running the project you can close it down doing the following steps, or simply close the terminal where the server is running.

* Close down the server by pressing 'c'
* Exit the virtual environment:

`> deactivate`
