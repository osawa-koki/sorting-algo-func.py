
def strand_sort(array):
    sorted_array = []
    while array:
        min_element = min(array)
        sorted_array.append(min_element)
        array.remove(min_element)
    return sorted_array
