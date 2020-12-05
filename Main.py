from Node import Node
from TreeTraversal import preorder, postorder, inorder

if __name__=="__main__":

    #Create a binary search tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(postorder(root))