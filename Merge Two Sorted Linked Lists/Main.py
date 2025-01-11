from typing import List, Optional 
from copy import deepcopy

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newlist = ListNode()  
        head = None      
        while list1 or list2:
            if list1== None and list2 != None:
                if head == None:
                    newlist = deepcopy(list2)
                    head = newlist
                    list2 = list2.next
                else:
                    newlist.next = deepcopy(list2)
                    newlist = newlist.next
                    list2 = list2.next
            elif list2== None and list1 != None:
                if head == None:
                    newlist = deepcopy(list1)
                    head = newlist
                    list1 = list1.next
                else:
                    newlist.next = deepcopy(list1)
                    newlist = newlist.next
                    list1 = list1.next
            elif list1.val == list2.val:
                if head == None:
                    newlist = deepcopy(list1)
                    head = newlist
                    newlist.next = deepcopy(list2)
                    newlist = newlist.next
                    list1 = list1.next
                    list2 = list2.next
                else:
                    newlist.next = deepcopy(list1)
                    newlist = newlist.next
                    newlist.next = deepcopy(list2)
                    newlist = newlist.next
                    list1 = list1.next
                    list2 = list2.next
            elif list1.val < list2.val:
                if head == None:
                    newlist = deepcopy(list1)
                    head = newlist
                    list1 = list1.next
                else:
                    newlist.next = deepcopy(list1)
                    newlist = newlist.next
                    list1 = list1.next
            elif list2.val < list1.val:
                if head == None:
                    newlist = deepcopy(list2)
                    head = newlist
                    list2 = list2.next
                else:
                    newlist.next = deepcopy(list2)
                    newlist = newlist.next
                    list2 = list2.next
        return head

if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: Basic input
    input1  = [1,2,4]
    input2  = [1,3,5]
    ll1 = builLinkedList(input1)
    ll2 = builLinkedList(input2)
    printLinkedList(ll1)
    printLinkedList(ll2)
    mll = solution.mergeTwoLists(ll1,ll2)
    printLinkedList(mll)
            