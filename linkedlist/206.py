# https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List

def reverseList(head):
        prev = None
        curr = head
        while curr:
            # temporarily save next
            next = curr.next
            # next pointer now points to prev
            curr.next = prev
            # move pointer
            prev = curr
            curr = next
        return prev