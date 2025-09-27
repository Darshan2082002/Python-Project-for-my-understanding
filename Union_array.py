def union(a,b):
    n,m=len(a),len(b)
    if n==0 and m ==0:
        return 0
    mp={}
    for i in range(n):
        mp[a[i]]=i
        
    for mp in b:
        
        