head = [1,2,3,4,5]
head1 = head[::-1]

n = 2
n1 = len(head)



for i,j in zip( head1,range(1,len(head1)+1)):
    if(j == n ):
        head1.remove(i)
print(head1)

def removeNthFromEnd (n,head):
    if not head.next:
        return None
    Node1 = head
    Node1.prev = None
    while Node1.next:
        Node1.next.prev = Node1
        Node1 = Node1.next
    if n == 1:
        Node1.prev.next = None
        del Node1
        return head
    for i in range(n - 1):
        Node1 = Node1.prev
    if not Node1.prev:
        Head1 = Node1.next
        Head1.prev = None
        del Node1
        return Head1
    NodePrev = Node1.prev
    NodeNext = Node1.next
    NodePrev.next = NodeNext
    NodeNext.prev = NodePrev
    del Node1
    return head



d = removeNthFromEnd (2, head)