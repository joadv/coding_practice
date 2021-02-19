# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        curr = result
        carry = 0
        while l1 or l2 or carry : # 각 리스트의 값을 다 더하고 1이 또 남아있는 경우를 위해 carry도 붙음
            if l1 :
                carry += l1.val
                l1 = l1.next
            if l2 :
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry //= 10
        return result.next