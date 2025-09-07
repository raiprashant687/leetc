# single linked list into circular list


class Node(object):

    def __init__(self, data,next=None):
        self.data = data
        self.next = next


class LinkedList(object):

    def __init__(self):
        self.head = None

    def append(self,data):
        node = Node(data)
        current = self.head
        if current is None:
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

    def display(self):
        current = self.head
        while current.next is not None:
            print(current.data,end="-->")
            current = current.next
        print(current.data)

    def make_circle(self):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = self.head

    def reverse(self):
        current = self.head
        prev = None
        next_node = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def detect_cycle(self):
        current = self.head
        dict1 = dict()
        dict1[self.head] = 1
        while current is not None:
            if current.next not in dict1:
                dict1[current.next] = 1
            else:
                current.next = None



def sort_linked_list(linked_list1,linked_list2):
    # list1 = []
    # current1 = linked_list1.head
    # while current1 is not None:
    #     list1.append(current1.data)
    #     current1 = current1.next
    # current2 = linked_list2.head
    # while current2 is not None:
    #     list1.append(current2.data)
    #     current2 = current2.next
    # print(list1)
    # list1.sort()
    # print(list1)
    # merged_list1 = LinkedList()
    # for item in list1:
    #     merged_list1.append(item)
    result = LinkedList()
    while linked_list1 and linked_list2:
        if linked_list1.value < linked_list2.value:
            result.next = linked_list1
            linked_list1 = linked_list1.next
        else:
            result.next = linked_list2
            linked_list2 = linked_list2.next
        result = result.next
        if linked_list1:
            result.next = linked_list1
        if linked_list2:
            result.next = linked_list2

    return result








x=LinkedList()
x.append(1)
x.append(2)
x.append(3)
x.append(4)


c=LinkedList()
c.append(3)
c.append(5)
c.append(9)
sort_linked_list(x,c)