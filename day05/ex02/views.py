from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.db import connection
import psycopg2
import os

# Create your views here.

def display(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT episode_nb, title, opening_crawl, director, producer, release_date FROM ex02_movies")
        data = cursor.fetchall()
    # Format data into a list of dictionaries for easier template rendering
    data = [{'episode_nb': row[0], 'title': row[1], 'opening_crawl': row[2], 'director':row[3], 'producer':row[4], 'release_date':row[5]} for row in data]

    return render(request, 'display.html', {'data': data})

def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT'],
        )

        # Create a cursor object using the connection
        cursor = conn.cursor()

        # Example SQL command to create a table
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS ex02_movies (
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
        return render(request, "init.html", {'result': result})

    except psycopg2.Error as e:
        # Return an error response if table creation fails
        error_msg = f'Error creating table: {e}'
        return HttpResponse(error_msg, status=500)

def populate(request):
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT'],
    )
    cursor = conn.cursor()

    state = []
    try:
        file_relative_path = "ex02/movies_data.txt"
        file_path = os.path.join(settings.BASE_DIR, file_relative_path)
        movie_dict = {}
        insert_query = """
            INSERT INTO ex02_movies (episode_nb, title, director, producer, release_date)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
        """
        with open (file_path, 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                pairs = line.split(" - ")
                for pair in pairs:
                    key_value = pair.strip().split(':')
                    if len(key_value) == 2:
                        key = key_value[0].strip()
                        value = key_value[1].strip()
                        movie_dict[key] = value
                # print(movie_dict)
                cursor.execute(insert_query, (
                    movie_dict['episode_nb'],
                    movie_dict['title'],
                    movie_dict['director'],
                    movie_dict['producer'],
                    movie_dict['release_date']
                ))
                movie_dict.clear()
                state.append('OK')

        print(state)
        conn.commit()
        cursor.close()
        conn.close()
        return render (request, 'populate.html', {'state': state})
    except psycopg2.Error as error:
        conn.rollback()
        error_msg = f'Error inserting: {error}'
        return HttpResponse(error_msg)