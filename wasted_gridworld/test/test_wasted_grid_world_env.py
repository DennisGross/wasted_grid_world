from unittest import TestCase
from wasted_gridworld.envs.wasted_gridworld_env import WastedGridWorld
import unittest
from baselines import deepq
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

    @unittest.skip("bla")
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

    def test_open_ai_baselines_deepq(self):
        env = WastedGridWorld(noise=0)
        env.reset()
        agent = deepq.learn(env, network='mlp', lr=0.0001, total_timesteps=1000, exploration_fraction=0.1,
                            exploration_final_eps=0.02)
        self.assertTrue(True)

