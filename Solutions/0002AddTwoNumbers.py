class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        l = []
        node = self
        while node:
            l.append(node.val)
            node = node.next
        return str(l)
        # return '->'.join(str(v) for v in l)

def fromList(digits):
    dummy = cur = ListNode()
    for d in digits:
        cur.next = ListNode(d)
        cur = cur.next
    return dummy.next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur = dummy = ListNode()
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry % 10)
        cur = cur.next
        carry //= 10
    return dummy.next

# def addTwoNumbersRecursive(l1: ListNode, l2: ListNode) -> ListNode:


if __name__ == '__main__':
    l1 = fromList([9,9,9,9,9,9,9])
    l2 = fromList([9,9,9,9])
    print(addTwoNumbers(l1, l2))
    s = "ab"
    print("##", list(range(1)), s[0:1])
