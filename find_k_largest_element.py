def sort(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
def prin(arr,k):
    
    sort(arr)
    return arr[::-k]
if __name__=="__main__":
    arr=[1,8,7,6,4,2]
    print(prin(arr,3))