
def stooge_sort(array, l=0, h=None):
    if h is None:
        h = len(array) - 1
    if l >= h:
        return
    if array[l] > array[h]:
        array[l], array[h] = array[h], array[l]
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        stooge_sort(array, l, h - t)
        stooge_sort(array, l + t, h)
        stooge_sort(array, l, h - t)
    return array
