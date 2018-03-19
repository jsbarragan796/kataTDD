from unittest import TestCase

__author__ = 'Juan Sebastian Barragan'

import Estadistic

class EstadisticTest(TestCase):
    def test_nElements(self):
        self.assertEqual(Estadistic().elements(" "),0,"Empty string")
