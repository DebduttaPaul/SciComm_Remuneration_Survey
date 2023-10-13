## Import required libraries.
import numpy as np
import matplotlib.pyplot as plt


## Defines the labels and the corresponding data.
labels = 'Writing', 'Workshop', 'Translation', 'Video/\nAudio', 'Illustration/\nArt/Design', 'Editing/\nManaging', 'Others'
sizes = [67, 5, 2, 6, 13, 8, 10]
#explode = (0.1, 0, 0, 0, 0, 0, 0)  # only explode" the 2nd slice (i.e. 'Hogs')


## Plots.
fig, ax = plt.subplots()
ax.pie( sizes, labels=labels, autopct='%1.1f%%', startangle=105 )
ax.axis( 'equal' )  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.tight_layout()
plt.savefig( './../plots/freelancerS_work--piechart.pdf' )
plt.clf()
plt.close()
