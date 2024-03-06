import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next: None|Node = None
        self.reference = random.randrange(-99_444, 23_952)

class LinkedList:
    def __init__(self, head: Node|None):
        self.head = head

def generate_node(n: int) -> Node:
    return Node(n)

def generate_full_node_snake(n: int) -> LinkedList:
    previous_segment: Node = None
    for i in range(n):
        segment = generate_node(i)
        segment.next = previous_segment
        previous_segment = segment

    head_node: Node = generate_node(n)
    head_node.next = previous_segment
    return LinkedList(head_node)

def output_snake(linked_list: LinkedList) -> None:
    if (linked_list.head == None):
        print('Ayyyy this shit empty as fuck, GERRREHHFUCKOURRAAAHHEEEREEE YA SCAMP')
        return
    idx = 0
    current_node: Node = linked_list.head
    while current_node.next != None:
        print(f'Node [{idx}] | Value [{current_node.value}] | Ref [{current_node.reference}] | Memory Location: {hex(id(current_node))}')
        current_node = current_node.next
        idx += 1
