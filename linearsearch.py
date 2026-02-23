# Recursive Linear Search

def linear_search(arr, key, index=0):
    # Base Case: If index reaches end, element not found
    if index >= len(arr):
        return -1
    
    # If element found
    if arr[index] == key:
        return index
    
    # Recursive Call
    return linear_search(arr, key, index + 1)


# Main Program
arr = [10, 25, 30, 45, 50]
key = int(input("Enter element to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")