class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def getheight(root):
    if not root:
        return 0
    return root.height

def getbalance(root):
    if not root:
        return 0
    return getheight(root.left) - getheight(root.right)

def updateheight(root):
    if not root:
        return 0
    root.height = 1 + max(getheight(root.left), getheight(root.right))
    return root.height

def rightrotate(z):
    x = z.left
    temp = x.right
    x.right = z
    z.left = temp
    updateheight(z)
    updateheight(x)
    return x

def leftrotate(z):
    y = z.right
    temp = y.left
    y.left = z
    z.right = temp
    updateheight(z)
    updateheight(y)
    return y

def insert(root, value):
    if not root:
        return Tree(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    updateheight(root)
    balance = getbalance(root)
    if balance > 1 and value < root.left.value:
        return rightrotate(root)
    if balance < -1 and value > root.right.value:
        return leftrotate(root)
    if balance > 1 and value > root.left.value:
        root.left = leftrotate(root.left)
        return rightrotate(root)
    if balance < -1 and value < root.right.value:
        root.right = rightrotate(root.right)
        return leftrotate(root)
    return root

if __name__ == "__main__":
    root = Tree(50)            # create root node correctly
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("Root is:", root.value)
    print("Left child of root is:", root.left.value)
    print("Right child of root is:", root.right.value)
    print("Height of root is:", root.height)

