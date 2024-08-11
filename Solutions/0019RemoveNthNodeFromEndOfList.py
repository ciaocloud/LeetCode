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
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    prev = None
    slow = fast = dummy = ListNode(0, head)
    for _ in range(n):
        fast = fast.next
    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    prev.next = slow.next
    return dummy.next

if __name__ == '__main__':
    head = constructLinkedList([1, 2, 3, 4, 5])
    print(removeNthFromEnd(head, 2))