def max_heap(arr,i,n):
    largest=i
    left=2*i+1
    right=2*i+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if right<n and arr[right]>arr[largest]:
        largest=right
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heap(arr,largest,n)
    return arr
if __name__ == "__main__":
    arr=[3,5,1,10,2,7]
    print("Original array:",arr)
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        max_heap(arr,i,n)
    print("Max-Heap array:",arr)