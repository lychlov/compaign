pre = [1, 2, 4, 5, 7, 8, 3, 6]
mid = [4, 2, 7, 5, 8, 1, 3, 6]
test_tree = None


class Node():
    def __init__(self, k=None, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r


post = [4, 7, 8, 5, 2, 6, 3, 1]
mid = [4, 2, 7, 5, 8, 1, 3, 6]


def get_tree_with_post_mid(post, mid):
    if len(post) > 0:
        root = Node(k=post[-1])
        root_index = mid.index(root.key)
        root.left = get_tree_with_post_mid(post[:root_index], mid[:root_index])
        root.right = get_tree_with_post_mid(post[root_index:-1], mid[root_index + 1:])
        return root
    else:
        return None


test_tree = get_tree_with_post_mid(post, mid)
# print(post_order(test_tree))
