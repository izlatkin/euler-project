import typing

import bintrees

class BstNode:

    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __print__(self):
        if self.left:
            self.left.__print__()
        print(self.data, end=' ')
        if self.right:
            self.right.__print__()

    def __add__value__(self, k: int):
        tmp = self
        if tmp.data == k:
            pass
        elif tmp.data > k:
            if tmp.left:
                tmp.left.__add__value__(k)
            else:
                tmp.left = BstNode(k)
        else:
            if tmp.right:
                tmp.right.__add__value__(k)
            else:
                tmp.right = BstNode(k)

    def __is_binary__(self):
        left_range = -float('inf')
        right_range = float('inf')
        def are_keys_in_range(node, low_range, upper_range):
            if not node:
                return True
            elif not low_range <= node.data <= upper_range: #and (left_range != float('inf') and upper_range != float('inf')):
                return False
            else:
                return are_keys_in_range(node.left, low_range, node.data) and \
                       are_keys_in_range(node.right, node.data, upper_range)

        return are_keys_in_range(self, left_range, right_range)




def build_min_height_bst_from_sorted_array(A: list[int]):
    def build_min_height_bst_from_sorted_subarray(start, end):
        if start >= end:
            return None
        mid = (start + end) // 2
        return BstNode(A[mid],
                       build_min_height_bst_from_sorted_subarray(start, mid),
                       build_min_height_bst_from_sorted_subarray(mid + 1, end))

    return build_min_height_bst_from_sorted_subarray(0, len(A))

def find_closest_elements_in_sorted_arrays(sorted_arrays: list[list[int]]) -> int:

    # Stores array iterators in each entry.
    iters = bintrees.RBTree()
    for idx, sorted_array in enumerate(sorted_arrays):
        it = iter(sorted_array)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)

    min_distance_so_far = float('inf')
    while True:
        min_value, min_idx = iters.min_key()
        max_value = iters.max_key()[0]
        min_distance_so_far = min(max_value - min_value, min_distance_so_far)
        it = iters.pop_min()[1]
        next_min = next(it, None)
        # Return if some array has no remaining elements.
        if next_min is None:
            return typing.cast(int, min_distance_so_far)
        iters.insert((next_min, min_idx), it)

def find_first_greater_then_k(tree: BstNode, k: int) -> BstNode:
    result = float('inf')
    subtree = tree
    while subtree:
        if subtree.data > k:
            result = min(subtree.data, result)
            subtree = subtree.left
        else:
            subtree = subtree.right
    return result


def find_first_smaller_then_k(tree: BstNode, k: int) -> BstNode:
    result = float('-inf')
    subtree = tree
    while subtree:
        if subtree.data < k:
            result = max(subtree.data, result)
            subtree = subtree.right
        else:
            subtree = subtree.left
    return result


def is_in_tree(tree: BstNode, element: int):
    subtree = tree
    while subtree:
        if subtree.data == element:
            return True
        elif subtree.data > element:
            subtree = subtree.left
        else:
            subtree = subtree.right
    return False


def find_closest_elements_in_sorted_arrays_2(a1, a2, a3) -> int:
    tree2 = BstNode(a2[0])
    for a in a2[1:]:
        tree2.__add__value__(a)
    tree2.__print__()
    tree3 = BstNode(a3[0])
    for a in a3[1:]:
        tree3.__add__value__(a)
    tree3.__print__()
    min_distance = float('inf')
    print()
    for a in a1:
        tree = None
        if is_in_tree(tree2, a) and is_in_tree(tree3, a):
            return 0
        if is_in_tree(tree2, a):
            tree = tree3
        if is_in_tree(tree3, a):
            tree = tree2
        if tree:
            close_min, close_max = find_first_smaller_then_k(tree, a), find_first_greater_then_k(tree, a)
            min_distance = min(a - close_min, close_max - a, min_distance)
        else:
            from_tree_2 = [find_first_smaller_then_k(tree2, a), find_first_greater_then_k(tree2, a)]
            from_tree_3 = [find_first_smaller_then_k(tree3, a), find_first_greater_then_k(tree3, a)]
            tmp_min_distance = min([max(a, x, y) - min(a, x, y) for x in from_tree_2 for y in from_tree_3])
            min_distance = min(min_distance, tmp_min_distance)

    return min_distance



def main():
    salaries = [90, 30, 100, 40, 20]
    print(find_closest_elements_in_sorted_arrays([[5, 10, 15], [3, 6, 9, 12, 15], [8, 16, 24]]))
    print()
    print(find_closest_elements_in_sorted_arrays_2([10, 5, 15], [9,3, 6, 12, 15], [16,8, 24]))






if __name__ == '__main__':
    main()