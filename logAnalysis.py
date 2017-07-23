#! /usr/bin/env python2

import psycopg2
dbname = "news"

# 1. Top three populor articles of all the time!
query1 = """SELECT articles.title, count(*) AS views FROM articles,
log WHERE SUBSTRING(log.path,10) = articles.slug AND
log.status LIKE '%200%' GROUP BY articles.title ORDER
BY views DESC LIMIT 3"""

# 2. The most popular article authors are!
query2 = """SELECT authors.name,count(*) AS total_views FROM articles,
authors,log WHERE authors.id = articles.author AND SUBSTRING
(log.path,10) = articles.slug AND log.status LIKE '%200%'
GROUP BY authors.name ORDER BY  total_views DESC"""

# 3. Days when the requests lead to an error more than 1%!
query3 = "SELECT * FROM percent_error_view  WHERE PercentError >= 1"

output1 = {}
output2 = {}
output3 = {}

output1['subject'] = "The most popular three articles of all time are:\n"

output2['subject'] = "The most popular article authors of all time are:\n"

output3['subject'] = "The days on which more than 1% of requests lead to"
"errors are:\n"


def fire_query(query):
    db = psycopg2.connect(database=dbname)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def display_resulted_query(output):
    print(output['subject'])
    for x in output['result']:
        print (str(x[0]) + '\t' + str(x[1]) + ' views')
    print('\n')


def display_error(output):
    print (output3['subject'])
    for x in output3['result']:
        print (str(x[0]) + '\t' + str(x[1]) + ' %' + '\n')
    print('\n')

output1['result'] = fire_query(query1)
output2['result'] = fire_query(query2)
output3['result'] = fire_query(query3)

display_resulted_query(output1)
display_resulted_query(output2)
display_error(output3)
