def repeat(arr):
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return arr[j]
def missing(arr):
    n=set(arr)
    l=len(n)
    
    
    return l

if __name__=='__main__':
    arr=[1,2,3,4,6,1]
    print((repeat(arr),missing(arr)))