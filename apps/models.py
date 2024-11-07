import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    try:
        # Replace with your actual DATABASE_URL from environment variables or configuration
        url = os.getenv("DATABASE_URL")
        connection = psycopg2.connect(url)
        print("\nConnected to database!")
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

