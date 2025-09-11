'''
Name: 160. Intersection of Two Linked Lists
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
'''

# Approach 1:
def getIntersectionNode(headA, headB):
    cntA = cntB = 0
    currA = headA
    currB = headB
    while currA is not None:
        cntA += 1
        currA = currA.next
    
    while currB is not None:
        cntB += 1
        currB = currB.next

    if cntA > cntB:
        for _ in range(cntA - cntB):
            headA = headA.next
    else:
        for _ in range(cntB - cntA):
            headB = headB.next
        
    while headA is not None and headB is not None:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next

# Alternate:
def getIntersectionNode2(headA, headB):
    cntA, cntB = 0, 0
    currA, currB = headA, headB
    while currA:
        cntA += 1
        currA = currA.next
    while currB:
        cntB += 1
        currB = currB.next

    # Align pointers
    while cntA > cntB:
        headA = headA.next
        cntA -= 1
    while cntB > cntA:
        headB = headB.next
        cntB -= 1

    # Move together and check for intersection
    while headA and headB:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

