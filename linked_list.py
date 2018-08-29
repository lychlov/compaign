from builtins import input


class LinkNode(object):
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next_node = next_node


def create_linked_list(link_node=None):
    node_data = input()
    temp_node = None
    while node_data != 'exit':
        if link_node is None:
            link_node = LinkNode(data=node_data)
            temp_node = link_node
        else:
            temp_node.next_node = LinkNode(data=node_data)

            temp_node = temp_node.next_node
        node_data = input('输入数据')
    return link_node


if __name__ == '__main__':
    print('开启链表')
    linked = create_linked_list()
    print(linked)
