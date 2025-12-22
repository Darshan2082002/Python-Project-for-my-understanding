output=[]
def count(arr,n):
    output=[0]*n
    count=[0]*200
    for i in range(n):
        count[i]=0
    for j in range(n):
        count[arr[j]]+=1
    for i in range(1,199):
        count[i]+=count[i-1]
    for j in range(n-1,-1,-1):
        output[count[arr[j]]-1]=arr[j]
        count[arr[j]]-=1
    print("sorted array is:",output)


if __name__=="__main__":
    import random as rd
    arr=rd.sample(range(0,200),10)
    n=len(arr)
    print("Unsorted array is:",arr)
    count(arr,n)