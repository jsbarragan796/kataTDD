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
