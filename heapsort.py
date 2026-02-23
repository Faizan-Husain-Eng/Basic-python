# Heap Sort Program in Python

def heapify(arr, n, i):
    largest = i        # Assume root is largest
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Step 1: Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Move root to end
        heapify(arr, i, 0)


# Main Program
arr = [12, 11, 13, 5, 6, 7]

print("Original Array:", arr)

heap_sort(arr)

print("Sorted Array:", arr)