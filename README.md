# CS162Python-Project4c
# project-4c

Modify insertion sort to sorts a list of strings instead of numbers.  It shouldn't return anything.  The sorting should ignore case.  For example "Zebra" should come after "apple",  "maRker" should come after "marble",  etc.  Name this function string_sort.  The resulting list should contain the exact same strings as the original list, but in sorted order.

The file must be named: **string_sort.py**

def insertion_sort(a_list):    
  """    
  Sorts a_list in ascending order    
  """    
  for index in range(1, len(a_list)):        
    value = a_list[index]        
    pos = index - 1        
    while pos >= 0 and a_list[pos] > value:            
      a_list[pos + 1] = a_list[pos]            
      pos -= 1        
    a_list[pos + 1] = value
