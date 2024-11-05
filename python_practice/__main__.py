#! /usr/bin/env python3

"""
This is the main file.
"""

from LinkedList import SinglyLinkedList
from sequences import crud
from selection_sort import selection_sort


def main():
    # LinkedList Usage
    # singly = SinglyLinkedList()
    # singly.add('a')
    # singly.print()
    # singly.add('b')
    # singly.print()
    # singly.add('c')
    # singly.print()
    # singly.print()  # Output: a -> b -> c -> None
    # # singly.delete_last()
    # # singly.print()  # Output: a -> b -> None
    # print(singly.is_empty())  # Output: False
    # print(len(singly))  # Output: 3

    # Sequences Practice (crud operations ig...)
    # crud()

    # Selection Sort
    # Run Time: 
    # Memory Usage: 
    # sample_list = [3, 2, 1]
    sample_list = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    selection_sort(sample_list)
    

if __name__ == "__main__":
    main()
