**LOG ANALYSIS**

**About**

This is the project of Udacity NanoDegree. This project includes large database professes to be designed for newspaper  site that includes 3 tables viz. **articles**, **authors** and **log** with millions of rows by SQL queries. This database contains the data of articles read, authors of the articles and web server log for the newspaper site.This data is used for conclusion for different results.

**Prerequisites**

* Python
* Vagrant
* VirtualBox

**Installing**

1. Install Vagrant and VirtualBox
2. Clone this repository.

**Downloading**

* Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file.


**Running the tests**

* Launch Vagrant VM by running `vagrant up`, you can the log in with `vagrant ssh`

* Load the data into databse named *news*, use the command `psql -d news -f newsdata.sql` only once.

* Connect to databse, run the command `psql -d news`.

* Create a *view* , use the command psql -d news and then run the SQL statement as mentioned below.

    * SQL query for creating view: CREATE VIEW percent_error_view:
```
CREATE VIEW percent_error_view AS SELECT date(time),
round(100.00*sum(CASE WHEN status = '404 NOT FOUND'
THEN 1 ELSE 0 END) / count(log.status),2)
AS PercentError FROM log GROUP BY date(time) ORDER BY PercentError DESC;
```

* To execute the program, run `python logAnalysis.py` from the command line.
