def sort1(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
   

def prin(arr,k):
    arr = sort1(arr)
    
    return arr[-k:][::-1]
     

if __name__=="__main__":
    arr=[1,8,7,6,4,2]
    print(prin(arr,3))