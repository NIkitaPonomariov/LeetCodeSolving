class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        k = head
        while curr:
            if curr == k.next:
                k.next
            else:
                curr.next = k.next
        return curr