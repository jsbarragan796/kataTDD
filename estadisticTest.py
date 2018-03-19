from unittest import TestCase

__author__ = 'Juan Sebastian Barragan'

from Estadistic import Estadistic

class EstadisticTest(TestCase):
    def test_nElements_stringVacio(self):
        self.assertEqual(Estadistic().elements(" "),0,"Empty string")
    def test_nElements_stringUnElemento(self):
        self.assertEqual(Estadistic().elements("1"), 1, " One String numbers")
    def test_nElements_stringDosElementos(self):
        self.assertEqual(Estadistic().elements("1,1"), 2, " Two String numbers")
    def test_nElements_stringNElementos(self):
        self.assertEqual(Estadistic().elements("1,1,3,2"), 4, " Four String numbers")
        self.assertEqual(Estadistic().elements("1,1"), 2, " Two String numbers")
        self.assertEqual(Estadistic().elements("1"), 1, " One String numbers")
        self.assertEqual(Estadistic().elements("1,4,6,2,6,32,1"), 7, " Seven String numbers")
