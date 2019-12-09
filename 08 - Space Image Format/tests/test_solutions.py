#!/usr/bin/env  python3

import unittest
import numpy as np

from solutions import combine
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


    def testPartII(self):
        images = createImages(parse('0222112222120000'), 4, 2, 2)
        np.testing.assert_array_equal(images, [[[0, 2], [2, 2]], [[1, 1], [2, 2]], [[2, 2], [1, 2]], [[0, 0], [0, 0]]])

        image = combine(images)

        self.assertEqual(image, [0,1,1,0])
        #np.testing.assert_array_equal(image, [[0,1], [1,0]])
