#!/usr/bin/env  python3

import unittest

from fft import fft
from fft import coefficient



class TestRepeat(unittest.TestCase):
    def test1(self):
        self.assertEqual(list(coefficient(8, 1)), [1, 0, -1, 0, 1, 0, -1, 0])


    def test2(self):
        self.assertEqual(list(coefficient(8, 2)), [0, 1, 1, 0, 0, -1, -1, 0])


    def test3(self):
        self.assertEqual(list(coefficient(8, 3)), [0, 0, 1, 1, 1, 0, 0, 0])




class TestFFT(unittest.TestCase):
    def test0_1(self):
        self.assertEqual(fft('12345678', 1), '48226158')


    def test0_2(self):
        self.assertEqual(fft('12345678', 2), '34040438')


    def test0_3(self):
        self.assertEqual(fft('12345678', 3), '03415518')


    def test0_4(self):
        self.assertEqual(fft('12345678', 4), '01029498')


    def test1(self):
        self.assertEqual(fft('80871224585914546619083218645595')[:8], '24176176')


    def test2(self):
        self.assertEqual(fft('19617804207202209144916044189917')[:8], '73745418')


    def test3(self):
        self.assertEqual(fft('69317163492948606335995924319873')[:8], '52432133')
