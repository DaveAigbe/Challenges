class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


if __name__ == '__main__':
    def reverseList(head: ListNode) -> ListNode:
        # Nothing to reverse if length is of 0 or 1
        if head is None or head.next is None:
            return head

        curr = head
        nodes = []

        # Store all nodes in an array
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Reverse node array
        nodes[:] = nodes[::-1]

        # Tail is now the head
        new_head = nodes[0]
        # Keep track of the node that needs a link
        unlinked_node = new_head
        # Attach unlinked node to current value in node array
        for i in range(1, len(nodes)):
            unlinked_node.next = nodes[i]
            unlinked_node = unlinked_node.next

        # Tail will be unlinked, so set it to none
        unlinked_node.next = None
        return new_head


    l1 = ListNode(1, ListNode(2, ListNode(4)))
    r = reverseList(l1)

    while True:
        print(r.val)
        if r.next is None:
            break
        else:
            r = r.next
