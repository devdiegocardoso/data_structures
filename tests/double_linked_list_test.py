import os
import sys
import unittest

from pprint import pprint
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from implementation.double_linked_list import DList

class TestLinkedList(unittest.TestCase):
    def test_add_single(self):
        lista = DList()
        lista.add(1)
        self.assertEqual(lista.iterate_forward(),"1","Nao adicionou corretamente")
    def test_add(self):
        lista = DList()
        lista.add(1)
        lista.add(2)
        self.assertEqual(lista.iterate_forward(),"1 -> 2","Nao adicionou corretamente")
    def test_remove_begin(self):
        lista = DList()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(1)
        self.assertEqual(lista.iterate_forward(),"2 -> 3","Nao removeu corretamente")
    def test_remove_middle(self):
        lista = DList()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(2)
        self.assertEqual(lista.iterate_forward(),"1 -> 3","Nao removeu corretamente")
    def test_remove_end(self):
        lista = DList()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(3)
        self.assertEqual(lista.iterate_forward(),"1 -> 2","Nao removeu corretamente")
    def test_remove_nonexistent(self):
        lista = DList()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.remove(4)
        self.assertEqual(lista.iterate_forward(),"1 -> 2 -> 3","Nao removeu corretamente")
    def test_iterate_backward(self):
        lista = DList()
        lista.add(1)
        lista.add(2)
        lista.add(3)
        lista.add(4)
        self.assertEqual(lista.iterate_backward(),"4 -> 3 -> 2 -> 1","Nao removeu corretamente")
    def test_add_start_end(self):
        lista = DList()
        lista.add(1)
        lista.add(2,type=1)
        lista.add(3,type=1)
        lista.add(4)
        self.assertEqual(lista.iterate_forward(),"3 -> 2 -> 1 -> 4","Nao removeu corretamente")

if __name__ == '__main__':
    unittest.main()