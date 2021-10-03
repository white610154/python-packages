from dataclasses import dataclass
from logging import WARNING, Handler

from packages.Logger.DBLogger.MariaHandler import MariaDBConfig


class DBType:
    Null = "null"
    Maria = "mysql"
    Postgres = "postgres"
    Mongo = "mongo"
    SQLServer = "mssql"

@dataclass
class DBLogConfig:
    dbType: str
    level: int = WARNING
    dbConfig: MariaDBConfig = None

class DBLogger(Handler):
    def __init__(self, config: DBLogConfig):
        super().__init__()

        self.setLevel(config.level)
