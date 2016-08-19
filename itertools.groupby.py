# like linux uniq, must be sorted
source = '''
import itertools
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)
'''
#A ['A', 'a', 'a']
#B ['B', 'B', 'b']
#C ['c', 'C']
#A ['A', 'A', 'a']
print source
exec(source)

