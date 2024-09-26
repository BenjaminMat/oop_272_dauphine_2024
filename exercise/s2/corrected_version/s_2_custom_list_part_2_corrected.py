import unittest
"""
**Instructions:**

In this practical exercise, you will extend the `List` class that we created earlier by adding dunder 
(double underscore) methods to implement basic operations. This will help you understand how these special methods 
allow objects to behave like native Python types.

Your task is to add the following dunder methods to this class:

- `__str__(self)`: Returns a string representation of the list.
- `__len__(self)`: Returns the length of the list.
- `__add__(self, other)`: Allows the addition of two lists (concatenation).
- `__getitem__(self, index)`: Allows access to elements by index (e.g., `my_list[2]`).
- `__setitem__(self, index, value)`: Allows modifying an element by index (e.g., `my_list[2] = 10`).
- `__iter__(self)`: Allows iteration over the list.


By implementing these methods, you will enable your `List` class to behave like a native Python list, allowing for 
intuitive operations and interactions.
"""

class List:
    def __init__(self):
        self._elements = {}
        self._count = 0

    def append(self, element):
        self._elements[self._count] = element
        self._count += 1

    def remove(self, value):
        for index, element in self._elements.items():
            if element == value:
                del self._elements[index]
                self._count -= 1
                for i in range(index, self._count):
                    self._elements[i] = self._elements.pop(i + 1)
                break

    def pop(self, index):
        if index < 0 or index >= self._count:
            raise IndexError("Index out of range")
        element = self._elements.pop(index)
        self._count -= 1
        for i in range(index, self._count):
            self._elements[i] = self._elements.pop(i + 1)
        return element

    def get_index(self, value):
        for index, element in self._elements.items():
            if element == value:
                return index
        return -1

    def __str__(self):
        # Returns a string representation of the list
        return str([self._elements[i] for i in range(self._count)])

    def __len__(self):
        # Returns the length of the list
        return self._count

    def __getitem__(self, index):
        # Allows access to elements by index (e.g., my_list[2])
        if index < 0 or index >= self._count:
            raise IndexError("Index out of range")
        return self._elements[index]

    def __setitem__(self, index, value):
        # Allows modifying an element by index (e.g., my_list[2] = 10)
        if index < 0 or index >= self._count:
            raise IndexError("Index out of range")
        self._elements[index] = value

    def __add__(self, other):
        # Allows adding two lists (concatenation)
        if not isinstance(other, List):
            raise TypeError("The operand must be an instance of List")
        new_list = List()
        for i in range(self._count):
            new_list.append(self._elements[i])
        for i in range(other._count):
            new_list.append(other._elements[i])
        return new_list

    def __iter__(self):
        # Allows iteration over the list
        for i in range(self._count):
            yield self._elements[i]

class TestListDunder(unittest.TestCase):
    def setUp(self):
        self.list = List()
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

    def test_str(self):
        self.assertEqual(str(self.list), "[1, 2, 3]")

    def test_len(self):
        self.assertEqual(len(self.list), 3)

    def test_getitem(self):
        self.assertEqual(self.list[1], 2)
        with self.assertRaises(IndexError):
            _ = self.list[3]

    def test_setitem(self):
        self.list[1] = 5
        self.assertEqual(self.list[1], 5)
        with self.assertRaises(IndexError):
            self.list[3] = 4

    def test_iter(self):
        self.assertEqual(list(self.list), [1, 2, 3])

    def test_add(self):
        other = List()
        other.append(4)
        other.append(5)
        result = self.list + other
        self.assertEqual(str(result), "[1, 2, 3, 4, 5]")

def run_tests():
    unittest.main(argv=[''], verbosity=2, exit=False)

if __name__ == '__main__':
    run_tests()