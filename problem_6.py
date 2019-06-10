class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def create_set(linklist):
    set1 = set()
    node = linklist.head
    while node:
        set1.add(node.value)
        node = node.next
    return set1


def union(llist_1, llist_2):
    # Your Solution Here
    un_set = create_set(llist_1).union(create_set(llist_2))
    union_list = LinkedList()
    for el in un_set:
        union_list.append(el)
    return union_list


def intersection(llist_1, llist_2):
    # Your Solution Here
    set1 = create_set(llist_1)
    set2 = create_set(llist_2)

    inter = set1.intersection(set2)
    inter_list = LinkedList()
    for el in inter:
        inter_list.append(el)
    return inter_list


# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("Case 1")
print("Union")
print(union(linked_list_1, linked_list_2)) # 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> 
print("Intersection")
print(intersection(linked_list_1, linked_list_2)) # 4 -> 21 -> 6 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("Case 2")
print("Union")
print(union(linked_list_3, linked_list_4)) # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> 
print("Intersection")
print(intersection(linked_list_3, linked_list_4)) # empty

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_3 = [3, 2, 4, 35, 12, 65, 6, 4, 23]
element_4 = []

for i in element_3:
    linked_list_5.append(i)

for i in element_4:
    linked_list_6.append(i)

print("Case 2")
print("Union")
print(union(linked_list_5, linked_list_6)) # 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 12 -> 23 ->
print("Intersection")
print(intersection(linked_list_5, linked_list_6)) # empty

# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_5 = []
element_6 = []

for i in element_5:
    linked_list_7.append(i)

for i in element_6:
    linked_list_8.append(i)

print("Case 3")
print("Union")
print(union(linked_list_7, linked_list_8)) # empty
print("Intersection")
print(intersection(linked_list_7, linked_list_8)) # empty