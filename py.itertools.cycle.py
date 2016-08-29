source = '''
from time import sleep
from itertools import cycle

for it in cycle([1,2,3]):
    print it
    sleep(1)
'''

print source
exec source
