class ListNode:
    def __init__(self, x, _next=None):
        self.val = x
        self.next_node = _next


if __name__ == '__main__':
    def delete_elements(head: ListNode, val: int):
        if head is None:  # If list is empty
            return head
        elif head.next_node is None:  # If there is only 1 node in the list
            if head.val == val:  # If the single node is a target value, remove its reference
                head = None
                return head
            else:
                return head

        prev = head  # Keep track of previous node
        curr = head.next_node  # Keep track of current node
        while True:
            if curr is not None:
                if curr.val == val:
                    curr = curr.next_node  # Link the previous node to the node that is after current
                    prev.next_node = curr
                else:  # Otherwise move up the point for the previous and current nodes
                    prev = curr
                    curr = curr.next_node
            else:
                if head.val == val:  # Edge case of if head is a target node, return its linked node instead
                    return head.next_node
                return head


    l1 = ListNode(6, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    l2 = ListNode(7, ListNode(7, ListNode(7, ListNode(7, ListNode(7, ListNode(7, ListNode(7)))))))
    delete_elements(l1, 6)
    delete_elements(l2, 7)

    current = l2
    while current:
        print(current.val)
        current = current.next_node
