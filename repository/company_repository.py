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


def find_company_by_id(cid: int):
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute("""
            select * from company where id = %s
            """, (cid, ))
            logging.info(f"Retrieving company by the id: {cid}")
            return cursor.fetchone()
    except Exception as e:
        logging.error(e)

