from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        nodes = []
        cur = self
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        return str(nodes)


def constructLinkedList(arr):
    if not arr:
        return None
    nodes = [ListNode(v) for v in arr]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    return nodes[0]

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    ## Iterative
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev

def reverseLinkedListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    # if not head or not head.next:
    #     return head
    # nxt = head.next
    # tail = reverseLinkedListRecursive(nxt)
    # nxt.next = head
    # head.next = None
    # return tail
    if not head or not head.next:
        return head
    nxt = head.next
    tail = reverseLinkedListRecursive(nxt)
    nxt.next = head
    head.next = None
    return tail

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ## iterative
        # prev, cur = None, head
        # while cur:
        #     nxt = cur.next
        #     cur.next = prev
        #     prev, cur = cur, nxt
        # return prev

        ## recursive
        if not head or not head.next:
            return head
        nxt = head.next
        tail = self.reverseList(nxt)
        nxt.next = head
        head.next = None
        return tail


if __name__ == '__main__':
    head = constructLinkedList([1, 2, 3, 4, 5])
    print(reverseList(head))
    # print(reverseLinkedListRecursive(head))
    tail = reverseLinkedListRecursive(head)
    print(tail.next)
    sol = Solution()
    print(sol.reverseList(head))