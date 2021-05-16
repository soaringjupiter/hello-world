import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--friendly", help="displays a more friendly message", action="store_true")
args = parser.parse_args()
if args.friendly:
	print('hello world :)')
else:
	print('hello world')