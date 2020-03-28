import argparse

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

Parser=argparse.ArgumentParser(description='Writes Fibonacci squence by the given number to a given file')
Parser.add_argument('--number', dest='number', type=int, required=True, help='Number used to generate the sequence')
Parser.add_argument('--file', dest='file',type=str, required=True, help='Name of the output file')
args=vars(Parser.parse_args())
Filename=args['file']
Var=args['number']

try: 
    ArbName=open(file=Filename,mode='x')
except:
    response=input('File Already Exists, Override y/n\n')
    if response=='y':
        ArbName=open(file=Filename,mode='w')
    else:
        exit()
print(factorial(Var),file=ArbName)
ArbName.close