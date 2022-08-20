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





if __name__ == '__main__':
    main()