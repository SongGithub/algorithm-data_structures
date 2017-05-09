"""implementation of queue and stack from scratch"""
from linked_list import *


class Queue(LinkedList):
    """FIFO"""

    def push(self, value):
        """insert item from the Left side"""
        new_node = Node(value)
        print('pushing value : ' + str(value))
        # print (self.head, new_node.get_value())
        if self.head:
            # tmp_node = self.head
            new_node.set_next(self.head)  # set new node's next = head node's next
            self.head = new_node  # assign the new node as the Head node
        else:
            self.head = new_node

    def pop_item(self):
        """pop item from the Right side"""
        node = self.head
        popped_value = int(0)
        item_count = self.count_items()
        print ('start popping ops, item count = ' + str(item_count))

        if item_count == 0:
            print('\nbut there is none in the list')
            return None

        elif item_count == 1:
            print('POPPING_ITEM: there is only ONE item left in the list!')
            popped_value = node.get_value()
            self.head = None

        elif item_count == 2:
            print('POPPING_ITEM: there is only TWO item left in the list!')
            node_tail = node.get_next()
            node_head = node
            node = node.get_next()
            popped_value = node.get_value()
            node_head.set_next(None)

        elif item_count > 2:
            for i in range(item_count - 2):
                node_2nd_last = node.get_next()
                node = node.get_next()

            node = node.get_next()
            popped_value = node.get_value()  # retrieve value from
            node_2nd_last.set_next(None)  # del
        print ('popped value = ' + str(popped_value))
        return popped_value


class Stack(Queue):
    """LIFO"""
    def push(self, value):
        """insert item fro the Right side"""
        new_node = Node(value)
        print('pushing value to the Tail : ' + str(value))
        if self.head:
            node = self.head
            while node.get_next():
                node = node.get_next()
            node.set_next(new_node)
        else:
            self.head = new_node

if __name__ == '__main__':
    print('\n' + '#' * 30 + 'Starting Queue ' + '#' * 30)
    q = Queue()
    q.push(123)
    q.set_item(0, 111)
    q.push(456)
    q.push(789)
    q.push(101112)
    q.print_items()
    q.pop_item()

    q.print_items()
    q.pop_item()

    q.print_items()
    q.pop_item()
    q.print_items()
    q.pop_item()
    q.pop_item()
    print('\n' + '#' * 30 + 'Starting Stack ' + '#' * 30 )
    stack = Stack()
    stack.push(123)
    stack.push(456)
    stack.push(789)
    stack.push(101112)
    stack.print_items()
    stack.pop_item()

    stack.print_items()
    stack.pop_item()

    stack.print_items()
    stack.pop_item()
    stack.print_items()
    stack.pop_item()
    stack.pop_item()