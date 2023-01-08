from app.bubble_sort import bubble_sort
from app.selection_sort import selection_sort
from app.insertion_sort import insertion_sort
from app.merge_sort import merge_sort

unsorted_list = [5, 3, 8, 6, 7, 2, 1, 4, 9, 0, 5, 3, 8, 6, 7, 2, 1, 4, 9, 0, 2, 5, 7, 1, 0]

print("unsorted list: ", unsorted_list)

print("***** Bubble Sort *****")
print("sorted list: ", bubble_sort(unsorted_list))

print("***** Selection Sort *****")
print("sorted list: ", selection_sort(unsorted_list))

print("***** Insertion Sort *****")
print("sorted list: ", insertion_sort(unsorted_list))

print("***** Merge Sort *****")
print("sorted list: ", merge_sort(unsorted_list))
