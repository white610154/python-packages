from packages.Logger import (ConsoleLogConfig, FileLogConfig, Logger, LogLevel,
                             LogType)
from packages.Logger.DBLogger import DBLogConfig, DBType
from packages.Logger.DBLogger.MariaHandler import MariaDBConfig

Logger.config(
    logTypes=LogType.Console | LogType.File | LogType.DB,
    consoleLogConfig=ConsoleLogConfig(
        level=LogLevel.WARNING,
        ),
    fileLogConfig=FileLogConfig(
        level=LogLevel.INFO,
        newline=False,
        dirname="logs",
        suffix='',
        ),
    dbLogConfig=DBLogConfig(
        dbType=DBType.Maria,
        level=LogLevel.INFO,
        dbConfig=MariaDBConfig(
            host="127.0.0.1",
            user="root",
            password="12345678",
            database="testdb",
            )
        )
    )
