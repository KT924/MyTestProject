#!/usr/bin/env python
import matplotlib.pyplot as plt
from random_walk import RandomWalk
def a():
    #x_values=[1,2,3,4,5]
    #y_values=[6,7,8,9,10]
    x_values=list(range(1,1001))
    y_values=[x**2 for x in x_values]
    plt.scatter(x=x_values,y=y_values,c=y_values,s=40,cmap=plt.cm.Blues)
    plt.title('Square Numbers',fontsize=14)
    plt.xlabel('Value',fontsize=14)
    plt.ylabel('Square of Value',fontsize=14)
    plt.tick_params(axis='both',labelsize=14)
    plt.show()

def b():
    while True:
        rw=RandomWalk(numPoints=5000)
        rw.fill_walk()  #填充列表
        pointNum=list(range(rw.numPoints))
        #print(plt.cm.Blues)
        plt.scatter(rw.xValue, rw.yValue, s=1, c=pointNum, cmap=plt.cm.Blues)
        plt.show()
        #plt.scatter(0,0,c='green',s=100)
        #plt.scatter(rw.xValue[-1],rw.yValue[-1],s=15,c='red')
        plt.show()
        keep_running=input("Make another walk?(y/n):")
        if keep_running=='n':
            break

def c():
    rw=RandomWalk(numPoints=5000)
    rw.fill_walk()
    plt.plot(rw.xValue,rw.yValue,linewidth=1)
    plt.show()

if __name__=='__main__':
    b()