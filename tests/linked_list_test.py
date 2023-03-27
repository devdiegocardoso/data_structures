import os
import sys
import unittest

from pprint import pprint
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from implementation.linked_list import List

class TestLinkedList(unittest.TestCase):
    def test_add_single(self):
        lista = List()
        lista.add(1)
        self.assertEqual(lista.get_list(),"1","Value was not added correctly.")
    def test_add(self):
        lista = List()
        lista.add(1)
        lista.add(2)
        self.assertEqual(lista.get_list(),"1 -> 2","Value was not added correctly.")
    def test_remove_begin(self):
        lista = List()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(1)
        self.assertEqual(lista.get_list(),"2 -> 3","Value was not removed correctly.")
    def test_remove_middle(self):
        lista = List()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(2)
        self.assertEqual(lista.get_list(),"1 -> 3","Value was not removed correctly.")
    def test_remove_end(self):
        lista = List()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(3)
        self.assertEqual(lista.get_list(),"1 -> 2","Value was not removed correctly.")
    def test_remove_nonexistent(self):
        lista = List()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(4)
        self.assertEqual(lista.get_list(),"1 -> 2 -> 3","Value must not be removed.")

if __name__ == '__main__':
    unittest.main()