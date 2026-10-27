# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        #find mid
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next #slow is middle when fast is done
        
        #split
        right = slow.next
        slow.next = None

        #reverse half right
        prev = None
        curr = right
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        #swap
        left = head
        right = prev

        while left and right:
            nextNodeLeft = left.next
            nextNodeRight = right.next
            left.next = right
            right.next = nextNodeLeft
            left = right.next
            right = nextNodeRight
        
        