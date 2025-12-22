class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return 0 if node is None else node.height

def update_height(node):
    if node is None:
        return 0
    node.height = 1 + max(get_height(node.left), get_height(node.right))
    return node.height

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def right_rotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    update_height(z)
    update_height(y)
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    update_height(z)
    update_height(y)
    return y

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)
    balance = get_balance(root)

    # Left Left
    if balance > 1 and key < root.left.data:
        return right_rotate(root)
    # Right Right
    if balance < -1 and key > root.right.data:
        return left_rotate(root)
    # Left Right
    if balance > 1 and key > root.left.data:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Left
    if balance < -1 and key < root.right.data:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def pre_order(root):
    if not root:
        return
    print(f"{root.data} ", end="")
    pre_order(root.left)
    pre_order(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

if __name__ == "__main__":
    root = None
    nums = [10, 20, 30, 40, 50, 25]
    for num in nums:
        root = insert(root, num)

    print("Preorder traversal of the constructed AVL tree is")
    pre_order(root)
    print("\nInorder traversal of the constructed AVL tree is")
    inorder(root)
    print("\nPostorder traversal of the constructed AVL tree is")
    postorder(root)
    print()

    key = 30
    if search(root, key) is not None:
        print("Found")
    else:
        print("Not Found")