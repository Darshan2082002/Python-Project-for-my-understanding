def insert(arr):
    n=len(arr)
    i=0
    for i in range(n):
        key=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>key:
                arr[j+1],arr[j]=arr[j],arr[j+1]
            else:
                break
    return arr
if __name__=="__main__":
    import random as rd
    arr=[]
    arr=rd.sample(range(1,100),99)
    print("Unsorted array is:",arr)
    
    ans=insert(arr)
    print(ans)