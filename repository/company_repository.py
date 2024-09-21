import logging

from database.connection import get_db_connection

def create_companies(*companies):
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            for company in companies:
                cursor.execute("""
                    insert into company (name, product) values (%s, %s)""",
                (company["name"], company["product"]))

            connection.commit()
            message = f"{len(companies)} companies has created"
            logging.info(message)
    except Exception as e:
        logging.error(e)


