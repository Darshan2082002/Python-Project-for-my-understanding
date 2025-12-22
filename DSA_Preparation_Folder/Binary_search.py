def binary_search(arr,target_val):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=low+high//2
        if arr[mid]==target_val:
            return mid
        elif arr[mid]<target_val:
            low=mid+1
        else:
            high=mid-1
    return -1
if __name__=="__main__":
    import random as rn
    arr=[1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    target=13
    result=binary_search(arr,target)
    print("Element found at index:",result) if result!=-1 else print("Element not found")