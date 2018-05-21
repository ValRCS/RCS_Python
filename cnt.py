# from https://docs.python.org/3/library/argparse.html#module-argparse
import argparse

parser = argparse.ArgumentParser(description='Process some integers')
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='integer accumulator')
parser.add_argument('-s','--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default finds max)')

args = parser.parse_args()
print(args.accumulate(args.integers))