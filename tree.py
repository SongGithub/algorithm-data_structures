"""implementation of Binary Tree"""


class BinaryTreeNode(object):

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_parent(self):
        return self.parent

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


class BinaryTree(object):
    """implement a binary tree
    Protocol:
    any data has value less than value of its parent node
    will be placed on the left child node. While the ones
    greater, will be placed to the right child node
    """
    def __init__(self):
        self.root = None
        self.tree_depth = int(0)
        self.node_sum = int(0)
        self.traverse_result = []

    def insert(self, data):
        new_node = BinaryTreeNode(data)
        current_node = self.root
        # print('begin inserting : ' + str(data))
        if self.root:
            # Determine left/right side should be chosen for the new node
            fulfill_status = False
            while not fulfill_status:
                if data >= current_node.get_data():

                    if current_node.get_right():
                          # print('move to RIGHT, and dive to next level')
                        current_node = current_node.get_right()
                    else:
                        current_node.right = new_node
                        new_node.set_parent(current_node)
                        fulfill_status = True
                else:
                    if current_node.get_left():
                          # print('move to LEFT, and dive to next level')
                        current_node = current_node.get_left()
                    else:  # empty node slot found
                        current_node.left = new_node
                        new_node.set_parent(current_node)
                        fulfill_status = True
                # 3. verify status on the current node
                  # print('Current parent node = ' + str(current_node.get_data()))
                  # print('Child status: '
                  #     + 'left=' + str(current_node.get_left())
                  #     + ' right=' + str(current_node.get_right()))
                  # print('new child\'s parent node is:' + str(new_node.get_parent()))
        else:
            # print('Building a new tree now, root = ' + str(data))
            self.root = new_node

        # print('Finishing inserting...' + '#' * 30)

    def query_recursive(self, node, data):
        # print ('beginning recursive querying data {}'.format(data))
        found_status = False
        if node:
            if node.get_left():
                self.query_recursive(node.get_left(), data)
            if data == node.get_data():
                found_status = True
                print('Data Entry: {} is FOUND'.format(data))
            if node.get_right():
                self.query_recursive(node.get_right(), data)
        return found_status or True

    def delete(self, data):
        """there are 3 possible scenarios:
        1. the node has no child
            delete the node and mark its parent node that 'node.next = None'
        2. the node has 1 child.
            delete the node and re-connect its parent node with its child node
        3. the node has 2 children
            find the Smallest key in the node's Right sub-tree
            replace the node with the Smallest key
        """
        current_node = self.root
        print('begin deleting data : {} '.format(data) + '#' * 50)
        if self.root:
            # Determine left/right side should be chosen for the new node
            found_status = False
            while not found_status:
                if data == current_node.get_data():
                    parent_node_data = current_node.get_parent().get_data()
                    print('Parent Node is ' + str(parent_node_data))
                    current_node = current_node.get_parent()
                    if data >= parent_node_data:
                        current_node.set_right(None)
                        print ('removing RIGHT')
                    else:
                        current_node.set_left(None)
                        print('removing LEFT')
                    found_status = True
                    break
                elif data > current_node.get_data():
                    if current_node.get_right():
                        # print('move to RIGHT, and dive to next level')
                        current_node = current_node.get_right()
                    else:
                        break  # no existing node larger than the current node.
                else:
                    if current_node.get_left():
                        # print('move to LEFT, and dive to next level')
                        current_node = current_node.get_left()
                    else:
                        break

            if found_status:
                print("The data entry: {} found and deleted ".format(str(data)) + '#' * 30)
                # print('my parent node is ' + str(current_node.get_parent()))
            else:
                print("Attention! The data entry: {} is not found ".format(str(data)) + '#' * 30 + '\n')
            return found_status
        else:
            print("Attention! The data entry: {} is not found because the tree doesn't exist ".format(str(data))
                  + '#' * 30 + '\n')
            return False

    def traverse_inOrder(self, node):
        result = []
        def traverse_inOrder_worker(node):
            """Steps:
            1 Go Left
            2 Process current node
            3 Go right"""
            if node.get_data():
                if node.get_left():
                    traverse_inOrder_worker(node.get_left())
                # result.append(node.get_data())
                result.append(node.get_data())
                if node.get_right():
                    traverse_inOrder_worker(node.get_right())
        traverse_inOrder_worker(node)
        print(result)

if __name__ == '__main__':
    INPUT_LIST = [50, 76, 21, 4, 32, 64, 15, 52, 14, 100, 83, 80, 2, 3, 70, 87]
    b = BinaryTree()
    for i in INPUT_LIST:
        b.insert(i)
    b.traverse_inOrder(b.root)
    b.delete(3)
    print(b.query_recursive(b.root, 4))
    b.traverse_inOrder(b.root)
