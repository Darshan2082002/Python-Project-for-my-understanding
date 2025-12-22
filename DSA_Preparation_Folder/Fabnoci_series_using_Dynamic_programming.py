def dp(n):
  if (n<=1):
    return n
  fib[0]=0
  fib[1]=1
  for i in range(2,n+1):
    fib[i]=fib[i-2]+fib[i-1]
  return f[i]

