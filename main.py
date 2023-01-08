from app.bubble_sort import bubble_sort
from app.selection_sort import selection_sort
from app.insertion_sort import insertion_sort
from app.merge_sort import merge_sort
from app.quick_sort import quick_sort
from app.heap_sort import heap_sort
from app.counting_sort import counting_sort
from app.bucket_sort import bucket_sort
from app.shell_sort import shell_sort
from app.comb_sort import comb_sort
from app.cycle_sort import cycle_sort
from app.pancake_sort import pancake_sort
from app.gnome_sort import gnome_sort
from app.stooge_sort import stooge_sort
from app.pigeonhole_sort import pigeonhole_sort
from app.oddeven_sort import oddeven_sort
from app.cocktail_sort import cocktail_sort

unsorted_list = [5, 3, 8, 6, 7, 2, 1, 4, 9, 0, 5, 3, 8, 6, 7, 2, 1, 4, 9, 0, 2, 5, 7, 1, 0]

print("unsorted list: ", unsorted_list)

print("***** Bubble Sort *****")
print("sorted list: ", bubble_sort(unsorted_list.copy()))

print("***** Selection Sort *****")
print("sorted list: ", selection_sort(unsorted_list.copy()))

print("***** Insertion Sort *****")
print("sorted list: ", insertion_sort(unsorted_list.copy()))

print("***** Merge Sort *****")
print("sorted list: ", merge_sort(unsorted_list.copy()))

print("***** Quick Sort *****")
print("sorted list: ", quick_sort(unsorted_list.copy()))

print("***** Heap Sort *****")
print("sorted list: ", heap_sort(unsorted_list.copy()))

print("***** Counting Sort *****")
print("sorted list: ", counting_sort(unsorted_list.copy()))

print("***** Bucket Sort *****")
print("sorted list: ", bucket_sort(unsorted_list.copy()))

print("***** Shell Sort *****")
print("sorted list: ", shell_sort(unsorted_list.copy()))

print("***** Comb Sort *****")
print("sorted list: ", comb_sort(unsorted_list.copy()))

print("***** Cycle Sort *****")
print("sorted list: ", cycle_sort(unsorted_list.copy()))

print("***** Pancake Sort *****")
print("sorted list: ", pancake_sort(unsorted_list.copy()))

print("***** Gnome Sort *****")
print("sorted list: ", gnome_sort(unsorted_list.copy()))

print("***** Stooge Sort *****")
print("sorted list: ", stooge_sort(unsorted_list.copy()))

print("***** Pigeonhole Sort *****")
print("sorted list: ", pigeonhole_sort(unsorted_list.copy()))

print("***** Odd-Even Sort *****")
print("sorted list: ", oddeven_sort(unsorted_list.copy()))

print("***** Cocktail Sort *****")
print("sorted list: ", cocktail_sort(unsorted_list.copy()))
