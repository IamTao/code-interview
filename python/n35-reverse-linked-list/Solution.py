"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """

    def reverse(self, head):
        return self.reverse1(head)

    def reverse1(self, head):
        # write your code here
        result   = None  # it use None to avoid the loop.
        node    = head
        while node != None:
            tmp         = node.next
            node.next   = result 
            result      = node
            node        = tmp
        return result


    # not good at Recursion. Try to rethink it.
    def reverse2(self, head):
        if head is None or head.next is None:
            return head
        tail        = head.next
        head.next   = None # use this to break the loop
        newhead     = self.reverse2(tail) # it corresponds to the first if else condition to figure out the head that to return.
        tail.next   = head # use this function to reverse
        return newhead 