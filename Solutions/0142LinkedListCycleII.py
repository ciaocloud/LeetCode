from typing import List, Optional


class ListNode(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None

def toString(node: ListNode, nodeList: List[ListNode]) -> str:
    if not node:
        return "no cycle"
    for i, node_in_list in enumerate(nodeList):
        if node == node_in_list:
            return "tail connects to node index %d" % i

# class LinkedList:
def constructLinkedList(listValues: List[int], pos: int) -> List[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    nodeList = []
    for v in listValues:
        cur.next = ListNode(v)
        nodeList.append(cur.next)
        cur = cur.next
    if pos >= 0:
        cur.next = nodeList[pos]
    return nodeList

def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if not fast or not fast.next:
        return None
    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return slow

if __name__ == '__main__':
    listVals = [3,2,0,-4]
    pos = 1
    nodeList = constructLinkedList(listVals, pos)
    print(toString(detectCycle(nodeList[0]), nodeList))

