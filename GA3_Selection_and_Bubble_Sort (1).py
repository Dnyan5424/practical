
# GA3 - Bubble Sort and Selection Sort

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

print("Original Array:", arr)

# Bubble Sort
a = arr.copy()

for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Bubble Sort:", a)


# Selection Sort
b = arr.copy()

for i in range(n):
    min_index = i

    for j in range(i+1, n):
        if b[j] < b[min_index]:
            min_index = j

    b[i], b[min_index] = b[min_index], b[i]

print("Selection Sort:", b)

# ALGORITHM
# 1. Start.
# 2. Read the number of elements, n.
# 3. Read n elements and store them in the array.
# 4. Repeat the outer loop for each pass from 0 to n-1.
# 5. In each pass, compare adjacent elements using the inner loop.
# 6. If the current element is greater than the next element, swap them.
# 7. Continue until all passes are completed.
# 8. Display the sorted array.
# 9. Stop.
# FLOWCHART
# START
#   |
#   v
# Read n and input array elements
#   |
#   v
# Set i = 0
#   |
#   v
# Is i < n? ---- No ----> Display sorted array ----> STOP
#   | Yes
#   v
# Set j = 0
#   |
#   v
# Is j < n-i-1?
#   | Yes
#   v
# Is arr[j] > arr[j+1]?
#   | Yes                 | No
#   v                     |
# Swap adjacent elements  |
#   |_____________________|
#   v
# j = j + 1; repeat inner loop
#   |
#   v
# i = i + 1; repeat outer loop
