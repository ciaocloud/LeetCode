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
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    cur = dummy = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    if l1:
        cur.next = l1
    if l2:
        cur.next = l2
    return dummy.next

def mergeTwoListsRecursive(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val <= l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2

if __name__ == '__main__':
    l1 = constructLinkedList([1,2,4])
    l2 = constructLinkedList([1,3,4])
    # print(mergeTwoLists(l1, l2))
    print(mergeTwoListsRecursive(l1, l2))