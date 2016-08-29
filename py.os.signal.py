# encoding: utf-8

import signal
import time

# 并不是所有的信号都可以注册，如SIGKILL和SIGSTOP,内核对这两个有绝对控制

def handler(signum, frame):
    print signum,'|',frame


signal.signal(signal.SIGHUP, handler)

while True:
    time.sleep(10)

