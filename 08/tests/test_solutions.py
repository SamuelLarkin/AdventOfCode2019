#!/usr/bin/env  python3

import unittest
import numpy as np

from solutions import createImages
from solutions import parse


class TestSolutions(unittest.TestCase):
    def testParse(self):
        data = '123456789012'
        self.assertEqual(parse(data), [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2])


    def testPartI(self):
        images = createImages(parse('123456789012'), 2, 2, 3)
        #self.assertEqual(images, [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]])
        np.testing.assert_array_equal(images, [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [0, 1, 2]]])
