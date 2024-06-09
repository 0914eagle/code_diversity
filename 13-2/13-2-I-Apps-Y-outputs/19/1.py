
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    # Using a set to keep track of the nodes we've visited
    # If we encounter a node that is already in the set, we know there is a cycle
    # If we reach the end of the list and the node is not in the set, we know there is no cycle
    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False

