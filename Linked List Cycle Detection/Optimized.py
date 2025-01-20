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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowPointer, fastPointer = None, None

        slowPointer = head
        fastPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
            if slowPointer == fastPointer:
                return True
        return False

            
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1  = [0,1,2,3]
    ll = builLinkedList(input1)
    printLinkedList(ll)
    rll = solution.hasCycle(ll)
    print(rll)