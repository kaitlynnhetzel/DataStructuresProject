'''

simple binary tree implementation

'''

class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.data = val
        

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)
            

    def _add(self, val, node):
        if val < node.data:
            if node.left is not None:
                self._add(val, node.left)
            else:            
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
                
    def delete():
        self.root = None

    def find(self, val):
        if self.root is not None:
           return self._find(val, self.root)
        else:
            return None
        
    def _find(self, val, node):
        if val is node.data:
            return node
        elif val < node.data and node.left is not None:
            return self._find(val, node.left)

        elif val > node.data and node.right is not None:
            return self._find(val, node.right)

    def printBST(self):
        if self.root is not None:
            self._printBST(self.root)

    def _printBST(self, node):
        if node is not None:
            self._printBST(node.left)
            print (node.data)
            self._printBST(node.right)



#testing         
binTree = BinarySearchTree()
binTree.add(1)
binTree.add(4)
binTree.add(10)
binTree.add(15)
binTree.add(-1)
binTree.add(9)
print ("Data of the root is: "+str(binTree.getRoot().data))
print ("Data of the -1 node is: "+str(binTree.find(-1).data))
print ("Data within the BST: ")
binTree.printBST() 
