# Recursive Binary Search

def binary_search(arr, low, high, key):
    # Base Case
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    # If element found
    if arr[mid] == key:
        return mid
    
    # If key is smaller, search left half
    elif key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    
    # If key is larger, search right half
    else:
        return binary_search(arr, mid + 1, high, key)


# Main Program
arr = [10, 20, 30, 40, 50, 60]  # Sorted array
key = int(input("Enter element to search: "))

result = binary_search(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")