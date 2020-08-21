from unittest import TestCase
from wasted_gridworld.envs.wasted_gridworld_env import WastedGridWorld
import unittest
from baselines import deepq
import numpy as np
import tensorflow as tf

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
        model = deepq.learn(env, network='mlp', total_timesteps=10000)

        done = False
        state = env.reset()
        episode_rew = 0
        print('start')
        while done is False:
            #print(env.agent_position)
            env.render()
            state = state.reshape(-1, 4, 4)
            actions, _, _, _ = model.step(state)
            state, rew, done, _ = env.step(actions.numpy()[0])
            episode_rew += rew
        print(env.counter)
        print(env.agent_position)
        print(episode_rew)


        self.assertTrue(True)

