from typing import List
from LinkedListUtils import *

snake_segments = 25
linked_list = generate_full_node_snake(snake_segments)
# output_snake(linked_list)

def insert_sorted(node: Node):
    for i in range(1, sorted_array.__len__):
        if sorted_array[i] > linked_list.head.value:
            if sorted_array[i+1] < linked_list.head.value:
                sorted_array.insert(i+1)
                break


sorted_array = []

nodes = 1

current_node = linked_list.head
while current_node.next is not None:
    current_node = current_node.next    
    sorted_len = len(sorted_array)
    print(f'Sorted Len: {sorted_len}')
    if(sorted_len == 0):
        sorted_array.insert(0, current_node)


    for i in range(0, sorted_len):
        print(f'range idx {i} of {sorted_len} | Sorted: {sorted_array[i].value} | Current: {current_node.value}')
        if sorted_array[i].value > current_node.value:
            if((i + 1) == sorted_len):
                sorted_array.append(current_node)
                current_node = current_node.next
                print(f'breaking - node {nodes}: i = [{i}], {sorted_len}, {current_node.value}')
                break

            if sorted_array[i+1].value < current_node.value:
                print(f'if 2: {sorted_array[i+1]} > {current_node.value}')
                sorted_array.insert(i+1, current_node)
                print('Inserted')
            # i = i + 1
        else:
            # i = i + 1
            print(f'new index: {i}')

    nodes = nodes + 1

print(f'nodes: {nodes}')