class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next_node = next_node


if __name__ == '__main__':
    list_1 = ListNode(1, ListNode(2, ListNode(4)))
    list_2 = ListNode(1, ListNode(3, ListNode(4)))


    def mergeTwoLinkedLists(list1, list2):
        if list1.next_node is None and list2.next_node is None:
            return list1

        curr_node_1 = list1
        curr_node_2 = list2

        organized_nodes = []

        while True:
            if curr_node_1 is None and curr_node_2 is None:
                break

            if curr_node_1 is None or curr_node_2 is None:
                if curr_node_1 is not None:
                    organized_nodes.append(curr_node_1)

                    curr_node_1 = curr_node_1.next_node
                else:
                    organized_nodes.append(curr_node_2)

                    curr_node_2 = curr_node_2.next_node
            else:
                val_1 = curr_node_1.val
                val_2 = curr_node_2.val

                if val_1 == val_2:
                    organized_nodes.append(curr_node_1)
                    organized_nodes.append(curr_node_2)

                    curr_node_1 = curr_node_1.next_node
                    curr_node_2 = curr_node_2.next_node
                elif val_1 < val_2:
                    organized_nodes.append(curr_node_1)

                    curr_node_1 = curr_node_1.next_node
                else:
                    organized_nodes.append(curr_node_2)

                    curr_node_2 = curr_node_2.next_node

        head = organized_nodes[0]

        for node in range(len(organized_nodes) - 1):
            organized_nodes[node].next = organized_nodes[node + 1]

        return head

    final_sorted = mergeTwoLinkedLists(list_1, list_2)
    curr_node = final_sorted

    while True:
        print(curr_node.val)

        curr_node = curr_node.next

        if curr_node is None:
            break