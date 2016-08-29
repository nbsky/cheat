source = '''
from itertools import chain
for it in chain([1,2], [3,4], [5,6]):
    print it
'''
print source
exec source
