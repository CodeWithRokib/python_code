class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_middle(head: ListNode) -> ListNode:
    if not head:
        return None

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def print_list(head: ListNode):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()


# Example usage
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print_list(head)
    middle = find_middle(head)
    print("Middle Element:", middle.val)
