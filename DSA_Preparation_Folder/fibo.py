def fib(n):
    
    a=0
    b=1
    count=0
    while count<=n:
        count+=1
        a,b=b,a+b
        print(a)



print(fib(10))