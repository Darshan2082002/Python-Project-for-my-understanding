def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_sum = mergesort(arr[:mid])
    right_sum = mergesort(arr[mid:])
    return merge(left_sum, right_sum)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Unsorted array:", arr)
    sorted_arr = mergesort(arr)
    print("Sorted array:", sorted_arr)