#!/usr/bin/env  python3

import numpy as np
import unittest

from moons import influence
from moons import step
from moons import velocity
from moons import energy
from parser import parse


_data = '''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>'''.splitlines()



class TestInfluence(unittest.TestCase):
    def test1(self):
        planets = parse(_data)
        self.assertEqual(planets.tolist(), [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])

        influences = influence(planets)
        self.assertEqual(influences.tolist(), 
                [[[ 0,  1,  1,  1],
                  [-1,  0,  1,  1],
                  [-1, -1,  0, -1],
                  [-1, -1,  1,  0]],
                 [[ 0, -1, -1,  1],
                  [ 1,  0,  1,  1],
                  [ 1, -1,  0,  1],
                  [-1, -1, -1,  0]],
                 [[ 0, -1,  1, -1],
                  [ 1,  0,  1,  1],
                  [-1, -1,  0, -1],
                  [ 1, -1,  1,  0]]])




class TestVelocity(unittest.TestCase):
    def test1(self):
        planets = parse(_data)
        self.assertEqual(planets.tolist(), [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])

        velocities = velocity(influence(planets))
        self.assertEqual(velocities.tolist(),
                [[ 3,  1, -3, -1],
                 [-1,  3,  1, -3],
                 [-1,  3, -3,  1]])




class TestStep(unittest.TestCase):
    def test1(self):
        planets = parse(_data)
        self.assertEqual(planets.tolist(), [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]])

        pp, pv = step(planets, np.zeros_like(planets))
        self.assertEqual(pp.tolist(),
                [[ 2, -1,  1],
                 [ 3, -7, -4],
                 [ 1, -7,  5],
                 [ 2,  2,  0]])
        self.assertEqual(pv.tolist(),
                [[ 3, -1, -1],
                 [ 1,  3,  3],
                 [-3,  1, -3],
                 [-1, -3,  1]])




class TestEnergy(unittest.TestCase):
    def test1(self):
        e = energy([[2,1,3],[1,8,0],[3,6,1],[2,0,4]],
                [[3,2,1],[1,1,3],[3,2,3],[1,1,1]])
        self.assertEqual(e, 179)



    def test1(self):
        e = energy(np.array([[2,-1,3],[1,-8,0],[-3,-6,1],[2,0,4]]),
                np.array([[3,2,-1],[-1,-1,3],[3,2,3],[-1,-1,-1]]))
        self.assertEqual(e, 179)
