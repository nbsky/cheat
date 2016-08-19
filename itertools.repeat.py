source = '''
from time import sleep
from itertools import repeat

for it in repeat('test', 5):
    print it
    sleep(1)
'''

print source
exec(source)
