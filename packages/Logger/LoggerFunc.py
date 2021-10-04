from typing import Union

from .ConsoleLogger import ConsoleLogConfig, ConsoleLogger
from .DBLogger import *
from .FileLogger import FileLogConfig, FileLogger


def console_logger(config: ConsoleLogConfig=None) -> ConsoleLogger:
    return ConsoleLogger(config)

def file_logger(config: FileLogConfig=None) -> FileLogger:
    return FileLogger(config)

def db_logger(config: DBLogConfig) -> MariaLogger:
    if config.dbType == DBType.Maria:
        return MariaLogger(config)
    return
