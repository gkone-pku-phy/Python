def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

import json
f=open('jsonfile','r+')
x=json.load(f)
print(x)
y=[e^2 for e in x if e%2==0]
json.dump(y,f)
