import logging
from typing import Any

from packages.Logger import LoggerFunc
from packages.Logger.ConsoleLogger import ConsoleLogConfig
from packages.Logger.DBLogger import DBLogConfig
from packages.Logger.FileLogger import FileLogConfig


class LogLevel:
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR

class LogType:
    Console: int = 0b0001
    File: int = 0b0010
    DB: int = 0b0100

class Logger:
    __logger: logging.Logger = logging.Logger(__name__)

    @classmethod
    def config(
        cls,
        logTypes: int=0,
        consoleLogConfig: ConsoleLogConfig = None,
        fileLogConfig: FileLogConfig = None,
        dbLogConfig: DBLogConfig = None,
        ):
        '''
        Basic settings of logger

        Args:
            logTypes (int): set log types, ex: LogType.Console | LogType.File | LogType.DB
            consoleLogConfig (ConsoleLogConfig): config of console log
            fileLogConfig (FileLogConfig): config of file log, create new file every day
            dbLogConfig (DBLogConfig): config of DB log, DB support: mariadb(mysql), postgres, mongodb, mssql, sqlite3
        '''
        if logTypes & LogType.Console:
            consoleLogger = LoggerFunc.console_logger(consoleLogConfig)
            cls.__logger.addHandler(consoleLogger)

        if logTypes & LogType.File:
            fileLogger = LoggerFunc.file_logger(fileLogConfig)
            cls.__logger.addHandler(fileLogger)

        if logTypes & LogType.DB:
            dbLogger = LoggerFunc.db_logger(logTypes & LogType.DB, dbLogConfig)
            cls.__logger.addHandler(dbLogger)


    @classmethod
    def log(cls, level: int, *msgs: Any):
        cls.__logger.log(level, msgs, stacklevel=3)

    @classmethod
    def debug(cls, *msgs: Any):
        cls.log(LogLevel.DEBUG, *msgs)

    @classmethod
    def info(cls, *msgs: Any):
        cls.log(LogLevel.INFO, *msgs)

    @classmethod
    def warning(cls, *msgs: Any):
        cls.log(LogLevel.WARNING, *msgs)

    @classmethod
    def error(cls, *msgs: Any):
        cls.log(LogLevel.ERROR, *msgs)
