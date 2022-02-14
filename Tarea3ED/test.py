import function3 as fun
import unittest

class test_main (unittest.TestCase):
    def test_valx(self):
        self.assertEqual(fun.valx(1), "positive")
    def test_valy(self):
        self.assertEqual(fun.valy(-2), "negative")
    def test_findCua(self):
        self.assertEqual(fun.findCua(1, -2), 4)