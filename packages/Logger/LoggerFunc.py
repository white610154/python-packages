from logging import CRITICAL

from packages.Logger.ConsoleLogger import ConsoleLogConfig, ConsoleLogger
from packages.Logger.DBLogger import DBLogConfig, DBLogger, DBType
from packages.Logger.FileLogger import FileLogConfig, FileLogger


def console_logger(config: ConsoleLogConfig=None):
    if config == None:
        print("WARNING: console log enable but console log config not set, console log will not work.")
        return ConsoleLogger(ConsoleLogConfig(level=CRITICAL))

    return ConsoleLogger(config)

def file_logger(config: FileLogConfig=None):
    if config == None:
        print("WARNING: file log enable but file log config not set, file log will not work.")
        return FileLogger(FileLogConfig(level=CRITICAL))

    return FileLogger(config)

def db_logger(config: FileLogConfig):
    if config == None:
        print("WARNING: DB log enable but DB log config not set, DB log will not work.")
        return DBLogger(DBLogConfig(dbType=DBType.Null, level=CRITICAL))

    DBLogger(config)