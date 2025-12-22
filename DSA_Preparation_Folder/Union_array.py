def union(a,b):
    st=set()
    for i in range(len(a)):
        st.add(a[i])
        
    for j in range(len(b)):
        st.add(b[i])
        
    res=[]
    for it in st:
        res.append(it)
    return res


if __name__ == "__main__":
    a = [1, 2, 3,1,5,4,7]
    b = [3, 2, 2]

    res = union(a, b)
    n=len(res)
    for i in range(n):
        print(res[i], end = '')
        
        
        