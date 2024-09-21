import logging

from database.connection import get_db_connection


def create_developers(*developers):
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            for developer in developers:
                cursor.execute("""
                    insert into developer (fullname, language, active_years) 
                    values (%s, %s, %s)""",
                (developer["fullname"], developer["language"], developer["active_years"]))

            connection.commit()
            message = f"{len(developers)} developers has created"
            logging.info(message)
    except Exception as e:
        logging.error(e)


