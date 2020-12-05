class Node:

    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if value < self.value:
            #Insert into left subtree
            if self.left is None:
                self.left = Node(value)
            else:
                #If the node already has a left child, recursively try to insert
                #the new value into the left subtree
                self.left.insert(value)

        else:
            #Insert into right subtree
            if self.right is None:
                self.right = Node(value)
            else:
                #If the node already has a right child, recursively try to insert
                #the new value into the right subtree
                self.right.insert(value)


                