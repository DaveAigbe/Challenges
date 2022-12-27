class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next_node = _next


if __name__ == '__main__':
    def isPalindrome(head: ListNode) -> bool:
        if head is None:
            return True
        elif head.next_node is None:
            return True

        curr = head
        vals = []

        while curr:
            vals.append(curr.val)
            curr = curr.next_node

        flipped = curr[::-1]

        if vals == flipped:
            return True

        return False
