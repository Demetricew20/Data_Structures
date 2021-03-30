from node import *


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend_node(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            #Original node is pushed over
            node.next = self.head
            #New node is placed in front
            self.head = node

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def contains(self, item):
        while self.head is not None:
            if self.head.data == item:
                return True
            else:
                #check next node data
                self.head = self.head.next
        return False


linked_list = LinkedList()
linked_list.append_node(60)
linked_list.append_node(70)
linked_list.append_node(80)
linked_list.prepend_node(40)
linked_list.contains(70)


