from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.

def ex00_view(request):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname='dbtest',
            user='oaboulgh',
            password='admin',
            host='localhost',
            port='5432'
        )

        # Create a cursor object using the connection
        cursor = conn.cursor()

        # Example SQL command to create a table
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS ex00_movies (
                episode_nb serial PRIMARY KEY,
                title VARCHAR(64) UNIQUE NOT NULL,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            )
        '''

        # Execute the SQL command
        cursor.execute(create_table_query)

        # Commit the transaction
        conn.commit()

        # Close communication with the database
        cursor.close()
        conn.close()

        # Return a success response
        result = 'OK'
        return render(request, "ex00/init.html", {'result': result})

    except psycopg2.Error as e:
        # Return an error response if table creation fails
        error_msg = f'Error creating table: {e}'
        return HttpResponse(error_msg, status=500)