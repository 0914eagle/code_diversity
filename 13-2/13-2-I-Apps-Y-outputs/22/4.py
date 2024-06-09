
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # use a set to keep track of the nodes we've visited
        visited = set()
        # loop through the list until we find a node we've visited before
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

