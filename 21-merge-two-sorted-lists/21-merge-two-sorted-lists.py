# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
          
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        r = ListNode()
        p = r
              
        if list1 == None and list2 == None:

            return None
    
        while list1 != None or list2 != None:
            
            if list1 == None:
                
                p.val = list2.val
                if list2.next != None:
                    p.next = ListNode()
                    p = p.next
                    
                list2 = list2.next
                
            elif list2 == None:
                
                p.val = list1.val
                if list1.next != None:
                    p.next = ListNode()
                    p = p.next
                    
                list1 = list1.next
           
            elif list1.val <= list2.val:
                
                p.val = list1.val
                p.next = ListNode()
                p = p.next
                list1 = list1.next
                
            else:
                
                p.val = list2.val
                p.next = ListNode()
                p = p.next
                list2 = list2.next
                
        return r
            
        
        