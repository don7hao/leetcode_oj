#!/usr/bin/python
# -*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if None == head:
            return None
        #记录尾部节点
        tail_node = head
        next_node  = head.next
        while None != next_node:
            if head.val >= next_node.val:
                ## 更新头指针和next_node
                tmp = next_node.next
                next_node.next = head
                head = next_node
                next_node = tmp
            elif tail_node.val <= next_node.val:
                #小于或等于尾部节点
                tail_node.next = next_node
                tail_node = next_node
                next_node = next_node.next
            else:
                #从头部查找合适位置进行插入操作
                tmp = head.next
                prev = head
                while None != tmp:
                    if tmp.val > next_node.val:
                        break;
                    prev = tmp
                    tmp = tmp.next
                prev.next = next_node
                next_node = next_node.next
                prev.next.next = tmp
        tail_next = next_node #None
        return head


if __name__ == "__main__":
    s = Solution()
    head = ListNode(4)
    node_1 = ListNode(1)
    head.next = node_1

    node_2 = ListNode(3)
    node_1.next = node_2

    node_3 = ListNode(5)
    node_2.next = node_3

    node_4 = ListNode(9)
    node_3.next = node_4

    node_5 = ListNode(2)
    node_4.next = node_5

    node_6 = ListNode(8)
    node_5.next = node_6

    node_7 = ListNode(13)
    node_6.next = node_7

    node = s.insertionSortList(head)

    while None != node:
        print node.val
        node = node.next


