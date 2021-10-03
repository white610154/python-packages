from packages.Logger import (ConsoleLogConfig, FileLogConfig, Logger, LogLevel,
                             LogType)

Logger.config(
    logTypes=LogType.Console | LogType.File,
    consoleLogConfig=ConsoleLogConfig(
        level=LogLevel.WARNING,
        ),
    fileLogConfig=FileLogConfig(
        level=LogLevel.INFO,
        newline=False,
        dirname="logs",
        suffix='',
        ),
    )
