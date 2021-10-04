from packages.Logger import *

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
        user="root",
        password="12345678",
        host="127.0.0.1",
        database="testdb",
        )
    )
