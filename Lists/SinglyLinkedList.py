'''
simple singly linked list implementation
'''

class Node:
    def __init__(self, val, next_node = None):
        self.data = val
        self.next = next_node
        
    def setNext(self, node):
        self.next = node

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def getHead(self):
        return self.head

    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            self._add(val, self.head)
            
    def _add(self, val, node):
        if node.next is not None:
            self._add(val, node.next)
        else:
            node.setNext(Node(val))

    def deleteList():
        self.head = None

    def find(self, val):
        if self.head is not None:
            return self._find(val, self.head)
        else:
            return None
        
    def _find(self, val, node):
        if val is node.data:
            return node
        elif node.next is not None:
            return self._find(val, node.next)
        else:
            return None
    def printLL(self):
        self._printLL(self.head)
    def _printLL(self, node):
        if node is not None:
            print (node.data)
            self._printLL(node.next)
        

#testing
linkedList = SinglyLinkedList()
linkedList.add(1)
linkedList.add(2)
linkedList.add(3)
linkedList.add(4)

linkedList.printLL()

print(linkedList.getHead().data)
print(linkedList.find(3).data)

