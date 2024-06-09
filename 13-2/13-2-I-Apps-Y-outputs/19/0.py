
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    # Use two pointers: fast and slow
    # If there is a cycle, fast will eventually catch slow
    # Since the cycle has a fixed length, we can use the following logic:
    # If fast catches slow, we know that the distance between them is equal to the length of the cycle
    # We can then move fast to the head of the list and slow to the beginning of the cycle
    # If they meet at the same node, we know that there is a cycle
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
