
def selection_sort(arr):

    # Get the length of the list
    n = len(arr)

    # Outer loop controls the boundary between sorted and unsorted parts
    for i in range(n):

        # Assume the current index is the minimum
        min_index = i

        # Inner loop finds the smallest element in remaining unsorted array
        for j in range(i + 1, n):

            # Compare current element with current minimum
            if arr[j] < arr[min_index]:
                min_index = j   # Update index of smallest element

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print step-by-step result
        print(f"Step {i+1}: {arr}")

    return arr

# Example usage
data = [64, 25, 12, 22, 11]
print("Original Array:", data)
sorted_array = selection_sort(data)
print("Sorted Array:", sorted_array)

--------------------------------------------------------
a = list(map(int, input("Enter numbers: ").split()))

for i in range(len(a)):
    m = i

    for j in range(i+1, len(a)):
        if a[j] < a[m]:
            m = j

    a[i], a[m] = a[m], a[i]

print("Sorted List:", a)

#----------------------OUTPUT----------------------
Enter numbers: 64 25 12 22 11
Sorted List: [11, 12, 22, 25, 64]