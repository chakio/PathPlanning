"""
Plotting tools for Sampling-based algorithms
@author: huiming zhou
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation as anim
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../../Sampling_based_Planning/")

from Sampling_based_Planning.rrt_2D import env


class Plotting:
    def __init__(self, x_start, x_goal, env):
        self.xI, self.xG = x_start, x_goal
        self.env = env
        self.obs_bound = self.env.obs_boundary
        self.obs_circle = self.env.obs_circle
        self.obs_rectangle = self.env.obs_rectangle

    def animation(self, nodelist, path, name, animation=False):
        self.path = path
        now = time.localtime()
        d = time.strftime('%Y_%m_%d_%H_%M_%S.png', now) 
        d_gif = time.strftime('%Y_%m_%d_%H_%M_%S.mp4', now) 
        self.fig, self.ax = plt.subplots()
        self.plot_grid(name)
        #ims = self.plot_visited(nodelist, animation)
        if animation == True:
            ani = anim.FuncAnimation(self.fig, self.plot_visited, fargs=(nodelist, animation), frames=len(nodelist)+100, interval=3)
            ani.save(d_gif)
        # self.plot_path(path)
        
        
        print(d)
        # if ims is not None:
            # ani = anim.ArtistAnimation(self.fig, ims, interval=100)
        
        plt.savefig(d,transparent=True, dpi=500)
        # plt.show()

    def animation_connect(self, V1, V2, path, name):
        self.plot_grid(name)
        self.plot_visited_connect(V1, V2)
        # self.plot_path(path)
        now = time.localtime()
        d = time.strftime('%Y_%m_%d_%H_%M_%S.png', now) 
        print(d)
        plt.savefig(d,transparent=True)
        
        # plt.show()

    def plot_grid(self, name):
        

        for (ox, oy, w, h) in self.obs_bound:
            self.ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    edgecolor='black',
                    facecolor='black',
                    fill=True
                )
            )

        for (ox, oy, w, h) in self.obs_rectangle:
            self.ax.add_patch(
                patches.Rectangle(
                    (ox, oy), w, h,
                    edgecolor='black',
                    facecolor='gray',
                    fill=True
                )
            )

        for (ox, oy, r) in self.obs_circle:
            self.ax.add_patch(
                patches.Circle(
                    (ox, oy), r,
                    edgecolor='black',
                    facecolor='gray',
                    fill=True
                )
            )

        self.ax.plot(self.xI[0], self.xI[1], "bs", linewidth=2)
        self.ax.plot(self.xG[0], self.xG[1], "gs", linewidth=2)

        plt.title(name)
        plt.axis("equal")

    def plot_visited(self, i, nodelist, animation):
        if animation:
            count = 0
            ims = []
            # for node in nodelist:
            
            count = i
            if i >=len(nodelist):
                if len(self.path) != 0:
                    self.ax.plot([x[0] for x in self.path], [x[1] for x in self.path], '-r', linewidth=2)
            else:
                node = nodelist[i]
                if node.parent:
                    if count % 10 == 0:
                        plt.pause(0.001)
                        im = self.ax.plot([node.parent.x, node.x], [node.parent.y, node.y], color="darkorange", linewidth=1)
                        # ims.append(im)
                    else:
                        self.ax.plot([node.parent.x, node.x], [node.parent.y, node.y], color="darkorange", linewidth=1)

            return ims
        else:
            for node in nodelist:
                if node.parent:
                    plt.plot([node.parent.x, node.x], [node.parent.y, node.y], color="darkorange", linewidth=1)
            return None
    @staticmethod
    def plot_visited_connect(V1, V2):
        len1, len2 = len(V1), len(V2)

        for k in range(max(len1, len2)):
            if k < len1:
                if V1[k].parent:
                    plt.plot([V1[k].x, V1[k].parent.x], [V1[k].y, V1[k].parent.y], color="darkorange", linewidth=1)
            if k < len2:
                if V2[k].parent:
                    plt.plot([V2[k].x, V2[k].parent.x], [V2[k].y, V2[k].parent.y], color="darkorange", linewidth=1)

            plt.gcf().canvas.mpl_connect('key_release_event',
                                         lambda event: [exit(0) if event.key == 'escape' else None])

            if k % 2 == 0:
                plt.pause(0.001)

        plt.pause(0.01)

    @staticmethod
    def plot_path(path):
        if len(path) != 0:
            plt.plot([x[0] for x in path], [x[1] for x in path], '-r', linewidth=2)
            plt.pause(0.01)
        plt.show()
