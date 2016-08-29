#!/usr/bin/env python
# encoding: utf-8
from collections import deque

def task(name, count):
    while count:
        yield
        print '{}:{}'.format(name, count)
        count -= 1

class Runner(object):

    def __init__(self, tasks):
        self.tasks = deque(tasks)

    def run(self):
        while self.tasks:
            task = self.tasks.pop()
            try:
                next(task)
            except StopIteration:
                pass
            else:
                self.tasks.appendleft(task)


if __name__ == '__main__':
    Runner([task('test1', 3), task('test2', 5)]).run()


