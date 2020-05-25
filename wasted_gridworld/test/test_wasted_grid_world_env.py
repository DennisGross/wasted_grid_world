from unittest import TestCase
from wasted_gridworld.envs.wasted_gridworld_env import WastedGridWorld
import unittest
class TestWastedGridWorld(TestCase):
    @unittest.skip("bla")
    def test_run1(self):
        env = WastedGridWorld(noise=0)
        env.render()
        env.step(0)
        env.render()
        env.step(0)
        env.render()
        env.step(0)
        env.render()
        env.step(1)
        env.render()
        env.step(1)
        env.render()
        env.step(1)
        env.render()
        self.assertTrue(True)

    def test_run2(self):
        env = WastedGridWorld(noise=0)
        env.render()
        env.step(1)
        env.render()
        env.step(1)
        env.render()
        env.step(0)
        env.render()
        env.step(0)
        env.render()
        env.step(0)
        env.render()
        env.step(1)
        env.render()
        env.reset()
        self.assertTrue(True)
