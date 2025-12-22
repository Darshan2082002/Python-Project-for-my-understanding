def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
def travesal(arr):
     for i in range(-1,-4,-1):
            print(arr[i],end=" ")
            
if __name__=='__main__':
    arr=[10,20,4,45,99,67]
    print("The last three digits of the array are:",end=" ")
    print(travesal(sort(arr)))
                    
        