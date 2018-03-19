from unittest import TestCase

__author__ = 'Juan Sebastian Barragan'

from Estadistic import Estadistic

class EstadisticTest(TestCase):

    def test_minMaxElement_stringTwoElement(self):
        self.assertEqual(Estadistic().minMaxPromElement(" "), [0, None, None, None], "Empty string")
        self.assertEqual(Estadistic().minMaxPromElement(""), [0, None, None, None], "Empty string")
#        self.assertEqual(Estadistic().minMaxElement("1"), [1, 1, 1], "One String numbers")
#        self.assertEqual(Estadistic().minMaxElement("10"), [1, 10, 10], "One String numbers")
#        self.assertEqual(Estadistic().minMaxElement("4,2"),[2,2,4],"Two String numbers")
#        self.assertEqual(Estadistic().minMaxElement("10,1200"), [2, 10,1200], "Two String numbers")
#        self.assertEqual(Estadistic().minMaxElement("4,2,93,7,24,7,3,12"),[8, 2, 93],"n String numbers")
#        self.assertEqual(Estadistic().minMaxElement("10,12,892,23591,8"), [5, 8, 23591], "n String numbers")