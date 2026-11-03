
undo = []
redo = []

def push(x):
    undo.append(x)
    redo.clear()

def undo_op():
    if undo:
        x = undo.pop()
        redo.append(x)
        print("Undo:", x)
    else:
        print("Nothing to Undo")

def redo_op():
    if redo:
        x = redo.pop()
        undo.append(x)
        print("Redo:", x)
    else:
        print("Nothing to Redo")

def display():
    print("Actions:", undo)


# Main Program

while True:
    print("\n1. Push")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        x = input("Enter action: ")
        push(x)

    elif ch == 2:
        undo_op()

    elif ch == 3:
        redo_op()

    elif ch == 4:
        display()

    elif ch == 5:
        break

    else:
        print("Invalid choice")

# ALGORITHM
# 1. Start.
# 2. Create empty undo and redo stacks.
# 3. Display the menu: Push, Undo, Redo, Display, Exit.
# 4. Read the user's choice.
# 5. If Push is selected, read an action, push it onto undo, and clear redo.
# 6. If Undo is selected, pop from undo and push the item onto redo; if undo is empty, display a message.
# 7. If Redo is selected, pop from redo and push the item onto undo; if redo is empty, display a message.
# 8. If Display is selected, display the undo stack.
# 9. If Exit is selected, terminate; otherwise, display an invalid-choice message when appropriate.
# 10. Repeat the menu until Exit is selected.
# FLOWCHART
# START
#   |
#   v
# Initialize empty undo and redo stacks
#   |
#   v
# Display menu and read choice
#   |
#   v
# Choice?
#   |-- 1: Read action -> Push to undo -> Clear redo --|
#   |-- 2: Is undo empty? -> Yes: message; No: move top undo item to redo --|
#   |-- 3: Is redo empty? -> Yes: message; No: move top redo item to undo --|
#   |-- 4: Display undo stack -------------------------------------------|
#   |-- 5: Exit -> STOP
#   |-- Other: Display invalid choice ----------------------------------|
#   |
#   +-------------------- Repeat menu -------------------------------
