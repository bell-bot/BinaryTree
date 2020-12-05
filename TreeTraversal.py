def preorder(node):

    if (node is None):
        return  []

    #First, visit root:
    root = node.value
    if node.left and node.right:
        return [root] + preorder(node.left) + preorder(node.right)
    elif not(node.left):
        return [root] + preorder(node.right)
    elif not(node.right):
        return [root] + preorder(node.left)
    else:
        return [root] 

def postorder(node):
    if (node is None):
        return []

    #1. traverse left subtree
    #2. traverse right subtree
    #3. visit route
    return postorder(node.left) + postorder(node.right) + [node.value]

def inorder(node):

    if (node is None):
        return []

    #1. traverse left subtree
    #2. visit root
    #3. traverse right subtree
    return inorder(node.left) + [node.value] + inorder(node.right)