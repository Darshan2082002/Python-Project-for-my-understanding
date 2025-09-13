def div(arr):
    mid=len(arr)//2
    if len(arr)<=1:
        return arr
    left=div(arr[:mid])
    right=div(arr[mid:])
    return conquer(left,right)
def conquer(left,right):
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
if __name__=="__main__":
    import random as rd
    arr=[]
    arr=rd.sample(range(1,100),10)
    print("Unsorted array is:",arr)
    
    ans=div(arr)
    print("Sorted array is:",ans)