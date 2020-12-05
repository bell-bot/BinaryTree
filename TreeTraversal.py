def preorder(node):

    if (node is None):
        return  []

    #1. visit root
    #2. traverse left subtree
    #3. traverse right subtree
    return [node.value] + preorder(node.left) + preorder(node.right)

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