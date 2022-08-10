import collections


class BinaryTreeNode:

    def __init__(self, data=None, name=None, parent=None, right=None, left=None, next=None):
        self.data = data
        self.name = name
        self.parent = parent
        self.right = right
        self.left = left
        self.next = next

def treverse_inorder(tree: BinaryTreeNode):
    if tree:
        treverse_inorder(tree.left)
        #print(" {} : {} ".format(tree.name, tree.data), end='')
        print(" {} ".format(tree.name), end='')
        treverse_inorder(tree.right)


def right_siblings(tree: BinaryTreeNode):
    def get_depth(node: BinaryTreeNode) -> int:
        depth = 0
        while node.parent:
            depth += 1
            if node.parent.left is node:
                if node.parent.right:
                    break
            node = node.parent
        return depth

    if tree:
        depth = get_depth(tree)
        tmp = tree
        if depth > 0:
            for i in range(depth):
                tmp = tmp.parent

            if not tmp.right:
                tmp = None
            else:
                tmp = tmp.right
                for i in range(depth - 1):
                    if tmp.left:
                        tmp = tmp.left
                    elif tmp.right:
                        tmp = tmp.right
                    else:
                        tmp = None
                        break
        if tree is not tmp:
            tree.next = tmp
        right_siblings(tree.left)
        right_siblings(tree.right)


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
    right_siblings(tree)
    treverse_inorder(tree)



if __name__ == '__main__':
    main()