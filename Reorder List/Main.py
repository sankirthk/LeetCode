from typing import List, Optional 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def builLinkedList(values:List[int]) -> Optional[ListNode]:
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printLinkedList(head: Optional[ListNode]) -> None:

    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    print(values)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        printLinkedList(head)




if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1  = [1,2,3,4]
    ll = builLinkedList(input1)
    printLinkedList(ll)
    solution.reorderList(ll)
