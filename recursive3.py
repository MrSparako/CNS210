import argparse

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

count=0
n1,n2=0,1
fib='1'
while count < Var:
    nth=n1+n2
    n1=n2
    n2=nth
    count+=1
    fib=fib+', '+str(nth)
print(fib,file=ArbName)
ArbName.close