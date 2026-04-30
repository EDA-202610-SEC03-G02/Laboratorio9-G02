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
    
def priority(my_heap, partent, child):
    return my_heap["cmp_funcion"](partent, child)    

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
    j = pos
    while j // 2 >= 1:
        padre = my_heap["elements"][j // 2]
        hijo  = my_heap["elements"][j]
        if not priority(my_heap, padre, hijo):  # padre NO tiene prioridad → subir hijo
            al.exchange(my_heap["elements"], j // 2, j)
            j = j // 2
        else:
            break
    return my_heap

def sink(my_heap, pos):
    j=pos
    while (2*j)<size(my_heap["elements"]):
        
        if (2*j)+1<size(my_heap["elements"]):
            
            if priority(my_heap, my_heap["elements"][2*j], my_heap["elements"][(2*j)+1]):
                j=(2*j)+1
            else:
                j=2*j
        else:
            j=2*j
        if priority(my_heap, my_heap["elements"][pos], my_heap["elements"][j]):
            al.exchange(my_heap["elements"], pos, j)
            pos=j
        else:
            break
    return my_heap

def insert(my_heap, priority, value):
    nuevo=pqe.new_pq_entry(priority, value)
    al.add_last(my_heap["elements"], nuevo)
    pos=(size(my_heap["elements"])-1)
    swim(my_heap,pos)
    return my_heap

def size(my_heap):
    return my_heap["size"]

def is_empty(my_heap):
    return size(my_heap)==0

def remove(my_heap):
    if is_empty(my_heap):
        return None
    else:
        al.exchange(my_heap["elements"], 1, (size(my_heap["elements"])-1))
        eliminado=my_heap["elements"].pop()
        sink(my_heap, 1)
        return eliminado

def get_first_priority(my_heap):
    if is_empty(my_heap):
        return None
    else:
        return pqe.get_priority(my_heap["elements"][1])

def is_present_value(my_heap, value):
    for i in range(1, size(my_heap["elements"])):
        if pqe.get_value(my_heap["elements"][i])==value:
            return i
    return -1

def improve_priority(my_heap, priority, value):
    
    pos=is_present_value(my_heap, value)
    if pos==-1:
        return None
    else:
        pqe.set_priority(my_heap["elements"][pos], priority)
        swim(my_heap, pos)
        return my_heap