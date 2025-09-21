class Node:
    def __init__(self, key):
        self.data=data
        self.Next=None
        self.prev=None
def insert(data):
    if data is None:
        return Node(data)
    else:
        n
            current=head
            while current.Next:
                current=current.Next
            current.Next=new_node
            new_node.prev=current
def display():
def delete(data):
def search(data):
def update(old_data,new_data):


if __name__ == "__main__":
    head=None
    
    while True:
        print("1. Insert")
        print("2. Display")
        print("3. Delete")
        print("4. Search")
        print("5. Update")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = int(input("Enter data to insert: "))
            head = insert(data)
        elif choice == 2:
            display()
        elif choice == 3:
            data = int(input("Enter data to delete: "))
            head = delete(data)
        elif choice == 4:
            data = int(input("Enter data to search: "))
            found = search(data)
            if found:
                print(f"{data} found in the list.")
            else:
                print(f"{data} not found in the list.")
        elif choice == 5:
            old_data = int(input("Enter old data to update: "))
            new_data = int(input("Enter new data: "))
            head = update(old_data, new_data)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")