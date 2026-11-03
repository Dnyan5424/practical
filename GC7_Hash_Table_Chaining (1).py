
table = [[] for i in range(10)]

def hash_function(key):
    return key % 10

def insert(key):
    index = hash_function(key)
    table[index].append(key)
    print("Element inserted")

def search(key):
    index = hash_function(key)

    if key in table[index]:
        print("Element found")
    else:
        print("Element not found")

def display():
    for i in range(10):
        print(i, ":", table[i])


# Main Program

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        insert(key)

    elif ch == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif ch == 3:
        display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")

# ALGORITHM
# 1. Start.
# 2. Create a hash table containing 10 empty lists.
# 3. Define the hash function as key modulo 10.
# 4. Display the menu: Insert, Search, Display, Exit.
# 5. For Insert, read a key, calculate its index, and append the key to that index's list.
# 6. For Search, read a key, calculate its index, and check whether the key exists in that list.
# 7. For Display, print every index and its chain.
# 8. For Exit, terminate the program.
# 9. For an invalid choice, display an error message.
# 10. Repeat until Exit is selected.
# FLOWCHART
# START
#   |
#   v
# Create hash table with 10 empty chains
#   |
#   v
# Display menu and read choice
#   |
#   v
# Choice?
#   |-- Insert: Read key -> index = key % 10 -> Append key to chain --|
#   |-- Search: Read key -> index = key % 10 -> Check key in chain
#   |             -> Found / Not found -------------------------------|
#   |-- Display: Print all indexes and chains -------------------------|
#   |-- Exit: STOP
#   |-- Other: Display invalid choice ---------------------------------|
#   |
#   +-------------------- Repeat menu -------------------------------
