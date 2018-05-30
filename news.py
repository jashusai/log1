#!/usr/bin/env python

import psycopg2

# Here the class name defined News


class News:
    def __init__(s):
        try:
            s.db = psycopg2.connect('dbname=news')
            s.cursor = s.db.cursor()
        except Exception as e:
            print e

    def implement_query(s, sqlquery):
        s.cursor.execute(sqlquery)
        return s.cursor.fetchall()

    def solution(s, q, sqlquery, top='views'):
        answer = s.implement_query(sqlquery)
        print q
        for j in range(len(answer)):
            print '.', answer[j][0], '->', answer[j][1], top

    def exit(s):
        s.db.close()

# Query of popular articles
q_1_title = ('Most popular three articles of all time')
sqlquery_1 = """
        select articles.title, count(*) as num
        from articles
        join log
        on log.path like concat('/article/%', articles.slug)
        group by articles.title
        order by num desc
        limit 3;
"""
# Query of popular authors
q_2_title = ('Most popular authors of all time')
sqlquery_2 = """
        select authors.name, count(*) as num
        from authors
        join articles
        on authors.id = articles.author
        join log
        on log.path like concat('/article/%', articles.slug)
        group by authors.name
        order by num desc
        limit 3;
"""
# Query of more than 1% of requests lead to errors
q_3_title = ('On which days did more than 1% of requests lead to errors?')
sqlquery_3 = """
select * from (
    select a.day,
    round(cast((100*b.hits) as numeric) / cast(a.hits as numeric), 2)
    as errp from
        (select date(time) as day, count(*) as hits from log group by day) as a
        inner join
        (select date(time) as day, count(*) as hits from log where status
        like '%404%' group by day) as b
    on a.day = b.day)
as t where errp > 1.0;
"""


# Store query results
if __name__ == '__main__':
    obj = News()
    obj.solution(q_1_title, sqlquery_1)
    obj.solution(q_2_title, sqlquery_2)
    obj.solution(q_3_title, sqlquery_3, '% error')
    obj.exit()
