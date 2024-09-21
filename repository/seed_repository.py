from database.connection import get_db_connection
import logging

from database.data import developers, companies, quotes, developers_companies
from repository.company_repository import create_companies
from repository.developer_companies_repository import create_developer_companies
from repository.developer_repository import create_developers
from repository.quotes_repository import create_quotes


def _creation_message(table_name: str) -> str:
    return f"{table_name} created, or already exists"

def create_company_table():
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists company (
                    id bigint primary key generated always as identity,
                    name varchar(200) not null,
                    product varchar(200) not null
                )""")
            logging.info(_creation_message("Company"))
    except Exception as e:
        logging.error(e)


def create_developer_table():
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists developer (
                    id bigint primary key generated always as identity,
                    fullname varchar(200) not null,
                    language varchar(100) not null,
                    active_years varchar(100) not null
                )""")
            logging.info(_creation_message("Developer"))
    except Exception as e:
        logging.error(e)


def create_quote_table():
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists quote (
                    id bigint primary key generated always as identity,
                    quote text not null,
                    developer_id bigint,
                    foreign key (developer_id) references developer(id)
                    on delete set null
                )""")
            logging.info(_creation_message("Quote"))
    except Exception as e:
        logging.error(e)


def create_developer_companies_table():
    try:
        with get_db_connection() as connection, connection.cursor() as cursor:
            cursor.execute("""
                create table if not exists developer_companies (
                    developer_id bigint not null,
                    company_id bigint not null,
                    primary key (developer_id, company_id),
                    foreign key (developer_id) references developer(id)
                    on delete cascade,
                    foreign key (company_id) references company(id)
                    on delete cascade
                )""")
            logging.info(_creation_message("Developer Companies"))
    except Exception as e:
        logging.error(e)

def init_database():
    try:
        for create_function in [
            create_company_table,
            create_developer_table,
            create_quote_table,
            create_developer_companies_table
        ]:
            with get_db_connection() as connection:
                create_function()
                connection.commit()

        logging.info("All tables created successfully")
    except Exception as e:
        logging.error(e)

def init_tables_data():
    create_developers(*developers)
    create_companies(*companies)
    create_quotes(*quotes)
    create_developer_companies(*developers_companies)