class Node():
    def __init__(self, k=None, l=None, r=None):
        self.key = k
        self.left = l
        self.right = r

def creatTree(nodeList):
    if nodeList[0] == None:
        return None
    head = Node(nodeList[0])
    Nodes = [head]
    j = 1
    for node in Nodes:
        if node != None:
            node.left = (Node(nodeList[j]) if nodeList[j] != None else None)
            Nodes.append(node.left)
            j += 1
            if j == len(nodeList):
                return head
            node.right = (Node(nodeList[j]) if nodeList[j] != None else None)
            j += 1
            Nodes.append(node.right)
            if j == len(nodeList):
                return head

def get_depth(root):
    if not root:
        return 0
    left = get_depth(root.left) + 1
    right = get_depth(root.right) + 1
    return max(left, right)


root = None
node_l = [1, 2, 3, 4, 5, None, 6, None, None, 7, 8]
node_l = [3, 9, 20, None, None, 15, 7]
head = creatTree(node_l)
# root = get_tree(root, [1, 2, 3, 4, 5, None, 6, None, None, 7, 8])
print(get_depth(head))
