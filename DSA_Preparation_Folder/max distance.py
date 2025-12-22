def maxdistance(arr):
    mp={}
    res=0
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]]=i
        else:
            res=max(res,i-mp[arr[i]])
    return res

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 1]
    print(maxdistance(arr))
            