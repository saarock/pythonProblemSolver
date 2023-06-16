class Node:
    # This is the one way to implement the data in the linked list and there is another method also
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next = None


class myLinkedList:
    def __init__(self):
        self.headval = None


head = myLinkedList()
if(head.headval==None):
    head.headval = Node('1')
    v = head.headval
    head.headval = Node(2)
    head.headval.next = v
    


    print('yes')        
print(head.headval.dataval)
print(head.headval.next.dataval)

