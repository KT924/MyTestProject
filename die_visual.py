#!/usr/bin/env python
from die import Die
import pygal
die=Die()
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)
#print(results)
frequencies=[]
for value in range(1,7):
    frequency=results.count(value)
    frequencies.append(frequency)
print(frequencies)
hist=pygal.Bar()
hist.x_labels=['1','2','3','4','5','6']
hist.x_title="Result"
hist._y_title="Frequency of Result"
hist.add("D6",frequencies)
hist.render_to_file("die_visual.svg")