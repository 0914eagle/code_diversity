
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def hasCycle(head):
    # Use two pointers: fast and slow
    # If there is a cycle, fast will eventually catch slow
    # Since the cycle has a fixed length, we can use the following logic:
    # If fast catches slow, we know that the cycle length is k
    # We then move fast to the head of the list and slow to the beginning of the cycle
    # After one round of the cycle, fast will be k nodes ahead of slow
    # So we move fast k nodes, and then both fast and slow will be at the beginning of the cycle
    # If they meet again, we know there is a cycle
    # If they don't meet, we know there is no cycle

    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

