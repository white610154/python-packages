import copy
from dataclasses import dataclass
from logging import Handler, LogRecord
from typing import Any, Dict, List, Union

import pymysql
import pymysql.cursors

createSql = """
DROP TABLE IF EXISTS `log`;
CREATE TABLE `log` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `levelname` char(1) NOT NULL COMMENT '等級名稱',
  `levelno` int(2) unsigned NOT NULL COMMENT '等級代碼',
  `log_time` datetime NOT NULL COMMENT '紀錄時間',
  `filename` text NOT NULL COMMENT '檔案名稱',
  `lineno` int(4) unsigned NOT NULL COMMENT '程式行數',
  `message` text NOT NULL COMMENT '訊息',
  `process_id` int(5) unsigned NOT NULL COMMENT '程序編號',
  `thread_id` int(5) unsigned NOT NULL COMMENT '執行續編號',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""

inserSql = """
INSERT INTO `log` (
    `levelname`, `levelno`, `log_time`, `filename`, `lineno`,
    `message`, `process_id`, `thread_id`)
VALUES (
    '{levelname}', {levelno}, '{log_time}', '{filename}', {lineno},
    '{message}', {process_id}, {thread_id});
"""

@dataclass
class MariaDBConfig:
    host: str
    user: str
    password: str
    database: str
    port: int = 3306


class MariaHandler(Handler):
    def __init__(self, config: MariaDBConfig):
        self.config: Dict[str, Union(str, int)] = config.__dict__
        self.conn: pymysql.Connection = self.connect()

    def connect(self):
        return pymysql.Connection(
            **self.config,
            cursorclass=pymysql.cursors.DictCursor
            )

    def emit(self, record: LogRecord):
        print(inserSql.format(**record.__dict__))
        # try:
        #     recordTemp = copy.deepcopy(record)
        #     msgs: List[Any] = record.msg
        #     recordTemp.msg = " ".join([str(m) for m in msgs])
        # except Exception:
        #     self.handleError(record)
