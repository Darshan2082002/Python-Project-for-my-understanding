def selection(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
    
if __name__=="__main__":
    import random as rd
    arr=[]
    arr=rd.sample(range(1,100),99)
    print("Unsorted array is:",arr)
    
    ans=selection(arr)
    print(ans)