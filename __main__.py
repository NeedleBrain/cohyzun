import sys

if __name__ == '__main__':
	import importlib

    if '--version' in sys.argv:
	    chatterbot = importlib.import_module('scatter')
	    print(chatterbot.__version__)