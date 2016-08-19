# encoding: utf-8

import signal
import time

def handler(signum, frame):
    print signum,'|',frame


signal.signal(signal.SIGHUP, handler)

while True:
    time.sleep(10)

