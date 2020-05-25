from gym.envs.registration import register

register(
    id='WastedGridWorld-v0',
    entry_point='wasted_gridworld.envs:WastedGridWorld',
)