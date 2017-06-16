#Load the data in local database using the command only once i.e.initially:
#psql -d news -f newsdata.sql
#Use psql -d news to connect to database.
# Create view article_view using:
#   create view article_view as select title,author,count(*) as views from articles,log where
#   log.path like concat('%',articles.slug) group by articles.title,articles.author
#   order by views desc;
#Create vier error_log_view using:
#   create view error_log_view as select date(time),round(100.0*sum(case log.status when '200 OK'
#   then 0 else 1 end)/count(log.status),2) as "Percent Error" from log group by date(time)
#   order by "Percent Error" desc;




import psycopg2

Dbname = "news"

# 1. Top three populor articles of all the time!
q1 = "select title,views from article_view limit 3"

# 2. The author of top most article of all the time!
q2 = """select authors.name,sum(article_view.views) as views from
article_view,authors where authors.id = article_view.author
group by authors.name order by views desc"""

# 3. Days when the requests lead to an error more than 1%!
q3 = "select * from error_log_view where \"Percent Error\" > 1"

q1_output = dict()
q1_output['title'] = "\n1. The top three populor articles of all the time:\n"

q2_output = dict()
q2_output['title'] = """\n2. The author of top most article of all the time:\n"""

q3_output = dict()
q3_output['title'] = """\n3. Days when the requests lead to an error more than 1%:\n"""



def get_query_output(query):
    db = psycopg2.connect(database=Dbname)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def display_query_output(query_output):
    print (query_output['title'])
    for result in query_output['results']:
        print ('\t' + str(result[0]) + ' --- ' + str(result[1]) + ' views')


def display_error_query_output(query_output):
    print (query_output['title'])
    for result in query_output['results']:
        print ('\t' + str(result[0]) + ' --- ' + str(result[1]) + ' %')


q1_output['results'] = get_query_output(q1)
q2_output['results'] = get_query_output(q2)
q3_output['results'] = get_query_output(q3)

display_query_output(q1_output)
display_query_output(q2_output)
display_error_query_output(q3_output)
