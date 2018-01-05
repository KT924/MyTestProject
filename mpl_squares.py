#!/usr/bin/env python
import matplotlib.pyplot as plt
def a():
    squares=[1,4,9,16,25,5]
    input_values=[2,3,4,5,6,12]
    plt.plot(input_values,squares,linewidth=5)

    plt.title('Square Numbers',fontsize=14)
    plt.xlabel('Value',fontsize=14)
    plt.ylabel('time',fontsize=13)
    plt.tick_params(axis='both',labelsize=14)
    plt.show()

def b():
    fig=plt.figure()
