def sort1(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return prin(arr)
   

def prin(arr,k):
    
    sort1(arr)
    
    for i in range(-3):
        print(arr[i])

if __name__=="__main__":
    arr=[1,8,7,6,4,2]
    print(prin(arr, 3))