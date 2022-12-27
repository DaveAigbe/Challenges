class ListNode:
    def __init__(self, x, _next=None):
        self.val = x
        self.next_node = _next


if __name__ == '__main__':
    def delete_node(node: ListNode):
        node.val = node.next_node.val
        node.next = node.next_node.next_node


    to_delete = ListNode(3)
    l1 = ListNode(1, ListNode(2, ListNode(4)))

    current = l1
    while current:
        print(current.val)
        current = current.next_node
