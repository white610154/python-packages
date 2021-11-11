import copy
from logging import Formatter, Handler, LogRecord
from typing import Any, Dict, List, Union

import pymysql
from pymysql.cursors import Cursor

from .Base import DBLogConfig

createSql = """
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `levelname` char(10) NOT NULL COMMENT '等級名稱',
  `levelno` int(2) unsigned NOT NULL COMMENT '等級代碼',
  `asctime` datetime NOT NULL COMMENT '紀錄時間',
  `pathname` text NOT NULL COMMENT '檔案名稱',
  `lineno` int(4) unsigned NOT NULL COMMENT '程式行數',
  `message` text NOT NULL COMMENT '訊息',
  `process` bigint(20) unsigned NOT NULL COMMENT '程序編號',
  `thread` bigint(20) unsigned NOT NULL COMMENT '執行續編號',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

insertSql = """
INSERT INTO `log` (
    `levelname`, `levelno`, `asctime`, `pathname`, `lineno`,
    `message`, `process`, `thread`)
VALUES (
    '{levelname}', {levelno}, '{asctime}', '{pathname}', {lineno},
    '{message}', {process}, {thread});
"""


class MariaLogger(Handler):
    def __init__(self, config: DBLogConfig):
        super().__init__()
        self.config: Dict[str, Union(str, int)] = {
            'user': config.user,
            'password': config.password,
            'host': config.host,
            'database': config.database,
            'port': config.port if config.port != None else 3306,
        }
        self.conn: pymysql.Connection = self.connect()

        self.setFormatter(Formatter(
            datefmt='%Y-%m-%d %H:%M:%S'
        ))

        self.setLevel(config.level)

    def connect(self):
        return pymysql.connect(
            **self.config,
            connect_timeout=86400,
            cursorclass=pymysql.cursors.DictCursor
            )

    def emit(self, record: LogRecord):
        self.check_connection()
        self.write_db(record)

    def format(self, record: LogRecord):
        recordTemp = copy.deepcopy(record)
        recordTemp.asctime = self.formatter.formatTime(record, self.formatter.datefmt)
        msgs: List[Any] = record.msg
        recordTemp.message = " ".join([str(m) for m in msgs])
        recordTemp.pathname = recordTemp.pathname.replace("\\", "/")
        return recordTemp

    def check_connection(self):
        try:
            self.conn.ping(reconnect=True)
        except Exception:
            self.conn = self.connect()

    def write_db(self, record: LogRecord):
        try:
            recordTemp = self.format(record)
            cursor: Cursor = self.conn.cursor()
            with cursor:
                cursor.execute(insertSql.format(**recordTemp.__dict__))
            self.conn.commit()
        except Exception:
            self.handleError(record)
