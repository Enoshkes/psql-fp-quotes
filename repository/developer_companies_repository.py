import logging

from database.connection import get_db_connection

def create_developer_companies(*developer_companies):
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            for dc in developer_companies:
                cursor.execute("""
                    insert into developer_companies (developer_id, company_id) 
                    values (%s, %s)""",
                (dc["developer_id"], dc["company_id"]))

            connection.commit()
            message = f"{len(developer_companies)} developer companies has created"
            logging.info(message)
    except Exception as e:
        logging.error(e)


