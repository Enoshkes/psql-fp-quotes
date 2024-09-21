import logging

from toolz import count

from database.connection import get_db_connection


def create_quotes(*quotes):
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            for quote in quotes:
                cursor.execute("""
                    insert into quote (quote, developer_id) values (%s, %s)
                """, (quote["quote"], quote["developer_id"]))

            connection.commit()
            message = f"{len(quotes)} quotes has created"
            logging.info(message)
    except Exception as e:
        logging.error(e)


