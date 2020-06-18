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
        print(l1.val, l1.next.val, l1.next.next.val)








def main():
    # Output: 1->1->2->3->4->4
    # l1: 1->2->4, l2: 1->3->4
    l1 = ListNode(val=1)
    l1.next = ListNode(val=2)
    l1.next.next = ListNode(val=4)
    l2 = ListNode(val=1)
    l2.next = ListNode(val=3)
    l2.next.next = ListNode(val=4)
    print(Solution().mergeTwoLists(l1, l2))


if __name__ == '__main__':
    main()

