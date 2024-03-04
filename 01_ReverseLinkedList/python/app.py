import random

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head: Node):
        self.head = head





n = 4

def generate_node() -> Node:
    return Node(random.randrange(-570, 1100))

def generate_full_node_snake() -> LinkedList:
    segment_count: int = 0
    previous_segment: Node = None

    while segment_count < n:
        segment = generate_node()
        segment.next = previous_segment
        segment_count += 1

    head_node: Node = generate_node()
    head_node.next = previous_segment

    return LinkedList(head_node)

def run():
    list: LinkedList = generate_full_node_snake()

    