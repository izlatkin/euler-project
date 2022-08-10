import collections


class BinaryTreeNode:

    def __init__(self, data=None, name=None, parent=None, right=None, left=None):
        self.data = data
        self.name = name
        self.parent = parent
        self.right = right
        self.left = left


def traverse_with_constant_space(tree: BinaryTreeNode) -> None:
    prev = None
    result = []
    while tree:
        if prev is tree.parent or not prev:
            prev = tree
            if tree.left:
                tree = tree.left
            elif tree.right:
                result.append(tree.name)
                tree = tree.right
            else:
                result.append(tree.name)
                tree = tree.parent
        elif prev is tree.left:
            result.append(tree.name)
            prev = tree
            if tree.right:
                tree = tree.right
            elif tree.parent:
                tree = tree.parent
        elif prev is tree.right:
            prev = tree
            tree = tree.parent


    print("  ".join([str(r) for r in result]))



def lca(tree: BinaryTreeNode, node1: BinaryTreeNode, node2: BinaryTreeNode) -> BinaryTreeNode:
    Status = collections.namedtuple('Status', ('num_targets_nodes', 'ancestor'))

    def lca_helper(tree: BinaryTreeNode, node1: BinaryTreeNode, node2: BinaryTreeNode):
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


def lca_parents(tree: BinaryTreeNode, node1: BinaryTreeNode, node2: BinaryTreeNode) -> BinaryTreeNode:
    def depth(node: BinaryTreeNode) -> int:
        d = 0
        while node.parent:
            d += 1
            node = node.parent
        return d

    d1, d2 = depth(node1), depth(node2)

    if d1 < d2:
        node1, node2 = node2, node1
        for i in range(d2 - d1):
            node1 = node1.parent

    while node1 and node2:
        if node1 is node2:
            return node1
        node1, node2 = node1.parent, node2.parent
    return tree


def find_successor(tree: BinaryTreeNode):
    if tree.right:
        tree = tree.right
        while tree.left:
            tree = tree.left
        return tree

    while tree.parent and tree.parent.right is tree:
        tree = tree.parent
    return tree.parent


def generate_tree_1():
    tree = BinaryTreeNode(314, 'A')
    tree.left = BinaryTreeNode(6, 'B', tree)
    tree.right = BinaryTreeNode(6, 'I', tree)

    tree.left.left = BinaryTreeNode(271, 'C', tree.left)
    tree.left.right = BinaryTreeNode(561, 'F', tree.left)

    tree.left.left.left = BinaryTreeNode(28, 'D', tree.left.left)
    tree.left.left.right = BinaryTreeNode(0, 'E', tree.left.left)

    tree.left.right.right = BinaryTreeNode(3, 'G', tree.left.right)
    tree.left.right.right.left = BinaryTreeNode(17, 'H', tree.left.right.right)

    tree.right.left = BinaryTreeNode(2, 'J', tree.right)
    tree.right.right = BinaryTreeNode(271, 'O', tree.right)

    tree.right.left.right = BinaryTreeNode(1, 'K', tree.right.left)

    tree.right.left.right.left = BinaryTreeNode(401, 'L', tree.right.left.right)
    tree.right.left.right.right = BinaryTreeNode(257, 'N', tree.right.left.right)

    tree.right.left.right.left.right = BinaryTreeNode(641, 'M', tree.right.left.right.left)

    tree.right.right.right = BinaryTreeNode(28, 'P', tree.right.right)
    return tree



def main():
    tree = generate_tree_1()
    print(lca(tree, tree.left.left.left, tree.left.right.right.left).name)
    print(lca_parents(tree, tree.left.left.left, tree.left.right.right.left).name)

    print(lca(tree, tree.left.left.left, tree.right.right.right).name)
    print(lca_parents(tree, tree.left.left.left, tree.right.right.right).name)

    print(lca(tree, tree.right.left.right.right, tree.right.left.right.left.right).name)
    print(lca_parents(tree, tree.right.left.right.right, tree.right.left.right.left.right).name)

    print(find_successor(tree).name)
    print(find_successor(tree.left.right.right.left).name)
    print(find_successor(tree.left.right.right).name)

    traverse_with_constant_space(tree)


if __name__ == '__main__':
    main()