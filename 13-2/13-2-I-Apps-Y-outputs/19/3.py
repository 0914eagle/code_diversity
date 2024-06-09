
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
    # We then move fast back to the head of the list, and move both pointers forward by one at a time
    # If fast ever catches slow again, then we know that the cycle length is a multiple of k
    # If fast does not catch slow again, then we know that the cycle length is not a multiple of k, and there is no cycle
    
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    else:
        return False
    
    # If there is a cycle, find the length of the cycle
    length = 0
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
        length += 1
    
    # Move both pointers forward by the length of the cycle
    fast = head
    for _ in range(length):
        fast = fast.next
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    
    return True

