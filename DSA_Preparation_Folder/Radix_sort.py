def radix_sort(arr):
    if len(arr) == 0:
        return arr
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        for val in arr:
            radix_index = (val // exp) % 10
            buckets[radix_index].append(val)
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
        exp *= 10
    return arr

if __name__ == "__main__":
    myArray = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", myArray)
    sortedArray = radix_sort(myArray)
    print("Sorted array:", sortedArray)