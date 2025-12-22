def count(arr):
    n=len(arr)
    count=0
    for i in range(0,n):
        
        if arr[i]==1:
            count=count+1
        else:
            continue
    return count

if __name__=="__main__":
    arr=[1,1,0,0,0,1]
    print(count(arr))
    