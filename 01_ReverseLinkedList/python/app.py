import random
import uuid

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.reference = random.randrange(0, 1_000)

class LinkedList:
    def __init__(self, head: Node|None):
        self.head = head

    def reverse(self):
        current_node: Node = self.head.next
        
        prev_node: Node = self.head
        prev_node.next = None

        while current_node.next:
            fw_node: Node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = fw_node
        
        self.head = current_node
        self.head.next = prev_node



heap: dict[str, Node] = {}
n = 4


def generate_node(n: int) -> Node:
    return Node(n)

def generate_full_node_snake() -> LinkedList:
    previous_segment: Node = None
    for i in range(n):
        segment = generate_node(i)
        segment.next = previous_segment
        previous_segment = segment

    head_node: Node = generate_node(n)
    head_node.next = previous_segment

    return LinkedList(head_node)

def output_snake(linked_list: LinkedList) -> None:
    idx = 0
    current_node: Node = linked_list.head
    while current_node.next != None:
        print(f'Node [{idx}] | Value [{current_node.value}] | Ref [{current_node.reference}]')
        current_node = current_node.next
        idx += 1
    
    print(f'Node [{idx}] | Value [{current_node.value}] | Ref [{current_node.reference}]')

def run():
    linked_list: LinkedList = generate_full_node_snake()
    print("In Order:")
    output_snake(linked_list)

    print("Reversed:")
    linked_list.reverse()
    output_snake(linked_list)

print("Starting")
run()
print("Exiting")