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

current_node = linked_list.head.next
while current_node.next is not None:
    # i = 0
    sorted_len = len(sorted_array)
    print(f'Sorted Len: {sorted_len}')
    if(sorted_len == 0):
        sorted_array.insert(0, current_node)


    for i in range(0, sorted_len(sorted_array)):
        print(f'range idx {i}')
        print(f'{sorted_array[i].value}')
        print(f'{current_node.value}')
        if sorted_array[i].value > current_node.value:
            print(f'if 1: {sorted_array[i].value} > {current_node.value}')
            if sorted_array[i+1] == None | sorted_array[i+1].value < current_node.value:
                if sorted_array[i+1] == None:
                    print(f'if 2: {sorted_array[i+1]} is none')
                else:
                    print(f'if 2: {sorted_array[i+1]} > {current_node.value}')

                sorted_array.insert(i+1)
                print('Inserted')
            # i = i + 1
        else:
            # i = i + 1
            print(f'new index: {i}')

    current_node = current_node.next    
    nodes = nodes + 1

print(f'nodes: {nodes}')