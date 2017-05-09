"""this module contains basic data structures to be called"""


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, value):
        self.value = value

    def set_next(self, next):
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def append_item(self, value):
        """append an item on the 2nd position of the LinkedList,
         only if there was a head. Otherwise, insert as a head.

         Actions if there was a head for the list:
         1. get the head's next
         2. re-set the head's next to the new node
         """
        new_node = Node(value)  # init a new Node obj

        if self.head:
            new_node.set_next(self.head.get_next())  # set new node's next = head node's next
            self.head.set_next(new_node)  # step2
        else:
            self.head = new_node

    def get_item(self, index):
        node = self.head
        if self.head:
            for i in range(index):
                node = node.get_next()
            return node.get_value()
        else:
            print ('head is not there so I can\'t get anything')
            return 0

    def set_item(self, index, item):
        # self.head:
        try:
            node = self.head
            for i in range(index):
                node = node.get_next()
            return node.set_value(item)

        except AttributeError as err:
            print('ERROR: head is not there, so that I can\'t set the value. \n'
                  'Detailed reason' + str(err.message) + '\n')
            return 1

    def count_items(self):
        node = self.head
        size = int(0)
        while node:
            size += 1
            node = node.get_next()
        # print('num of items: ' + str(size))
        return size

    def print_items(self):
        node = self.head
        if node:
            print ('\nprinting items in the list:')
            while node:
                print(node.get_value())
                node = node.get_next()
            print ('#' * 30)
        else:
            print ('\nList is empty. There is nothing to print!')

if __name__ == '__main__':
    llist = LinkedList()
    llist.append_item(1)
    llist.append_item(2)
    llist.append_item(5)
    llist.set_item(0, 7)
    print('getting item: ' + str(llist.get_item(1)))
    llist.print_items()
