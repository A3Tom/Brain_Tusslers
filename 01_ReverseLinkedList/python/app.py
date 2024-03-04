import random
import uuid

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.reference = random.randrange(1_000_000, 10_000_000)

class LinkedList:
    def __init__(self, head: Node|None):
        self.head = head



heap: dict[str, Node] = {}
n = 4


def generate_node() -> Node:
    return Node(random.randrange(-999_999, 999_999))

def generate_full_node_snake() -> LinkedList:
    previous_segment: Node = None
    for _ in range(n):
        segment = generate_node()
        segment.next = previous_segment
        previous_segment = segment

    head_node: Node = generate_node()
    head_node.next = previous_segment

    print(f"Head node value: {head_node.value}")
    return LinkedList(head_node)

def run():
    list: LinkedList = generate_full_node_snake()
    current_node: Node = list.head
    idx = 0
    print(f"Current node value: {current_node.value}")
    print(f"Next node value: {current_node.next}")
    while current_node.next != None:
        print(f'Node [{idx}] | Value [{current_node.value}]')
        current_node = current_node.next
        idx += 1

print("Starting")
run()
print("Exiting")