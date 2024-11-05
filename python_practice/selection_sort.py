"""
Selection Sort: Repeatedly check the list for the minimum and move it to the sorted front section and add it in order
"""
def selection_sort(list: list):
  print(list)
  # Empty list? Early return.
  # if len(list) == 0:
  #   return

  # We're placing the items in sorted order at the beginning of the list.
  # So we'll need to know at what index the unsorted elements begin (and therefore we know where the sorted elements are to the left of this)
  unsortedStartIndex = 0

  while (unsortedStartIndex < len(list)):
    # 1. Find smallest item's index
    indexOfMin = unsortedStartIndex
    for i in range(unsortedStartIndex, len(list)):
      item = list[i]
      if item < list[indexOfMin]:
        indexOfMin = i
    
    # 2. Move min to sorted section at beginning of list. Place in sorted order.
    min = list.pop(indexOfMin)
    list.insert(unsortedStartIndex, min)

    # 3. Increase unsortedStartIndex after each iteration
    unsortedStartIndex += 1
  

    

    


# Not selection sort. Misunderstood the algorithm.
# def selection_sort(list: list):
#   print(list)
#   # For each index in list
#   for i in range(0, len(list) - 1):
#     j = i + 1

#     # Compare current and next values (i and j)
#     print('before:', i , j, list[i], list[j])
#     if list[i] <= list[j]:
#       continue
#     else:
#       temp = list[i]
#       list[i] = list[j]
#       list[j] = temp
#     print('after:', list[i], list[j])