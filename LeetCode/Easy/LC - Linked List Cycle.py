class ListNode:
    def __init__(self, x, _next=None):
        self.val = x
        self.next_node = _next


if __name__ == '__main__':
    def hasCycle(head: ListNode) -> bool:

        if head is None:
            return False
        elif head.next_node is None:
            return False

        curr = head
        nodes = []

        while curr:
            if curr in nodes:
                return True
            else:
                nodes.append(curr)
                curr = curr.next_node

        return False



