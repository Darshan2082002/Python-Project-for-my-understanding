"""
you are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array [Basically you have to sort the array]. Traverse array only once. 

Input :  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output :  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input :  [0, 1, 0]  
Output :  [0, 0, 1] 

Input :  [1, 1]  
Output :  [1, 1] 

Input :  [0]  
Output :  [0] 

"""
def segerate(arr):
    n=len(arr)
    count=0
    for i in range(n):
        if arr[i]==None:
            return arr
        elif arr[i]==1:
            count+=1
    for i in range(count):
        arr[i]=1
    for i in range(count,n):
        arr[i]=0
    return arr
arr=[0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(segerate(arr))