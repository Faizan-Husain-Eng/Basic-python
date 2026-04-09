def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]   # current element
        j = i - 1

        #Shift the elements until the correct position is found.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key   # correct position pe insert

# Example
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)

print("Sorted array:", arr)