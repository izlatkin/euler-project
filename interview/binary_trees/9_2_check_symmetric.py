class BinaryTreeNode:

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

def treverse_preorder(tree: BinaryTreeNode):
    if tree:
        print(" {} ".format(tree.name), end='')
        treverse_preorder(tree.left)
        treverse_preorder(tree.right)

def treverse_postorder(tree: BinaryTreeNode):
    if tree:
        treverse_postorder(tree.left)
        treverse_postorder(tree.right)
        print(" {} ".format(tree.name), end='')


def is_symmetric(tree: BinaryTreeNode):
    def check_symmetric(subtree1: BinaryTreeNode, subtree2: BinaryTreeNode):
        if not subtree1 and not subtree2:
            return True
        elif subtree1 and subtree2:
            return subtree1.data == subtree2.data and check_symmetric(subtree1.left, subtree2.right) \
                   and check_symmetric(subtree1.right, subtree2.left)
        return False


    return not tree or check_symmetric(tree.left, tree.right)


def generate_tree_symmetric():
    tree = BinaryTreeNode(314, 'A')
    tree.left = BinaryTreeNode(6, 'B')
    tree.right = BinaryTreeNode(6, 'E')

    tree.left.right = BinaryTreeNode(2, 'C')
    tree.left.right.right = BinaryTreeNode(3, 'D')

    tree.right.left = BinaryTreeNode(2, 'F')
    tree.right.left.left = BinaryTreeNode(3, 'G')

    return tree


def generate_tree_assymmetric_1():
    tree = BinaryTreeNode(314, 'A')
    tree.left = BinaryTreeNode(6, 'B')
    tree.right = BinaryTreeNode(6, 'E')

    tree.left.right = BinaryTreeNode(2, 'C')
    tree.left.right.right = BinaryTreeNode(3, 'D')

    tree.right.left = BinaryTreeNode(2, 'F')
    tree.right.left.left = BinaryTreeNode(4, 'G')

    return tree


def generate_tree_assymmetric_2():
    tree = BinaryTreeNode(314, 'A')
    tree.left = BinaryTreeNode(6, 'B')
    tree.right = BinaryTreeNode(6, 'E')

    tree.left.right = BinaryTreeNode(2, 'C')

    tree.right.left = BinaryTreeNode(2, 'F')
    tree.right.left.left = BinaryTreeNode(4, 'G')

    return tree



def main():
    tree = generate_tree_symmetric()
    treverse_inorder(tree)
    print()
    print(is_symmetric(tree))

    tree = generate_tree_assymmetric_1()
    treverse_inorder(tree)
    print()
    print(is_symmetric(tree))

    tree = generate_tree_assymmetric_2()
    treverse_inorder(tree)
    print()
    print(is_symmetric(tree))



if __name__ == '__main__':
    main()