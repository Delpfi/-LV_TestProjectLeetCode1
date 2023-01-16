
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):

        if not head:
            return None
        if not head.next:
            return head
        c1 =head
        c2 = head.next
        new_head = c2
        #c3 = c2.next
        #c1.next = c3
        q3 = c2.next
        c1.next = q3
        prev = c1
        new_head.next  = c1

        while True:
            if not q3:
                return new_head
            if not q3.next:
                return new_head
            q4 = q3.next
            x = q4
            y = q4.next
            z = q3
            q3.next = y
            q4.next = q3
            prev.next = q4
            prev = q4
            q3 = prev.next

c5 = ListNode(5)
c4 = ListNode(4,c5)
c3 = ListNode(3,c4)
c2 = ListNode(2,c3)
c1 = ListNode(1,c2)

a = Solution()
Res = a.swapPairs(c1)
Curr = Res
while Curr:
    print(Curr.val)
    Curr = Curr.next

print(Res)