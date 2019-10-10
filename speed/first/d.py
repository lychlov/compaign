# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     PreOrder
   Description :
   Author :       Lychlov
   date：          2018/8/21
-------------------------------------------------
   Change Activity:
                   2018/8/21:
-------------------------------------------------
"""


class Node(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 前序遍历（递归）
def pre_deep_func(root):
    if root is None:
        return
    print(root.value)  # print 放到下一行 就是中序遍历，放到最后 就是后序遍历
    pre_deep_func(root.left)
    pre_deep_func(root.right)


# 前序遍历（根左右）:模拟压栈过程
# 入栈之前读（根、左），这样出栈时再读右（也是右结点子节点们的根）
def pre_deep_func2(root):
    a = []
    while a or root:
        while root:
            print(root.value)
            a.append(root)
            root = root.left
        h = a.pop()
        root = h.right


# 中序遍历（左根右）:模拟压栈过程
# 出栈之后读（左、根），这样出栈后指针变更再读右
def mid_deep_func2(root):
    a = []
    while a or root:
        while root:
            a.append(root)
            root = root.left
        h = a.pop()
        print(h.value)
        root = h.right


# 后序遍历（左右根）:模拟逆序(根右左)存入数组b，然后再数组b逆序输出
# (根右左)与(根左右)类似，入栈a前读（根、右），出栈后指针变更再读左
def after_deep_func2(root):
    a = []
    b = []
    while a or root:
        while root:
            b.append(root.value)
            a.append(root)
            root = root.right
        h = a.pop()
        root = h.left
    print
    b[::-1]


def level_func(root):
    a = []
    a.append(root)
    while a:
        head = a.pop(0)
        print
        head.value
        if head.left:
            a.append(head.left)
        if head.right:
            a.append(head.right)


def get_level_func1(root):
    a = []
    b = []
    a.append(root)
    b.append(1)
    while a:
        head = a.pop(0)
        p = b.pop(0)
        if head.left:
            a.append(head.left)
            b.append(p + 1)
        if head.right:
            b.append(p + 1)
            a.append(head.right)
    return p


def get_level_func2(root):
    if not root:
        return 0
    left = right = 0
    left = get_level_func2(root.left)
    right = get_level_func2(root.right)
    return max(left, right) + 1


def get_tree(post, mid):
    if len(post) == 0:
        return None
    if len(post) == 1:
        return Node(post[-1])
    root = Node(post[-1])
    root_index = mid.index(post[-1])
    root.left = get_tree(post[0:root_index], mid[:root_index])
    root.right = get_tree(post[root_index:-1], mid[root_index + 1:])
    return root


# head = get_tree([1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10], [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7])
# pre_deep_fuhead)

def get_after_deep(pre, mid, a):
    if len(pre) == 1:
        a.append(pre[0])
        return
    if len(pre) == 0:
        return
    root = pre[0]
    root_index = mid.index(root)
    get_after_deep(pre[1:root_index + 1], mid[:root_index], a)
    get_after_deep(pre[root_index + 1:], mid[root_index + 1:], a)
    a.append(root)
    return a


def get_rear(node, rear_list=[]):
    if node is None:
        return None
    get_rear(node.left, rear_list)
    get_rear(node.right, rear_list)
    rear_list.append(node.value)
    return rear_list

def widthOfBinaryTree( root):
    """
    :type root: TreeNode
    :rtype: int
    """

    def dfs(root, x, y, num, dmin, dmax):
        if root:
            left = dfs(root.left, x - 1, y + 1, num * 2, dmin, dmax)
            right = dfs(root.right, x + 1, y + 1, 1 + num * 2, dmin, dmax)
            dmin[y] = min(num, dmin.get(y, float("inf")))
            dmax[y] = max(num, dmax.get(y, float("-inf")))
            return max(left or 0, right or 0, 1 + dmax[y] - dmin[y])

    return dfs(root, 0, 0, 1, {}, {})


# res = get_after_deep([1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10], [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7], [])
# res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]


if __name__ == '__main__':
    in_file = open('widthoftree.txt', 'r')
    out_file = open('4-width-answer.txt', 'w')
    for line in in_file.readlines():
        line = line.strip()
        mid_ord = line.split(';')[0].split(',')
        post_ord = line.split(';')[1].split(',')
        root = None
        root = get_tree(post_ord,mid_ord)
        res = widthOfBinaryTree(root)
        out_file.write(str(res)+'\r\n')
    pass
