import gym
import random
import pygame
import inspect
from gym import spaces
import numpy as np
class WastedGridWorld(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, noise=0.2,
                 living_penalty=0.05,
                 grid_size=[4, 4],
                 agent_position=[3, 0],
                 cops_position=[3, 3],
                 cops_reward=0.5,
                 bad_ombre_position=[1, 1],
                 bad_ombre_reward=-1,
                 home_position=[0,3],
                 home_reward=1):
        self.noise = noise
        self.living_penalty = living_penalty
        self.grid_size = grid_size
        self.agent_position = agent_position
        self.cops_position = cops_position
        self.cops_reward = cops_reward
        self.hombre_malo_position = bad_ombre_position
        self.hombre_malo_reward = bad_ombre_reward
        self.home_position = home_position
        self.home_reward = home_reward
        self.done = False
        self.agent_init_position = agent_position.copy()
        self.cops_init_position = cops_position.copy()
        self.hombre_malo_init_position = bad_ombre_position.copy()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(1, self.grid_size[0], self.grid_size[1]), dtype=np.uint8)


    def applying_potential_noise(self, action):
        if random.random() <= self.noise:
            coin = random.randint(0, 1)
            if action == 0 and coin == 0:
                action = 3
            elif action == 0 and coin == 1:
                action = 1
            elif action == 1 and coin == 0:
                action = 0
            elif action == 1 and coin == 1:
                action = 2
            elif action == 2 and coin == 0:
                action = 1
            elif action == 2 and coin == 1:
                action = 3
            elif action == 3 and coin == 0:
                action = 2
            elif action == 3 and coin == 1:
                action = 0
        return action

    def apply_action(self, action):
        if action == 0:
            # NORTH
            if self.agent_position[0] > 0:
                self.agent_position[0] -= 1
        elif action == 1:
            # EAST
            if self.agent_position[1] < self.grid_size[1]:
                self.agent_position[1] += 1
        elif action == 2:
            # SOUTH
            if self.agent_position[0] < self.grid_size[0]:
                self.agent_position[0] += 1
        elif action == 3:
            # WEST
            if self.agent_position[1] > 0:
                self.agent_position[1] -= 1

    def same_position(self, pos1, pos2):
        return pos1[0] == pos2[0] and pos1[1] == pos2[1]

    def get_reward(self):
        if self.same_position(self.agent_position, self.home_position):
            return self.home_reward, True
        elif self.same_position(self.agent_position, self.hombre_malo_position):
            return self.hombre_malo_reward, True
        elif self.same_position(self.agent_position, self.cops_position):
            return self.cops_reward, False
        else:
            return self.living_penalty, False

    def get_state(self):
        grid_world = np.zeros((self.grid_size[0], self.grid_size[1]))
        grid_world[self.agent_position[0]-1][self.agent_position[1]-1] = 1
        grid_world[self.cops_position[0]-1][self.cops_position[1]-1] = 2
        grid_world[self.hombre_malo_position[0]-1][self.hombre_malo_position[1]-1] = 3
        return grid_world


    def step(self, action):
        action = self.applying_potential_noise(action)
        self.apply_action(action)
        reward, self.done = self.get_reward()
        state = self.get_state()
        return state, reward, self.done, None


    def reset(self):
        self.agent_position = self.agent_init_position.copy()
        self.cops_position = self.cops_init_position.copy()
        self.hombre_malo_position = self.hombre_malo_init_position.copy()
        return self.get_state()


    def render(self, mode='human', close=False):
        folder_path=inspect.getfile(self.__class__).replace("wasted_gridworld_env.py","")
        pygame.init()
        # Create the screen
        screen = pygame.display.set_mode((self.grid_size[0]*100, self.grid_size[1]*100))
        # Title and Icon
        pygame.display.set_caption("Wasted Gridworld")
        # Draw Background
        background = pygame.image.load(folder_path+'assets/cell.png')
        for i in range(self.grid_size[0]):
            for d in range(self.grid_size[1]):
                screen.blit(background, (i*100, d*100))

        # Draw Cops
        cops = pygame.image.load(folder_path+'assets/cops.png')
        cops = pygame.transform.scale(cops, (100, 100))
        screen.blit(cops, (self.cops_position[1] * 100, self.cops_position[0] * 100))

        # Draw Hombre Malo
        hombre_malo = pygame.image.load(folder_path+'assets/hombre_malo.png')
        hombre_malo = pygame.transform.scale(hombre_malo, (100, 100))
        screen.blit(hombre_malo, (self.hombre_malo_position[1] * 100, self.hombre_malo_position[0] * 100))

        # Draw Hombre Malo
        home = pygame.image.load(folder_path+'assets/home.png')
        home = pygame.transform.scale(home, (100, 100))
        screen.blit(home, (self.home_position[1] * 100, self.home_position[0] * 100))

        # Draw Agent
        agent = pygame.image.load(folder_path+'assets/agent.png')
        agent = pygame.transform.scale(agent, (100, 100))
        screen.blit(agent, (self.agent_position[1]*100, self.agent_position[0]*100))

        pygame.display.update()
        # Wait
        pygame.time.wait(1000)
        if self.done == True:
            pygame.quit()






