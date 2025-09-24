def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr[-2]
if __name__=='__main__':
    arr=[10,20,4,45,99,67]
    print("The second largest element in the array is:",sort(arr))