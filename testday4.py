from unittest import TestCase
from day4 import zerohunt

class zerosTestCase(TestCase):
    def test_1(self):
        self.assertEqual(zerohunt([9,99,4,0,1,3,4]),[9,99,4,1,3,4,0])
    def test_2_end_zeros(self):
        self.assertEqual(zerohunt([1,2,3,4,5,0,0,0]),[1,2,3,4,5,0,0,0])
    def test_3_empty(self):
        self.assertEqual(zerohunt([]),[])
    def test_4_no_zeros(self):
        self.assertEqual(zerohunt([4,5,6,7,8,9,1,2]),[4,5,6,7,8,9,1,2])
    def test_5_only_zeros(self):
        self.assertEqual(zerohunt([0,0,0,0,0]),[0,0,0,0,0])
    def test_6_middle_zeros(self):
        self.assertEqual(zerohunt([40,22,33,1,0,0,0,3,4]),[40,22,33,1,3,4,0,0,0])
