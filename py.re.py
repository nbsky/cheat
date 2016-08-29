# remove [] and Contents inside in "[lol]markup[smile]"
source = '''
s = '[lol]markup[smile]'
import re
print re.sub('\[.*?\]', '', s)
'''
print source
exec(source)
