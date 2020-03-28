import sys
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

Var=sys.argv[1]
Filename=sys.argv[2]

try: 
    ArbName=open(file=Filename,mode='x')
except:
    response=input('File Already Exists, Override y/n\n')
    if response=='y':
        ArbName=open(file=Filename,mode='w')
    else:
        exit()
print(factorial(int(Var)),file=ArbName)