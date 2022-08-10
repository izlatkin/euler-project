class BinaryTreeNode:
    # def __int__(self, data=None, name=None, left=None, right=None):
    #     self.data = data
    #     self.name = name
    #     self.right = right
    #     self.left = left

    def __init__(self, data=None, name=None, right=None, left=None):
        self.data = data
        self.name = name
        self.right = right
        self.left = left


def treverse_inorder(tree: BinaryTreeNode):
    if tree:
        treverse_inorder(tree.left)
        #print(" {} : {} ".format(tree.name, tree.data), end='')
        print(" {} ".format(tree.name), end='')
        treverse_inorder(tree.right)

def treverse_inorder_without_recursion(tree: BinaryTreeNode):
    result = []
    progress = [(tree, False)]
    while progress:
        node, left_tree_traversed = progress.pop()
        if node:
            if left_tree_traversed:
                result.append(node.name)
            else:
                progress.append((node.right, False))
                progress.append((node, True))
                progress.append((node.left, False))

    print("  ".join([str(r) for r in result]))


def treverse_preorder(tree: BinaryTreeNode):
    if tree:
        print(" {} ".format(tree.name), end='')
        treverse_preorder(tree.left)
        treverse_preorder(tree.right)


def treverse_preorder_without_recursion(tree: BinaryTreeNode):
    result = []
    progress = [tree]
    while progress:
        node = progress.pop()
        if node:
            progress.append(node.right)
            progress.append(node.left)
            result.append(node.name)

    print("  ".join([str(r) for r in result]))


def treverse_postorder(tree: BinaryTreeNode):
    if tree:
        treverse_postorder(tree.left)
        treverse_postorder(tree.right)
        print(" {} ".format(tree.name), end='')


def treverse_postorder_without_recursion(tree: BinaryTreeNode):
    result = []
    progress = [(tree, False)]
    while progress:
        node, left_tree_traversed = progress.pop()
        if node:
            if left_tree_traversed:
                result.append(node.name)
            else:
                progress.append((node, True))
                progress.append((node.right, False))
                progress.append((node.left, False))

    print("  ".join([str(r) for r in result]))


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def check_balance(tree):
        if not tree:
            return True, -1

        left_result, left_height = check_balance(tree.left)
        if not left_result:
            return left_result, left_height

        right_result, right_height = check_balance(tree.right)
        if not right_result:
            return right_result, right_height

        if abs(left_height - right_height) > 1:
            return False, max(right_height, left_height) + 1
        else:
            return True, max(right_height, left_height) + 1

    result, h = check_balance(tree)
    return result



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


def generate_tree_2():
    tree = BinaryTreeNode(314, 'A')
    tree.left = BinaryTreeNode(6, 'B')
    tree.right = BinaryTreeNode(6, 'I')

    tree.left.left = BinaryTreeNode(271, 'C')
    tree.left.right = BinaryTreeNode(561, 'F')

    tree.left.left.left = BinaryTreeNode(28, 'D')
    tree.left.left.right = BinaryTreeNode(0, 'E')

    tree.left.right.right = BinaryTreeNode(3, 'G')
    tree.left.right.left = BinaryTreeNode(17, 'H')

    tree.right.left = BinaryTreeNode(2, 'J')
    tree.right.right = BinaryTreeNode(271, 'O')

    tree.right.left.right = BinaryTreeNode(1, 'K')

    tree.right.left.right.left = BinaryTreeNode(401, 'L')
    tree.right.left.right.right = BinaryTreeNode(257, 'N')

    tree.right.left.left = BinaryTreeNode(641, 'M')

    tree.right.right.right = BinaryTreeNode(28, 'P')
    tree.right.right.left = BinaryTreeNode(33, 'P')
    return tree


def main():
    tree =generate_tree_1()
    treverse_inorder(tree)
    print()
    treverse_inorder_without_recursion(tree)
    treverse_preorder(tree)
    print()
    treverse_preorder_without_recursion(tree)
    treverse_postorder(tree)
    print()
    treverse_postorder_without_recursion(tree)
    print(is_balanced_binary_tree(tree))

    tree = generate_tree_2()
    print(is_balanced_binary_tree(tree))


if __name__ == '__main__':
    main()