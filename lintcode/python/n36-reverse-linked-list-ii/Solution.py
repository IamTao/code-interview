"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if m < 1 or m > n or head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        for ind in xrange(m - 1):
            head = head.next

        pre, cur = head.next, head.next.next

        for ind in xrange(0, n - m):
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        head.next.next = cur
        head.next = pre
        return dummy.next

if __name__ == '__main__':
    node1 = ListNode(0)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node = Solution().reverseBetween(node1, 1, 2)
    while node is not None:
        print node.val
        node = node.next
