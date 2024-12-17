from scipy.constants import value
from sympy import false


class Node:
    def __init__(self, value, parent=None):
        self._parent = parent
        self._left = None
        self._right = None
        self._value = value
        self._quantity = 1

    def __repr__(self):
        if self._left is None and self._right is None:
            return f'{self._value}'
        return f'{self._value}({self._left}, {self._right})'

    def __eq__(self, other):
        return self._value ==other

    def __gt__(self, other):
        return self._value > other
    def __lt__(self, other):
        return self._value < other
    def __le__(self, other):
        return self._value <= other
    def __ge__(self, other):
        return self._value >= other

    class Tree:
        def __init__(self, iterable=()):
            self._root = None
            for value in iterable:
                self.insert(value)

        def insert(self, value):
            if self._root is None:
                self._root = Node(value)
            else:
                self._root.insert(value)

        def B_iterB_(self):

            if self._root:
                yield from self._root.traverse()

        def reverse(self):

            if self._root:
                yield from self._root.reverse_traverse()

        def B_containsB_(self, value):

            if self._root:
                return self._root.contains(value)
            return False

        def __contains__(self, value):

            return self.B_containsB_(value)

        def B_reprB_(self):

            if self._root:
                return f"Tree({self._root})"
            return "Empty Tree"


    def insert(self, value):
        if value < self:
            if self._left is None:
                self._left = Node(value, self)
            self._left.insert(value)
        elif value > self:
            if self._right is None:
                self._right = Node(value, self)
            self._right.insert(value)
        elif value:
            self._quantity = self._quantity+1


root = Node(5)
root._left = Node(4, parent=root)
root._right = Node(6, parent=root)
print(root)


def bubble_sort(data: list, reverse=False):
    n = len(data)
    for i in range(n):
        swapped = False
        for k in range(n-1-i):
            if data[k+1] < data[k]:
                data[k], data[k + 1] = data[k + 1], data[k]
                swapped = True
        if not swapped:
            break
    return data


def merge(left, right, reverse=False):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if (left[i] < right[j] and not reverse) or (left[i] > right[j] and reverse):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining elements from both lists
    result.extend(left[i:])
    result.extend(right[j:])
    return result


data = [1, 4, 5, 6, 2, 4, 7, 4, 2]


def merge_sort(data):
    if len(data) <= 1:
        return data

    # Find the middle point to divide the list
    mid = len(data) // 2

    # Recursively call merge_sort to sort the left half
    left = merge_sort(data[:mid])

    # Recursively call merge_sort to sort the right half
    right = merge_sort(data[mid:])

    # Merge the two sorted halves
    return merge(left, right)


merge_sort(data)


def bisect_search(sorted_data: list, value) -> int:
    low, high = 0, len(sorted_data) - 1

    while low <= high:
        mid = (low + high) // 2  # Find the middle index
        mid_value = sorted_data[mid]

        if mid_value == value:  # Value found
            return mid
        elif mid_value < value:  # Value is in the right half
            low = mid + 1
        else:  # Value is in the left half
            high = mid - 1

    return -1  # Value not found

