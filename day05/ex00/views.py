from django.shortcuts import render
import psycopg2
# Create your views here.

def ex00_view(request):
    conn = psycopg2.connect(dbname='mydb', user='postgres', password='mypassword', host='www.mydbserver.com', port='5432', sslmode='require')
    cur = conn.cursor()
    cur.execute('SELECT * FROM existing_schema.existing_table')
    one = cur.fetchone()
    print(one)
    return render (request, "ex00/init.html")