def partition (arr,low,high):
    pivot=arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
def quicksort(arr,low=0,high=None):
    if high is None:
        high = len(arr) - 1
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print("Sorted array is:", arr)