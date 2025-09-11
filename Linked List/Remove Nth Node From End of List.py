'''
Name: 19. Remove Nth Node From End of List
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Approach
def removeNthFromEnd(head, n)
        if head is None:
            return None

        # length of list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # If n equals length, remove the head node
        if n == length:
            head = head.next
            return head

        # move to the (length-n)th node
        current = head
        for _ in range(length - n - 1):
            current = current.next

        # Delete the nth node from the end
        if current.next:
            current.next = current.next.next

        return head
