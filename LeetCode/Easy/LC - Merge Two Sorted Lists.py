class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


if __name__ == '__main__':

    def mergeTwoLinkedLists(list1: ListNode, list2: ListNode):
        merged_list = ListNode()
        curr = merged_list

        while list1 and list2:
            if list1.val < list2.val:
                curr.next_node = list1
                curr = curr.next_node

                list1 = list1.next_node
            else:
                curr.next_node = list2
                curr = curr.next_node

                list2 = list2.next_node

        if list1 or list2:
            if list1:
                curr.next_node = list1
            else:
                curr.next_node = list2

        return merged_list.next_node


    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = mergeTwoLinkedLists(l1, l2)

    while True:
        print(merged.val)
        if merged.next_node is None:
            break
        else:
            merged = merged.next_node
