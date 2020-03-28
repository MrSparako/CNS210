import argparse

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

Parser=argparse.ArgumentParser(description='Writes Fibonacci squence by the given number to a given file')
Parser.add_argument('number',type=int,
    help='number help')
Parser.add_argument('file', type=str)
print('test')
args=Parser.parse_args(['number','file'])
print(args)
Filename=Parser.parse_args(['file'])

try: 
    ArbName=open(file=Filename,mode='x')
except:
    response=input('File Already Exists, Override y/n\n')
    if response=='y':
        ArbName=open(file=Filename,mode='w')
    else:
        exit()
print(factorial(Var),file=ArbName)