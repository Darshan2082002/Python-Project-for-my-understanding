def linearsearch(arr,target):
    n= len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
if __name__=="__main__":
    arr=[1,2,3,4,5]
    target=3
    result=linearsearch(arr,target)
    print("Element found at index:",result) if result!=-1 else print("Element not found")