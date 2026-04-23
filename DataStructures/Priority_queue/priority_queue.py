from DataStructures.List import array_list as al
from DataStructures.Priority_queue import pq_entry as pqe

def default_compare_higher_value(father_node, child_node):
    if pqe.get_priority(father_node) >= pqe.get_priority(child_node):
        return True
    else:
        return False

def default_compare_lower_value(father_node, child_node):
    if pqe.get_priority(father_node) <= pqe.get_priority(child_node):
        return True
    else:
        return False

def new_heap(is_min_pq=True):
    if is_min_pq==False:
        cmp_function=default_compare_higher_value
    else:
        cmp_function=default_compare_lower_value
    return {
        "elements":[None],
        "size":0,
        "cmp_funcion": cmp_function
    }
def swim(my_heap, pos):
    j=pos
    while (j//2)>1:
        if pqe.priority(my_heap, my_heap["elements"][j//2], my_heap["elements"][j]):
            al.exchange(my_heap["elements"], j//2, j)
            pos=j//2
    return my_heap

def insert(my_heap, priority, value):
    nuevo=pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], nuevo)
    pos=(al.size(my_heap["elements"])-1)
    swim(my_heap,pos)
    return my_heap

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    if size(my_heap)<=1:
        return True
    else:
        return False