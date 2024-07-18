from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db import connection, IntegrityError
import psycopg2
import os
# Create your views here.

def display(request):
    data = []
    data_planet = []

    try:
        # Connect to the database
        query = """
        SELECT name, homeworld FROM ex08_people;
        """
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()


        query = "SELECT climate FROM ex08_planets WHERE name = %s;"
        
        result = []
        for row in data:
            with connection.cursor() as cursor:
                cursor.execute(query, (row[1], ))
                data_planet = cursor.fetchone()
            if data_planet is not None:
                climate = data_planet[0]
            else:
                climate = "Unknown"
            new_entry = {'name':row[0], 'homeworld': row[1], 'climate': climate}
            result.append(new_entry)

        return render(request, 'ex08/display.html', {'data': result})
    except Exception as e:
        print(f"Error: {e}")
        return render(request, 'ex08/display.html', {'data': result})



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
        # Insert planets
        file_relative_path = "ex08/planets.csv"
        file_path = os.path.join(settings.BASE_DIR, file_relative_path)
        insert_query = """
            INSERT INTO ex08_planets (name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING;
        """
        def convert_to_none(value):
            if value == 'NULL' or value == '':
                return None
            return value
        with open(file_path, 'r') as file:
            for line in file:
                pairs = line.strip().split("\t")  # strip to remove whitespace
                values = tuple(convert_to_none(pairs[i]) for i in range(8))
                cursor.execute(insert_query, values)
                state.append('OK')

        # Commit planet inserts
        conn.commit()

        # Insert people
        file_relative_path = "ex08/people.csv"
        file_path = os.path.join(settings.BASE_DIR, file_relative_path)
        insert_query = """
            INSERT INTO ex08_people (name, birth_year, gender, eye_color, hair_color, height, mass, homeworld)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (name) DO NOTHING;
        """
        with open(file_path, 'r') as filo:
            for line in filo:
                pairs = line.strip().split("\t")  # strip to remove whitespace
                values = tuple(convert_to_none(pairs[i]) for i in range(8))
                cursor.execute(insert_query, values)
                state.append('OK')

        conn.commit()
        cursor.close()
        conn.close()
        return render(request, 'populate.html', {'state': state})
        
    except FileNotFoundError:
        state.append("(planets.csv || people.csv) | can't open.")
        conn.rollback()
        return render(request, 'populate.html', {'state': state})
        
    except psycopg2.Error as error:
        conn.rollback()
        error_msg = f'Error inserting: {error}'
        return HttpResponse(error_msg)
        
    except Exception as e:
        conn.rollback()
        state.append(f'{e}')
        return render(request, 'populate.html', {'state': state})


def init(request):
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
        create_tables_query = '''
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR(255),
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64),
                CONSTRAINT fk_homeworld
                    FOREIGN KEY (homeworld)
                    REFERENCES "ex08_planets" (name)
            );
        '''

        # Execute the SQL command
        cursor.execute(create_tables_query)

        # Commit the transaction
        conn.commit()

        # Close communication with the database
        cursor.close()
        conn.close()

        # Return a success response
        result = []
        result.append("OK")
        return render(request, "ex08/init.html", {'result': result})

    except psycopg2.Error as e:
        # Return an error response if table creation fails
        error_msg = f'Error creating table: {e}'
        return HttpResponse(error_msg, status=500)