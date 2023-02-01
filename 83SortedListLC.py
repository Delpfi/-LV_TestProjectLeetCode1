class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        head1 = head
        while head.next:

            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return head1

c4 = ListNode(5)
c3 = ListNode(2,c4)
c2 = ListNode(1,c3)
c1 = ListNode(1,c2)
a = Solution()
Res = a.deleteDuplicates(c1)
Cur = Res

while Cur:
    print(Cur.val)
    Cur = Cur.next

print(Res)
