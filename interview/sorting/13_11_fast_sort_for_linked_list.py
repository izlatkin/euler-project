class LinkedNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __add__(self, l: list):
        if not l:
            return
        tmp = self
        self.data = l[0]
        for element in l[1:]:
            tmp.next = LinkedNode(element)
            tmp = tmp.next

    def __print__(self):
        tmp = self
        while tmp:
            print("{} ".format(tmp.data), end='')
            tmp = tmp.next
        print()


def merge_two_sorted_lists(L1: LinkedNode, L2: LinkedNode) -> LinkedNode:
    dummy_head = tail = LinkedNode()
    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    tail.next = L1 or L2
    return dummy_head.next


def fast_sort(L: LinkedNode):
    if L is None or L.next is None:
        return L

    pre_slow, slow, fast = None, L, L
    while fast and fast.next:
        pre_slow = slow
        slow = slow.next
        fast = fast.next.next

    if pre_slow:
        pre_slow.next = None

    return merge_two_sorted_lists(fast_sort(L), fast_sort(slow))

def main():
    a = [20, 1, 11, 2, 7, 8, 10]
    l1 = LinkedNode()
    l1.__add__(a)
    l1.__print__()
    fast_sort(l1).__print__()


if __name__ == '__main__':
    main()