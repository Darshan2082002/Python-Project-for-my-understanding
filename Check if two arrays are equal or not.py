def equal(a,b):
    n,m=len(a),len(b)
    if n!=m:
        return False
    mp={}
    for num in a:
        mp[num]=mp.get(num,0)+1
    for num in b:
        if num not in mp:
            return False
        if mp[num]==0:
            return False
        else:
            mp[num]-=1
    return True

if __name__ == '__main__':
    a = [3, 5, 2, 5, 2]
    b = [2, 3, 5, 5, 2]

    if equal(a, b):
        print("true")
    else:
        print("false")