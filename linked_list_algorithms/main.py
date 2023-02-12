class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


def print_list_recursively(head: Node):

    if head is None:
        print()
        return

    print(head.val, end=" ")
    print_list_recursively(head.next)


def sum_recursively(head: Node) -> int:

    if head is None:
        return 0

    total = 0
    total += head.val

    return total + sum_recursively(head.next)


def reverse_list(head: Node):
    prev_node = None

    current = head
    while current:
        # Save next node pointer
        next_node = current.next
        # Redefine next pointer for the current node
        current.next = prev_node

        # Iterate through the list
        prev_node = current
        current = next_node

    return prev_node


# print_list_recursively(a)
# print(sum_recursively(a))

reversed_head = reverse_list(a)
print_list_recursively(reversed_head)
