
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, key):
    if root == None:
        return Node(key)

    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def search(root, key):
    if root == None or root.data == key:
        return root

    if key < root.data:
        return search(root.left, key)
    else:
        return search(root.right, key)


def display(root):
    if root:
        display(root.left)
        print(root.data, end=" ")
        display(root.right)


def delete(root, key):
    if root == None:
        return root

    if key < root.data:
        root.left = delete(root.left, key)

    elif key > root.data:
        root.right = delete(root.right, key)

    else:
        if root.left == None:
            return root.right

        elif root.right == None:
            return root.left

        temp = root.right

        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Main Program

root = None

while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key: "))
        root = insert(root, key)

    elif ch == 2:
        key = int(input("Enter key to search: "))

        if search(root, key):
            print("Element found")
        else:
            print("Element not found")

    elif ch == 3:
        print("BST:")
        display(root)
        print()

    elif ch == 4:
        key = int(input("Enter key to delete: "))
        root = delete(root, key)

    elif ch == 5:
        break

    else:
        print("Invalid choice")

# ALGORITHM
# 1. Start.
# 2. Initialize the BST root as None.
# 3. Display the menu: Insert, Search, Display, Delete, Exit.
# 4. For Insert, read a key and insert it in its correct position: smaller values go left; greater or equal values go right.
# 5. For Search, compare the key with the current node; move left for a smaller key and right for a greater key until found or None is reached.
# 6. For Display, perform inorder traversal: left subtree, node, right subtree.
# 7. For Delete, locate the key.
# 8. If the node has no left child, return its right child; if it has no right child, return its left child.
# 9. If the node has two children, find the minimum node in the right subtree, copy its value, and delete that successor.
# 10. Repeat the menu until Exit is selected.
# FLOWCHART
# START
#   |
#   v
# Set root = None
#   |
#   v
# Display menu and read choice
#   |
#   v
# Choice?
#   |-- Insert: Read key -> Insert by BST comparison -----------------|
#   |-- Search: Read key -> Compare and move left/right -> Found? -----|
#   |-- Display: Inorder traversal (Left, Root, Right) ----------------|
#   |-- Delete: Find node -> 0/1 child? reconnect child
#   |                         -> 2 children? use inorder successor
#   |                         -> Delete successor ---------------------|
#   |-- Exit: STOP
#   |-- Other: Display invalid choice ---------------------------------|
#   |
#   +-------------------- Repeat menu -------------------------------
