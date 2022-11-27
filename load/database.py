import psycopg2
from config import setting
from load import create_table


class Database:
    """PostgreSQL Database class."""

    def __init__(self):
        self.host = setting.POSTGRES_SERVER
        self.username = setting.POSTGRES_USER
        self.password = setting.POSTGRES_PASSWORD
        self.port = setting.POSTGRES_PORT
        self.dbname = setting.POSTGRES_DATABASE
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
                self.tables()
                self.conn.commit()
                self.cur.close()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)

        return self.conn

    def tables(self):

        commands = create_table.create_tables()
        while True:
            try:
                self.cur = self.conn.cursor()
                command = (next(commands))
                self.cur.execute(command)
                self.conn.commit()
                self.cur.close()
            except StopIteration:
                break
            except:
                pass

    def insert_rows(self, query):
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(query)
            self.conn.commit()
            self.cur.close()
        except:
            pass

