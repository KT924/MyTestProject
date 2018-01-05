#!/usr/bin/env python
from random import choice
class RandomWalk():
    def __init__(self,numPoints):
        self.numPoints=numPoints
        self.xValue=[0]
        self.yValue=[0]

    def get_step(self):
        while len(self.xValue)<self.numPoints:
            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4,5,6,7])
            x_step=x_direction*x_distance   #计算出Ｘ轴应该走的步数

            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4,5,6,7])
            y_step=y_direction*y_distance  #计算出Ｙ轴应该走的步数
            if x_step==0 and y_step==0: #当步数为0时跳过计算
                continue
    def fill_walk(self):#制造一个随机的列表
        while len(self.xValue)< self.numPoints:

            nextX=self.xValue[-1]+x_step
            nextY=self.yValue[-1]+y_step

            self.xValue.append(nextX)
            self.yValue.append(nextY)

