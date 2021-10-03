import time

from service.Log import Logger


cnt: int = 0
while True:
    Logger.warning('hello', 'world', cnt)
    time.sleep(10)
    cnt += 1
