import argparse

parser = argparse.ArgumentParser(description='This program is used to add 2 integers.')

parser.add_argument('-a', type=str, help='First Integer',required=True, metavar='A')
parser.add_argument('-b', type=str, help='Second Integer',required=True, metavar='B')


args = parser.parse_args()

print(f"The sum of {args.a} and {args.b} is: {int(args.a) + int(args.b)}")