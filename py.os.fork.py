# encoding: utf-8

import os
import sys
import signal
import time

######### fork前:
# :ps -o  pid,ppid,sid,comm,args -wwf
# PID   PPID   SID  COMMAND         COMMAND
# 9955  3358  3358  \_ python       \_ python os.fork.py
# fork 前父id 和 sid 都是zsh

pid = os.fork()
if pid > 0:
    sys.exit(0)

def handler(signum, frame):
    print signum,'|',frame

signal.signal(signal.SIGHUP, handler)

####### fork后,如果没有setsid：
# :ps -o  pid,ppid,sid,comm,args -wwf
# PID   PPID   SID  COMMAND         COMMAND
# 31033 1      3358 python          python os.fork.py
# fork 使得该进程父进程为init 即ppid为1, 但是sessionid 还是原来的session组, 3358是zsh的pid, 一旦zsh退出该进程还是会收到HUP信号

os.setsid() # 设置该子进程为进程组组长，如果不是组长就会收到session组长的信号,这个调用只对非session组长有效

# 设置完
# PID   PPID   SID  COMMAND         COMMAND
# 11577     1 11577 python          python os.fork.py
# setsid后变成sid变成自己了，不会在收到其他进程的信号


os.chdir("/") # 更改目录，比如原来父进程的目录是在某个u盘，这时候这个守护进程就会在后台还占用这个目录
os.umask(0)


###### 下面再次fork是可选的，目的是让自己变成子进程，因为这样自己就无法使用终端,彻底切断了可能被终端发送信号停止的命运
pid = os.fork()

# 再次fork是自己自己变成非会话组长
# PID   PPID   SID  COMMAND         COMMAND
# 12402     1 12401 python          python os.fork.py

if pid> 0:
    sys.exit(0)

def handler(signum, frame):
    print signum,'|',frame

signal.signal(signal.SIGHUP, handler)

while True:
    time.sleep(10)
