import psycopg2

from src.services.aws.secrets import get_secret
from src.services.logs.logger import Logger
from src.services.read_params.yaml_util import read_yaml


def read_db_params(schema, server, param):
    return read_yaml(f"src/shared_utils/db/db_info/{schema}.yaml")[server][param]


class DataBase(object):
    def __init__(self, schema, server):
        self.schema = schema
        # Initializing the needed variables for different schemas
        self.db_id = read_db_params(schema, server, 'id')
        self.db_host = read_db_params(schema, server, 'host')
        self.db_port = str(read_db_params(schema, server, 'port'))
        self.db_username = read_db_params(schema, server, 'username')

        # get password from aws
        if server == "localhost" and schema == "template":
            self.db_password = get_secret("local")
        elif server == "test" and schema == "template":
            self.db_password = get_secret("test")

        self.conn = self.start_connection()
        self.cursor = self.conn.cursor()

    def start_connection(self):
        """
      Starting the connection to database to corresponding schema
      :return:
      """
        conn = psycopg2.connect(
            database=self.db_id,
            user=self.db_username,
            password=self.db_password,
            host=self.db_host,
            port=self.db_port,
            connect_timeout=20
        )

        Logger(f"[DB_{self.schema}] Connected!").substep_passed()
        return conn

    def execute_query(self, query):
        """Executes the query to proper db

      :param query:
      :return:
      """
        self.cursor.execute(query)
        # Fetching 1st row from the table
        return self.cursor.fetchall()

    def kill_connection(self):
        """Kills the connection with database

      :return:
      """
        self.conn.close()
