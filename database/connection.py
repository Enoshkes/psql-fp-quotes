import psycopg2
from psycopg2.extras import RealDictCursor

from database.config import SQL_URI


def get_db_connection():
    return psycopg2.connect(SQL_URI, cursor_factory=RealDictCursor)