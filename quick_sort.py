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
    def sortList(self, head):
        if None == head or None == head.next:
            return head
        pivot   = head
        node    = head.next
        less_list    = None
        greater_list = None
        equal_list   = pivot

        while None != node:
            tmp = node.next
            if pivot.val > node.val:
                node.next = less_list
                less_list = node
            elif pivot.val < node.val:
                node.next = greater_list
                greater_list = node
            else:
                equal_list.next = node
                equal_list = node
            node = tmp
        #greater_list指向等于pivot的链表
        equal_list.next = None
        #less_list指向小于pivot的链表
        less_list = self.sortList(less_list)
        #greater_list指向大于pivot的链表
        greater_list = self.sortList(greater_list)
        less_list = self.connect(less_list, pivot, greater_list)

        return less_list

    def connect(self, less_list, pivot, greater_list):
        node = pivot
        while True:
            if node.next == None:
                node.next = greater_list
                break
            node = node.next

        node = less_list
        if less_list == None:
            less_list = pivot
        else:
            while node.next != None:
                node = node.next
            node.next = pivot
        return less_list

if __name__ == "__main__":
    s = Solution()
    head = ListNode(49)
    node_1 = ListNode(38)
    head.next = node_1

    node_2 = ListNode(65)
    node_1.next = node_2

    node_3 = ListNode(57)
    node_2.next = node_3

    node_4 = ListNode(76)
    node_3.next = node_4

    node_5 = ListNode(33)
    node_4.next = node_5

    node_6 = ListNode(27)
    node_5.next = node_6

    #node_7 = ListNode(13)
    #node_6.next = node_7

    node = head
    while None != node:
        print node.val
        node = node.next
    print '========================='

    node = s.sortList(head)
    print '#########################'
    while None != node:
        print node.val
        node = node.next
