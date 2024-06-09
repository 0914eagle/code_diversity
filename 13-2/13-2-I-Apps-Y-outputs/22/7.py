
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # use a set to keep track of the nodes we've visited
        visited = set()
        # loop through the list until we reach the end
        while head:
            # if we've visited this node before, there must be a cycle
            if head in visited:
                return True
            # add the current node to the set of visited nodes
            visited.add(head)
            # move on to the next node
            head = head.next
        # if we reach the end of the list without finding a cycle, return False
        return False

