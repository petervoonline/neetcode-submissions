# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        list_map = {}
        cur = head
        while cur != None:
            if cur not in list_map:
                list_map[cur] = 1
            else:
                return True
            cur = cur.next
        return False
        