from repository.seed_repository import init_database, init_tables_data
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    init_database()
    # init_tables_data()