def min_heap(arr,i,n):
    smallest=i
    left=2*i+1
    right=2*1+2
    if left<n and arr[left]<arr[smallest]:
        smallest=left
    if right<n and arr[right]<arr[smallest]:
        smallest=right 
    if smallest!=i:
        arr[i],arr[smallest]=arr[smallest],arr[i]
        min_heap(arr,smallest,n)
    return arr
if __name__ == "__main__":
    arr=[3,5,1,10,2,7]
    print("Original array:",arr)
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        min_heap(arr,i,n)
    print("Min-Heap array:",arr)