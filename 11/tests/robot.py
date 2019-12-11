#!/usr/bin/env  python3

import unittest

from robot import Robot


class TestRobot(unittest.TestCase):
    def testLeftTurn(self):
        robot = Robot()
        self.assertEqual(robot.position, (0, 0))
        self.assertEqual(robot.direction, (0, 1))

        robot.step(0)
        self.assertEqual(robot.direction, (-1, 0))
        self.assertEqual(robot.position, (-1, 0))

        robot.step(0)
        self.assertEqual(robot.direction, (0, -1))
        self.assertEqual(robot.position, (-1, -1))

        robot.step(0)
        self.assertEqual(robot.direction, (1, 0))
        self.assertEqual(robot.position, (0, -1))

        robot.step(0)
        self.assertEqual(robot.direction, (0, 1))
        self.assertEqual(robot.position, (0,0))


    def testRightTurn(self):
        robot = Robot()
        self.assertEqual(robot.position, (0, 0))
        self.assertEqual(robot.direction, (0, 1))

        robot.step(1)
        self.assertEqual(robot.direction, (1, 0))
        self.assertEqual(robot.position, (1, 0))

        robot.step(1)
        self.assertEqual(robot.direction, (0, -1))
        self.assertEqual(robot.position, (1, -1))

        robot.step(1)
        self.assertEqual(robot.direction, (-1, 0))
        self.assertEqual(robot.position, (0, -1))

        robot.step(1)
        self.assertEqual(robot.direction, (0, 1))
        self.assertEqual(robot.position, (0, 0))
