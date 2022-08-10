import collections


class BinaryTreeNode:

    def __init__(self, data=None, name=None, right=None, left=None):
        self.data = data
        self.name = name
        self.right = right
        self.left = left


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



def generate_tree_1():
    tree = BinaryTreeNode(314, 'A')
    tree.left = BinaryTreeNode(6, 'B')
    tree.right = BinaryTreeNode(6, 'I')

    tree.left.left = BinaryTreeNode(271, 'C')
    tree.left.right = BinaryTreeNode(561, 'F')

    tree.left.left.left = BinaryTreeNode(28, 'D')
    tree.left.left.right = BinaryTreeNode(0, 'E')

    tree.left.right.right = BinaryTreeNode(3, 'G')
    tree.left.right.right.left = BinaryTreeNode(17, 'H')

    tree.right.left = BinaryTreeNode(2, 'J')
    tree.right.right = BinaryTreeNode(271, 'O')

    tree.right.left.right = BinaryTreeNode(1, 'K')

    tree.right.left.right.left = BinaryTreeNode(401, 'L')
    tree.right.left.right.right = BinaryTreeNode(257, 'N')

    tree.right.left.right.left.right = BinaryTreeNode(641, 'M')

    tree.right.right.right = BinaryTreeNode(28, 'P')
    return tree



def main():
    tree = generate_tree_1()
    print(lca(tree, tree.left.left.left, tree.left.right.right.left).name)

    print(lca(tree, tree.left.left.left, tree.right.right.right).name)

    print(lca(tree, tree.right.left.right.right, tree.right.left.right.left.right).name)


if __name__ == '__main__':
    main()