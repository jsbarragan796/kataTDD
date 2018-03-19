from unittest import TestCase

__author__ = 'Juan Sebastian Barragan'

from Estadistic import Estadistic

class EstadisticTest(TestCase):
    def test_nElements_stringNElement(self):
        self.assertEqual(Estadistic().elements(" "),[0],"Empty string")
        self.assertEqual(Estadistic().elements(""), [0], "Empty string")
        self.assertEqual(Estadistic().elements("1,1,3,2"), [4], " Four String numbers")
        self.assertEqual(Estadistic().elements("1,1"), [2], " Two String numbers")
        self.assertEqual(Estadistic().elements("1"), [1], " One String numbers")
        self.assertEqual(Estadistic().elements("1,4,6,2,6,32,1"), [7], " Seven String numbers")
    def test_minElement_stringNoneElement(self):
        self.assertEqual(Estadistic().minElement(""),[0, None],"Empty string")
    def test_minElement_stringOneElement(self):
        self.assertEqual(Estadistic().minElement("1"),[1,1],"One String numbers")
        self.assertEqual(Estadistic().minElement("10"), [1, 10], "One String numbers")
    def test_minElement_stringTwoElement(self):
        self.assertEqual(Estadistic().minElement("4,2"),[2,2],"Two String numbers")
        self.assertEqual(Estadistic().minElement("10,1200"), [2, 10], "Two String numbers")

    def test_minElement_stringNElement(self):
        self.assertEqual(Estadistic().minElement("4,2,93,7,24,7,3,12"),[8,2],"n String numbers")
        self.assertEqual(Estadistic().minElement("10,12,892,23591,8"), [5, 8], "Two String numbers")