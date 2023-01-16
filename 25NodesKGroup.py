# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        if not head.next:
            return head
        







c2 = ListNode(2)
c1 = ListNode(1,c2)
a = Solution()
Res = a.reverseKGroup(c1,2)

Curr = Res
while Curr:
    print(Curr.val)
    Curr = Curr.next

print(Res)