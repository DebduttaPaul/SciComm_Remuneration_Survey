## Imports required libraries.
from astropy.io import ascii
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt


## Reads data from the selected .csv file output by the data-reading code.
data = ascii.read( './../outputs/selected.csv', format = 'csv' )


## Defines the two columns of data into two arrays.
curr_sal_nego = data['Negotiate current salary?'].data
frst_sal_nego = data['Negotiate first salary?'].data


## Calculates the number of rows, that is, survey data-points.
Total = len(curr_sal_nego)

## Prints the number of data-points.
print ( '\n', 'Number: ', Total, '\n' )



## Defines the number that calculates the required number and percentage of a selected column of data, given the sample size is defined.
## Returns the numbers array containing the frequency of each unique entry in that column, and the respective percentages in another array.
def percentage( array, total ):
	'''
	Parameters:
	array: The array of data that needs the analysis.
	total: The sample size against which percentages need to be calculated.
	
	Returns:
	percentage_array: Array containing individual percentages, when calculated against the total, of each unique element in 'array'.
	'''
	unique_array = np.unique(array)
	print ( '\n', unique_array, '\n' )
	l = len( unique_array )
	percentage_array = np.zeros(l)
	for k, val in enumerate( unique_array ):
		num = len( np.where( array == val )[0] )
		per = np.round( 100*num / total, 1 )
		percentage_array[k] = per
	return (percentage_array)


## Analyses the data by running the 'percentage' function over the column and stores for the two input datasets.
percentages_curr_sal_nego = percentage( curr_sal_nego, Total )
percentages_frst_sal_nego = percentage( frst_sal_nego, Total )



## Prints the two arrays.
print ( '\n')
print ( 'Current: ', percentages_curr_sal_nego )
print ( 'Earlier: ', percentages_frst_sal_nego )
print ( '\n' )



## Plots histogram of full-timers' salaries.
def autolabel(rects):
    '''Attach a text label above each bar in *rects*, displaying its height.'''
    for rect in rects:
        height = rect.get_height()
        # ~ print (height)
        ax.annotate('{}'.format(height),
                    xy = (rect.get_x() + rect.get_width() / 2, height),
                    xytext = (0, 3),  # 3 points vertical offset
                    textcoords = "offset points",
                    ha = 'center', va = 'bottom')
labels = ["Did not get opportunity", "I wasn't aware/ interested", "Yes"]
x      = np.arange(len(labels))
width  = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar( x - width/2, percentages_curr_sal_nego, width, label="Current assignment/ job" )
rects2 = ax.bar( x + width/2, percentages_frst_sal_nego, width, label="First assignment/ job"   )
ax.set_ylim( [0, 80] )
ax.set_title("Question: Did you negotiate the remuneration?")
ax.set_ylabel("Percentage [%]")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.savefig('./../plots/negotiation_comparison.pdf')
plt.clf()
plt.close()
#plt.show()



