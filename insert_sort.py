def insert(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        # Shift elements of arr[0..i-1] that are greater than current_value
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr   

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Unsorted array:", arr)
    sorted_array = insert(arr.copy())  
    print("Sorted array:", sorted_array)