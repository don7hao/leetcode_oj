# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if None == head:
            return None

        header = ListNode(-1)
        prev   = header
        header.next = head
        slow   = head
        fast   = head.next
        count  = 0x00

        while None != fast:
            if slow.val == fast.val:
                fast = fast.next
                count += 1
                continue
            elif count > 0:
                prev.next = fast
                slow = fast
                count = 0
                fast = slow.next
            else:
                prev = slow
                slow = fast
                count = 0
                fast = slow.next
        if count > 0:
            prev.next = None
        return header.next

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    node_1 = ListNode(2)
    head.next = node_1

    node_2 = ListNode(3)
    node_1.next = node_2

    node_3 = ListNode(3)
    node_2.next = node_3

    node_4 = ListNode(4)
    node_3.next = node_4

    node_5 = ListNode(4)
    node_4.next = node_5

    node_6 = ListNode(5)
    node_5.next = node_6

    node_7 = ListNode(6)
    node_6.next = node_7

    head1 = s.deleteDuplicates(head)

    print '======================================='
    node = head1
    while None != node:
        print node.val
        node = node.next


