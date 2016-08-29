source = '''
from time import sleep
from itertools import count
for c in count(10, 2):
    print c
    sleep(2)
'''
print source
exec(source)
