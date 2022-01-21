# Time: O(n) where n is the number of noeds in linkedList
# Space: O(1)

def removeDuplicatesFromLinkedList(linkedList):
    walker = linkedList
    runner = linkedList

    while runner.next:
        if runner.value != walker.value:
            walker.next = runner
            walker = runner
        runner = runner.next

    if (walker.value == runner.value):
        walker.next = runner.next

    return linkedList
