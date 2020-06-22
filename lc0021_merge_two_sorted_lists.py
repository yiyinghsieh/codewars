"""Leetcode 21. Merge Two Sorted Lists
Easy

URL: https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first 
two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # print(l1.val, l1.next.val, l1.next.next.val)
        # lst = []
        # lst.append([l1.val,l1.next.next.val,l1.next.val])
        # print(lst)

        if not l1 or not l2:
            return l1 or l2

        # Create pre_head->node1->node2....
        pre_head = ListNode()
        current = pre_head
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 or l2

        return pre_head.next


def show(ls):
    result = []
    current = ls
    while current:
        result.append(current.val)
        current = current.next
    print(result)


def main():
    # l1 = ListNode(): val=0 (default), next=None (default)
    # l1 = ListNode(val=1): val=1, next=None (default)
    # l1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4)))

    # Output: [1]->1->2->3->4->4
    # l1: 1->2->4, l2: 1->3->4
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=4)
    l2 = ListNode(val=1)
    l2.next = ListNode(val=3)
    l2.next.next = ListNode(val=4)
    
    ls = Solution().mergeTwoLists(l1, l2)
    # print(ls.val, ls.next.val, ls.next.next.val,
    #       ls.next.next.next.val, ls.next.next.next.next.val, 
    #       ls.next.next.next.next.next.val)
    show(ls)


if __name__ == '__main__':
    main()

