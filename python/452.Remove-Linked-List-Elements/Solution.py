# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        dummy 		= ListNode(0)
        dummy.next 	= head
        cur 		= dummy
        while cur and cur.next:
        	if cur.next.val == val:
        		cur.next = cur.next.next
        	else:
        		cur = cur.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head == None:
            return None
        head.next = self.removeElements(head.next, val)
        if head.val == val:
            return head.next
        else:
            return head  