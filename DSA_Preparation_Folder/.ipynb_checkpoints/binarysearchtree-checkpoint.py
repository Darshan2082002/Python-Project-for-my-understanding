class binarysearchtree:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def insert(root,value):
    if root is None:
        return binarysearchtree(value)
    if value<root.key:
        root.left=insert(root.left,value)
    else:
        root.right=insert(root.right,value)
    return root
def search(root,value):
    if root is None or root.key==value:
        return root
    if value<root.key:
        return search(root.left,value)
    return search(root.right,value)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.key,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key,end=" ")

if __name__=="__main__":
    root=binarysearchtree(50)
    insert(root,30)
    insert(root,20)
    insert(root,40)
    insert(root,70)
    insert(root,60)
    insert(root,80)
    print("Inorder traversal is:")
    inorder(root)
    print("\nPreorder traversal is:")
    preorder(root)
    
    print("\nPostorder traversal is:")
    postorder(root)
    result=search(root,60)
    if result:
        print("\nElement found:",result.key)
    else:
        print("\nElement not found")