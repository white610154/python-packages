from dataclasses import dataclass
from logging import WARNING


class DBType:
    Null = "null"
    Maria = "mysql"
    Postgres = "postgres"
    Mongo = "mongo"
    SQLServer = "mssql"

@dataclass
class DBLogConfig:
    dbType: str
    user: str
    password: str
    host: str
    database: str
    port: int = None
    level: int = WARNING
