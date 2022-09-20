import collections


class BstNode:

    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __print__(self):
        if self.left:
            self.left.__print__()
        print(self.data, end=' ')
        if self.right:
            self.right.__print__()

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


def find_k_largerst(tree: BstNode, k: int) -> list[int]:
    def k_largests_helper(tree):
        if tree and len(k_largest) < k:
            k_largests_helper(tree.right)
            if len(k_largest) < k:
                k_largest.append(tree.data)
                k_largests_helper(tree.left)

    k_largest = []
    k_largests_helper(tree)
    return k_largest

def lca_old(tree: BstNode, node1: BstNode, node2: BstNode) -> BstNode:
    Status = collections.namedtuple('Status', ('num_targets_nodes', 'ancestor'))

    def lca_helper(tree: BstNode, node1: BstNode, node2: BstNode):
        if tree is None:
            return Status(num_targets_nodes=0, ancestor=None)

        left_result = lca_helper(tree.left, node1, node2)
        if left_result.num_targets_nodes == 2:
            return left_result

        right_result = lca_helper(tree.right, node1, node2)
        if right_result.num_targets_nodes == 2:
            return right_result

        num_target_nodes = left_result.num_targets_nodes + right_result.num_targets_nodes + \
                           (node1, node2).count(tree)

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helper(tree, node1, node2).ancestor


def find_lca(tree: BstNode, a: int, b: int) -> BstNode:
    subtree = tree
    a, b = min(a, b), max(a, b)
    while not (a < subtree.data < b):
        if subtree.data < a:
            subtree = subtree.right
        else:
            subtree = subtree.left
    return subtree


def rebuild_bst_from_preorder(preorder: list[int]) -> BstNode:  # example [40, 20, 10, 30, 80, 70, 60, 75, 90]
    if not preorder:
        return None

    if len(preorder) == 1:
        return BstNode(preorder[0])

    transite_point = 1
    for i, p in enumerate(preorder):
        if p > preorder[0]:
            transite_point = i
            break
    left = preorder[1:transite_point]
    right = preorder[transite_point:]
    return BstNode(preorder[0], rebuild_bst_from_preorder(left), rebuild_bst_from_preorder(right))


def generate_tee1():
    tree = BstNode(19)
    l = BstNode(2)
    r = BstNode(5)
    ll = BstNode(3, l, r)
    l = BstNode(13)
    rr = BstNode(17, l)
    rrr = BstNode(11)
    rrr.right = rr
    lll = BstNode(7, ll, rrr)
    tree.left = lll

    right =  BstNode(43, BstNode(23, None, BstNode(37, BstNode(29, None, BstNode(31)), BstNode(41))), BstNode(47, None, BstNode(53)))
    tree.right = right

    return tree


def main():
    salaries = [90, 30, 100, 40, 20]
    tree = generate_tee1()
    tree.__print__()
    print(tree.__is_binary__())
    print(find_first_greater_then_k(tree, 23))
    print(find_k_largerst(tree, 1))
    print(find_k_largerst(tree, 10))
    print(lca_old(tree, tree.left, tree.right).data)
    print(find_lca(tree, 11, 53).data)
    print(find_lca(tree, 5, 11).data)

    print("rebuild from preorder")
    tmp = rebuild_bst_from_preorder([40, 20, 10, 30, 80, 70, 60, 75, 90])
    tmp.__print__()
    #print(tmp.__print__())





if __name__ == '__main__':
    main()