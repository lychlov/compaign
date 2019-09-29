#!/usr/bin/python


class node():
    def __init__(self, k=None, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r


def create(root):
    a = input('enter a key:')
    if a is '#':
        root = None
    else:
        root = node(k=a)
        root.left = create(root.left)
        root.right = create(root.right)
    return root


def preorder(root):  # 前序遍历
    if root is None:
        return
    else:
        print(root.key)
        preorder(root.left)
        preorder(root.right)


def inorder(root):  # 中序遍历
    if root is None:
        return
    else:
        inorder(root.left)
        print(root.key)
        inorder(root.right)


def postorder(root):  # 后序遍历
    if root is None:
        return
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.key)


root = None  # 测试代码
root = create(root)
preorder(root)
inorder(root)
postorder(root)
