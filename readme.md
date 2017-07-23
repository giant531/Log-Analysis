
# Log Analysis

# About
This is the project under Udacity NanoDegree. It includes a database that professes to be designed for newspaper website.
The database includes multiple table and millions of rows included through SQL query.
The data included in the database would be helpfull to draw different conclusions.

# Prerequisites

* Python
* VirtualBox
* Vagrant

# Installing
* Install VirtualBox and Vagrant.
* Clone this repository.

# To Run
 
* Launch Vagrant VM by running `vagrant up`,and after running you can the log in with `vagrant ssh`

* Load the data into database by using the command `psql -d news -f newsdata.sql` to connect to a database named *news* and run the necessary SQL statements.


* Create a view by running the following SQL statement `psql -d news` and then fire the below SQL statement:

'''
CREATE VIEW percent_error_view AS SELECT date(time),
round(100.00 * sum(CASE WHEN log.status = '404 NOT FOUND' THEN 1 ELSE 0 END)/ count(log.status), 2)
AS percenterror FROM log GROUP BY date(time) ORDER BY  PercentError DESC;
'''

To execute the program, run `python newsdata.py` from the command line.


