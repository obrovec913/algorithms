# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slo = head
        fus = head
        '''ищем середину в списке'''
        while fus and fus.next and fus.next.next:
            slo = slo.next
            fus = fus.next.next
        fist = slo
        sch = slo.next
        '''переворачиваем вторую половину списка'''
        prev = None
        cur = sch
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        '''проверям список на палиндром'''
        h = head
        h1 = prev
        while h1:
            if not h.val == h1.val:
                return False
            h = h.next
            h1 = h1.next
        return True