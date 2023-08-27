def create_an_empty_list():
    return []


def create_a_list():
    # Use the literal constructor to create a list with four elements
    return [1, 2, 3, 4]

def add_element_to_end_of_list(l, element):
    # Use the append() method to add the element to the end of the list
    l.append(element)
    return l

def add_element_to_start_of_list(l, element):
    # Use the insert() method to add the element at the start of the list
    l.insert(0, element)
    return l

def remove_element_from_end_of_list(l):
    # Use the pop() method to remove and return the last element from the list
    if len(l) > 0:
        l.pop()
    return l

def remove_element_from_start_of_list(l):
    # Use the del keyword to remove the first element from the list
    if len(l) > 0:
        del l[0]
    return l

def retrieve_first_element_from_list(l):
    # Use indexing to retrieve the value stored at the first index (index 0)
    if len(l) > 0:
        return l[0]
    return None

def retrieve_element_from_index(l, index):
    # Use indexing to retrieve the value stored at the specified index
    if 0 <= index < len(l):
        return l[index]
    return None

def retrieve_last_element_from_list(l):
    # Use indexing with a negative index to retrieve the last element
    if len(l) > 0:
        return l[-1]
    return None

