import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
import os
from sawaal import Sawaal

# Generating Path to .env file and loading from path
path_to_env = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=path_to_env)

def run_query(query): 
    try:
    
        connection = psycopg2.connect(user=os.getenv("DBUSER"),
                                  password=os.getenv("DBPASSWORD"),
                                  host=os.getenv("DBHOST"),
                                  port=os.getenv("DBPORT"),
                                  database=os.getenv("DBNAME"))
        
        print("Successfully connected to Postgresql Database...")
        # Creating cursor to interact with databse.
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        # print("Result: ", result)
        print("Query Ran Successfully")
        return result

    except (Exception, Error) as e:
        print(f"Something went wrong!\nError: {e}") 
        
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Database connection closed.")

def get_random_sawaal():
    result = run_query("select * from prashn order by random() limit 1;")
    sawaal_object = Sawaal(id=result[0][0], text=result[0][1], image_url=result[0][2], answer=result[0][3], votes=result[0][4], choices=result[0][5], created_at=result[0][6])
    print("Retrieved Sawaal Successfully")
    return sawaal_object

