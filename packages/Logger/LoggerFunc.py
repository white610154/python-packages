from logging import CRITICAL

from packages.Logger.ConsoleLogger import ConsoleLogConfig, ConsoleLogger
from packages.Logger.FileLogger import FileLogConfig, FileLogger


def console_logger(
    enable: bool=False,
    config: ConsoleLogConfig=None,
    ):
    if not enable:
        return ConsoleLogger(ConsoleLogConfig(level=CRITICAL))
    elif config == None:
        print("WARNING: console log enable but console log config not set, console log will not work.")
        return ConsoleLogger(ConsoleLogConfig(level=CRITICAL))

    return ConsoleLogger(config)

def file_logger(
    enable: bool=False,
    config: FileLogConfig=None,
    ):
    if not enable:
        return FileLogger(FileLogConfig(level=CRITICAL))
    elif config == None:
        print("WARNING: file log enable but file log config not set, file log will not work.")
        return FileLogger(FileLogConfig(level=CRITICAL))

    return FileLogger(config)
