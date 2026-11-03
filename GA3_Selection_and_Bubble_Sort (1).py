
arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array:", arr)

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
