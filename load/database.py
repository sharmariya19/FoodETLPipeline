import psycopg2
from config import setting
from load import create_table


class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = "localhost" #setting.POSTGRES_SERVER
        self.username = "riya" #setting.POSTGRES_USER
        self.password = "postgres" #setting.POSTGRES_PASSWORD
        self.port = 5432  #setting.POSTGRES_PORT
        self.dbname = "food" #setting.POSTGRES_DATABASE
        self.conn = None
        self.cur = None

    def connect(self):
        """Connect to a Postgres database."""
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
                self.cur = self.conn.cursor()
                commands = create_table.create_tables()
                for command in commands:
                    try:
                        self.cur.execute(command)
                    except Exception as e:
                        pass
                else:
                    self.conn.commit()
                    self.cur.close()

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

    def insert_rows(self, query):
        self.cur = self.conn.cursor()
        self.cur.execute(query)
        self.conn.commit()
        self.cur.close()

db_obj = Database()
db_obj.connect()