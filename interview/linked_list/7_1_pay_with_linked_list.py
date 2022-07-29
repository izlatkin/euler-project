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


def delete_note(note_to_delete: LinkedNode):
    note_to_delete.data = note_to_delete.next.data
    note_to_delete.next = note_to_delete.next.next


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


def revirse(L1: LinkedNode) -> LinkedNode:
    prev, curr = None, L1
    while curr:
        prev, curr.next, curr = curr, prev, curr.next
    return prev


# slow did x iterations. x = before_cycle_start + [0,1)* cycle
# fast did 2x iterations. 2x = before_cycle_start +
def has_cycle(L1: LinkedNode) -> bool:
    def len_cycle(catch_node: LinkedNode):
        count = 1
        end = catch_node
        start = catch_node.next
        while True:
            if start is end:
                return count
            start = start.next
            count += 1

    slow, fast = L1, L1
    count = 0
    cycle_len = 0
    while fast and fast.next:
        count += 1
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            cycle_len = len_cycle(slow)
            break
    if cycle_len != 0:
        cycle_start = L1
        for _ in range(0, count - cycle_len):
            cycle_start = cycle_start.next
        return cycle_start
    return False


def lists_overloap(L1: LinkedNode, L2: LinkedNode) -> LinkedNode:
    def len_of_list(L: LinkedNode, till=None):
        count = 0
        while L and L is not till:
            count += 1
            L = L.next
        return count

    def adjust(L: LinkedNode, n: int) -> LinkedNode:
        for _ in range(0, n):
            L = L.next
        return L

    loop_l1, loop_l2 = has_cycle(L1), has_cycle(L2)
    if (not loop_l1 and loop_l2) or (not loop_l2 and loop_l1):
        return None

    if loop_l1 and loop_l2:
        len_L1, len_L2 = len_of_list(L1, loop_l1), len_of_list(L2, loop_l2)

        if len_L1 > len_L2:
            L1 = adjust(L1, len_L1 - len_L2)
        if len_L1 < len_L2:
            L2 = adjust(L2, len_L2 - len_L1)

        # case when list overloap before loop
        while L1 is not loop_l1 or L2 is not loop_l2:
            if L1 is L2:
                return L1
            L1, L2 = L1.next, L2.next

        # case when list overloap after loop
        tmp = loop_l1.next
        while tmp is not loop_l1:
            if tmp is loop_l2:
                return tmp
            tmp = tmp.next
        return None

    if not loop_l1 and not loop_l2:
        len_L1, len_L2 = len_of_list(L1), len_of_list(L2)

        if len_L1 > len_L2:
            L1 = adjust(L1, len_L1 - len_L2)
        if len_L1 < len_L2:
            L2 = adjust(L2, len_L2 - len_L1)

        while L1 or L2:
            if L1 is L2:
                return L1
            L1, L2 = L1.next, L2.next
        return None


def remove_duplicates(L: LinkedNode):
    while L.next:
        if L.data == L.next.data:
            L.next = L.next.next
        else:
            L = L.next


def cyclic_right_shift(L1: LinkedNode, k: int):
    def len_of_list(L: LinkedNode):
        count = 0
        while L:
            count += 1
            L = L.next
        return count
    k = k % len_of_list(L1)

    new_head, new_tail = L1, L1
    for _ in range(0, k - 1):
        new_head = new_head.next
        new_tail = new_tail.next
    new_head = new_head.next
    save = new_head
    new_tail.next = None
    while new_head.next:
        new_head = new_head.next
    new_head.next = L1
    return save


def even_odd(L: LinkedNode) -> (LinkedNode, LinkedNode):
    if not L:
        return None, None

    odd, even = L, L.next
    head_odd, head_even = L, L.next

    while even.next:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = None

    return head_odd, head_even



def palindromic_list(L: LinkedNode) -> bool:
    def len_of_list(L: LinkedNode):
        count = 0
        while L:
            count += 1
            L = L.next
        return count

    n = len_of_list(L)
    second_part = L
    for _ in range(n // 2 - 1):
        second_part = second_part.next

    cut = second_part
    second_part = second_part.next
    cut.next = None
    L.__print__()
    second_part.__print__()
    second_part = revirse(second_part)
    second_part.__print__()
    while L and second_part:
        if L.data != second_part.data:
            return False
        L = L.next
        second_part = second_part.next
    return True


def add_list_base(L1: LinkedNode, L2: LinkedNode) -> LinkedNode:
    to_return = head = LinkedNode()
    carry = 0
    while L1 or L2 or carry > 0:
        val = carry + (L1.data if L1 else 0) + (L2.data if L2 else 0)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        to_return.next = LinkedNode(val % 10)
        carry = val // 10
        to_return = to_return.next
    return head.next



def main():
    a = [1,2,7,8,10]
    l1 = LinkedNode()
    l1.__add__(a)
    l1.__print__()
    b = [3, 7, 7, 9, 11]
    l2 = LinkedNode()
    l2.__add__(b)
    l2.__print__()

    l3 = merge_two_sorted_lists(l1, l2)
    l3.__print__()
    delete_note(l3.next.next)
    l3.__print__()

    l4 = revirse(l3)
    l4.__print__()

    l_with_cycle = l4
    l4.next.next.next.next.next.next.next.next = l4
    #l4.__print__()
    print(has_cycle(l4))
    print(has_cycle(l3))
    print(has_cycle(l1))

    l5 = LinkedNode()
    l5.__add__(a)
    c = [3, 7, 7, 9, 11, 12, 17]
    l6 = LinkedNode()
    l6.__add__(c)
    l6.next.next.next = l5.next.next
    print(lists_overloap(l5, l6))

    l7 = LinkedNode()
    l7.__add__(a)
    c = [3, 7, 7, 9, 11, 12, 17]
    l8 = LinkedNode()
    l8.__add__(c)
    print(lists_overloap(l7, l8))

    cc = [1, 1, 1, 2, 2, 2, 7, 8, 10, 10, 10]
    l1 = LinkedNode()
    l1.__add__(cc)
    remove_duplicates(l1)
    l1.__print__()

    cc = [1, 1, 1, 2, 2, 2, 7, 8, 10, 10, 10]
    l1 = LinkedNode()
    l1.__add__(cc)
    l1.__print__()
    l1 = cyclic_right_shift(l1, 2)
    l1.__print__()

    dd = [k for k in range(100)]
    l1 = LinkedNode()
    l1.__add__(dd)
    s1, s2 = even_odd(l1)
    s1.__print__()
    s2.__print__()


    dd = [max(k, 99 - k) for k in range(100)]
    l1 = LinkedNode()
    l1.__add__(dd)
    print(palindromic_list(l1))

    dd = [k + 1 for k in range(4)]
    l1 = LinkedNode()
    l1.__add__(dd)
    l2 = LinkedNode()
    l2.__add__(dd)
    l_result = add_list_base(l1, l2)
    l_result.__print__()



if __name__ == '__main__':
    main()