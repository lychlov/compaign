class Node(object):
    def __init__(self, value=None, left=-1, right=-1, father=-1):
        self.value = value
        self.left = left
        self.right = right
        self.father = father


def preorder(root, post_str=[]):  # 前序遍历
    if root is None:
        return
    else:
        post_str.append(root.value)
        preorder(root.left)
        preorder(root.right)
        return post_str


def inorder(root, post_str=[]):  # 中序遍历
    if root is None:
        return
    else:
        inorder(root.left)
        post_str.append(root.value)
        inorder(root.right)
        return post_str


def postorder(root, post_str=[]):  # 后序遍历
    if root is None:
        return
    else:
        postorder(root.left, post_str)
        postorder(root.right, post_str)
        post_str.append(root.value)
        return post_str


def get_tree(root, values):
    if len(values) > 0:
        a = values.pop(0)
        if a is '#':
            root = None
        else:
            root = Node(value=a)
            root.left = get_tree(root.left, values)
            root.right = get_tree(root.right, values)
        return root
    else:
        return None


if __name__ == '__main__':
    with open(r'/Users/zhikuncheng/devspace/0828/05/in.txt', 'r') as in_str:
        with open(r'/Users/zhikuncheng/devspace/0828/05/out.txt', 'w', encoding='utf-8') as out_file:
            for tree_str in in_str.readlines():
                tree_str = tree_str.strip()
                root = None
                str_list = list(tree_str)
                root = get_tree(root, str_list)
                post = postorder(root)
                pre = preorder(root)
                ino = inorder(root)