def largest(arr):
    if len(arr)==None:
        return None 
    else:
        return max(arr)
            



if __name__=='__main__':
    arr=[10,20,4]
    print("The largest element in the array is:",largest(arr))S