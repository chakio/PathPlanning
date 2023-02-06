"""
Environment for rrt_2D
@author: huiming zhou
"""

import random
class Env:
    def __init__(self):
        self.x_range = (0, 50)
        self.y_range = (0, 30)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        obs_boundary = [
            [0, 0, 0.2, 30],
            [0, 30, 50, 0.2],
            [0.2, 0, 50, 0.2],
            [50, 0.2, 0.2, 30]
        ]
        
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        # obs_rectangle = [
        #     [14, 12, 8, 2],
        #     [27, 7, 10, 2]
        # ]
        obs_rectangle = [
            [random.uniform(10, 40), random.uniform(10, 20), random.uniform(1, 10), random.uniform(1, 10)],
            [random.uniform(10, 40), random.uniform(10, 20), random.uniform(1, 10), random.uniform(1, 10)]
        ]
        
        # obs_rectangle = []
        return obs_rectangle

    @staticmethod
    def obs_circle():
        # obs_cir = [
        #     [7, 12, 3],
        #     [30, 20, 2],
        #     [25, 23, 3]
        # ]
        obs_cir = [
            [random.uniform(10, 40), random.uniform(10, 20), random.uniform(1, 7)],
            [random.uniform(10, 40), random.uniform(10, 20), random.uniform(1, 7)]
        ]
        # obs_cir = []

        return obs_cir
