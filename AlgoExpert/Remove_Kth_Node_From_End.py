# Time Complexty: O(n) where n is the number of nodes
# Space Complexty: O(1)

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    runner = head
    walker = head
    prev = head

    for _ in range(k):
        runner = runner.next

    while runner:
        prev = walker
        walker = walker.next
        runner = runner.next

    if prev == walker:
        head.value = head.next.value
        head.next = head.next.next
    else:
        prev.next = walker.next
