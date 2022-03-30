import sys

from numpy import source

class SourceNotFound(Exception):
    pass

def checkSus():
    suus = sys.argv[1:]
    if '--source' in sys.argv:
        res = sys.argv.index('--source')
        if res < (len(suus)):
            return suus[res]
    raise SourceNotFound

print(checkSus())