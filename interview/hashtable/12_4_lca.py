class BinaryTreeNode:
    def __init__(self, data=None, name=None, parent=None, right=None, left=None):
        self.data = data
        self.name = name
        self.parent = parent
        self.right = right
        self.left = left

    def __str__(self):
        return self.__repr__()


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


def lac(node1: BinaryTreeNode, node2: BinaryTreeNode):
    iter1, iter2 = node1, node2

    path_to_root = set()
    while iter1 or iter2:
        if iter1:
            if iter1 in path_to_root:
                return iter1
            path_to_root.add(iter1)
            iter1 = iter1.parent
        if iter2:
            if iter2 in path_to_root:
                return iter2
            path_to_root.add(iter2)
            iter2 = iter2.parent
    return False





def main():
    tree = generate_tree_1()
    print(lac(tree.left.left.left, tree.left.right.left) )
    print(lac(tree.left.left.left, tree.left.left.right).name)
    print(lac(tree.left.left.left, tree.right.left.right.left.right).name)





if __name__ == '__main__':
    main()