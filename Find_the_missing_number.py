def missing(arr):
    n=len(arr)+1
    total=n*(n+1)//2
    sum_of_arr=sum(arr)
    return total-sum_of_arr
if __name__=='__main__':
    arr=[1,2,3,5]
    print("The missing number in the array is:",missing(arr))
    