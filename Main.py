from Node import Node
from TreeTraversal import preorder, postorder, inorder

if __name__=="__main__":

    #Create a binary search tree
    root = Node(5)
    for i in [0,1,2,3,4,6,7,8,9,10]:
        root.insert(i)

    #do preorder traversal and print result
    bst = postorder(root)
    print(bst)