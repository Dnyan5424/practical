
# GA1: Library Book Borrowing Records

# Number of books borrowed by each member
books = [5, 3, 0, 8, 2, 0, 5, 4]

# Calculate average borrowing
total = sum(books)
average = total / len(books)
print("Average borrowing:", average)

# Find highest and lowest borrowing
print("Highest borrowing:", max(books))
print("Lowest borrowing:", min(books))

# Count members who borrowed zero books
zero_count = books.count(0)
print("Members with zero borrowing:", zero_count)

# Find mode (most frequently occurring count)
mode = max(set(books), key=books.count)
print("Most frequent borrowing:", mode)

# ALGORITHM
# 1. Start.
# 2. Store the number of books borrowed by each member in a list.
# 3. Calculate the total number of books using sum().
# 4. Calculate average borrowing by dividing total by the number of members.
# 5. Find and display the highest and lowest borrowing values.
# 6. Count and display members who borrowed zero books.
# 7. Find and display the most frequently occurring borrowing count (mode).
# 8. Stop.
# FLOWCHART
# START
#   |
#   v
# Store book-borrowing values in a list
#   |
#   v
# Calculate total and average
#   |
#   v
# Find highest and lowest values
#   |
#   v
# Count zero-borrowing members
#   |
#   v
# Find and display mode
#   |
#   v
# STOP
