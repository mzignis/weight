import configparser

from sqlalchemy import create_engine


config = configparser.ConfigParser()
config.read('db/config.ini')
user = config['GENERAL']['USER-NAME']
password = config['GENERAL']['PASSWORD']
hostname = config['GENERAL']['HOST-NAME']
database = config['GENERAL']['DATABASE-NAME']

engine = create_engine(
    f'postgresql+psycopg2://{user}:{password}@{hostname}/{database}'
)

if __name__ == '__main__':
    pass
