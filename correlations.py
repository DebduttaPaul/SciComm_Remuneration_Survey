## Importssd required libraries.
from astropy.io import ascii
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt


## Reads data from the selected .csv file output by the data-reading code.
data = ascii.read( './../outputs/selected.csv', format = 'csv' )


## Defines the different columns of data into different arrays.
gender        = data['Gender'].data
edu_qual      = data['Educational Qualification'].data
edu_detail    = data['Science or SciComm'].data
exp_years     = data['Years of Experience'].data
curr_work     = data['Current Work'].data
full_salary   = data['Full-timerS salary'].data
full_org      = data['Full-timerS organisation'].data
org_funds     = data['India or Abroad'].data
curr_sal_ok   = data['Current salary commensurate?'].data
curr_sal_nego = data['Negotiate current salary?'].data
frst_sal_nego = data['Negotiate first salary?'].data


## Calculates the number of rows, that is, survey data-points.
Total = len(gender)

## Prints the number of data-points.
print ( '\n', 'Number: ', Total, '\n' )


## Prints the column of data being analysed in the particular run.
# ~ print ( '\n', 'All data...' )
# ~ print ( '\n',        gender, '\n' )
# ~ print ( '\n',      edu_qual, '\n' )
# ~ print ( '\n',    edu_detail, '\n' )
# ~ print ( '\n',     exp_years, '\n' )
# ~ print ( '\n',     curr_work, '\n' )
# ~ print ( '\n',   full_salary, '\n' )
# ~ print ( '\n',      full_org, '\n' )
# ~ print ( '\n',     org_funds, '\n' )
# ~ print ( '\n',   curr_sal_ok, '\n' )
# ~ print ( '\n', curr_sal_nego, '\n' )
# ~ print ( '\n', frst_sal_nego, '\n' )


## Prints the unique entries in the column.
# ~ print ( '\n\n\n', 'Unique data...' )
# ~ print ( '\n', np.unique(       gender), '\n' )
# ~ print ( '\n', np.unique(     edu_qual), '\n' )
# ~ print ( '\n', np.unique(   edu_detail), '\n' )
# ~ print ( '\n', np.unique(    exp_years), '\n' )
# ~ print ( '\n', np.unique(    curr_work), '\n' )
# ~ print ( '\n', np.unique(  full_salary), '\n' )
# ~ print ( '\n', np.unique(     full_org), '\n' )
# ~ print ( '\n', np.unique(    org_funds), '\n' )
# ~ print ( '\n', np.unique(  curr_sal_ok), '\n' )
# ~ print ( '\n', np.unique(curr_sal_nego), '\n' )
# ~ print ( '\n', np.unique(frst_sal_nego), '\n' )




def select( ind ):
    '''
    Parameters:
    ind: The array of indices with the full dataset needs to be sliced.
    
    Returns:
    ...sliced arrays for all datasets...
    
    '''
    
    return ( gender[ind], edu_qual[ind], edu_detail[ind], exp_years[ind], curr_work[ind], full_salary[ind], full_org[ind], org_funds[ind], curr_sal_ok[ind], curr_sal_nego[ind], frst_sal_nego[ind] )



## Defines the number that calculates the required number and percentage of a selected column of data, given the sample size is defined.
## Returns the numbers array containing the frequency of each unique entry in that column, and the respective percentages in another array.
def correlate( array1, array2 ):
	'''
	Parameters:
	array1, array2: The two arays for which the heatmap needs to be generated.
	
	Returns:
	Z : Array containing meshed data of the correlation/heatmap in jumbled order.
	
	'''
	
	l1 = len( np.unique(array1) )
	l2 = len( np.unique(array2) )
	Z = np.zeros( (l1, l2) )
	for i, val1 in enumerate(np.unique(array1)):
		for j, val2 in enumerate(np.unique(array2)):
			Z[i, j] = len ( np.where( (array1 == val1) & (array2 == val2) )[0] )
	Z = np.asarray(Z, dtype = 'int')
	return Z

# ~ ## Selects the indices where the person is a full-time professional with a single organisation.
inds = np.where( curr_work == 'Full-time professional with a single organisation' )[0]
l = len(inds) ## Calculates the number of such professionals.
print ( 'Number of full-time professionals with a single organisation:', l ) ## Prints the number.

## Slices the data according to these indices using the function 'slices'.
full_timer_single_org    = select(inds)
## Saves the data for each column for these professionals in separate arrays.
full_timer_gender        = full_timer_single_org[0]
full_timer_edu_qual      = full_timer_single_org[1]
full_timer_edu_detail    = full_timer_single_org[2]
full_timer_exp_years     = full_timer_single_org[3]
full_timer_curr_work     = full_timer_single_org[4]
full_timer_full_salary   = full_timer_single_org[5]
full_timer_full_org      = full_timer_single_org[6]
full_timer_org_funds     = full_timer_single_org[7]
full_timer_curr_sal_ok   = full_timer_single_org[8]
full_timer_curr_sal_nego = full_timer_single_org[9]
full_timer_frst_sal_nego = full_timer_single_org[10]


## Inputs the order of the full timers' full time salaries from the calculations.py code.
inds_sal  = [6, 2, 3, 4, 1, 0, 5]

## Does a consistency check of the order.
print ('\n\n')
array = np.unique(full_timer_full_salary)
print ('\n')
labels_sal = array [ np.array(inds_sal) ]
labels_sal[0] = '<25 K'; labels_sal[-1] = '>2 Lacs'
print (labels_sal)
print ('\n\n')




## Runs the function 'correlate' to calulate the correlation between full-timers' salary versus fullt-timers' educational qualification.
Z = correlate( full_timer_full_salary, full_timer_edu_qual  )

## Arranges the data according to the full timers' full time salaries order.
#print ('\n\n')
#print (Z)
for i in np.arange( int(7/2) + 1 ):
	Z[ [i, inds_sal[i]] ] = Z[ [inds_sal[i], i] ]
#print (Z)
#print ('\n\n')



## Figures out the the order for full timers' educational qualification.
inds_qual = [4, 3, 0, 2, 1]
print ('\n\n')
array = np.unique(full_timer_edu_qual)
labels_qual = array[ np.array(inds_qual) ]
print (labels_qual)
print ('\n\n')


## Implements the order on the meshed data. 
#print ('\n\n')
#print (Z)
#print ('\n')
Z[ :, [0, 4] ] = Z[ :, [4, 0] ]
Z[ :, [1, 3] ] = Z[ :, [3, 1] ]
Z[ :, [2, 4] ] = Z[ :, [4, 2] ]
Z[ :, [3, 4] ] = Z[ :, [4, 3] ]
#print (Z)
#print ('\n\n')


## Plots the salary versus educational qualification heatmap.
labels_qual = ['UG', 'PG', 'MPhil', 'PhD\nunder review', 'PhD']
plt.imshow( Z, origin = 'lower' )
plt.colorbar()
plt.yticks( list(range(7)), labels_sal  )
plt.xticks( list(range(5)), labels_qual )
plt.ylabel("Full-timers' salaries [Indian Rupees]")
plt.xlabel("Full-timers' educational qualification", labelpad=10)
plt.tight_layout()
plt.savefig('./../plots/correlation--salary_vs_education.pdf' )
plt.clf()
plt.close()
#plt.show()







## Runs the function 'correlate' to calulate the correlation between full-timers' salary versus fullt-timers' work experience.
Z = correlate( full_timer_full_salary, full_timer_exp_years )

## Arranges the data according to the full timers' full time salaries order.
#print ('\n\n')
#print (Z)
for i in np.arange( int(7/2) + 1 ):
	Z[ [i, inds_sal[i]] ] = Z[ [inds_sal[i], i] ]
#print (Z)
#print ('\n\n')



## Checks out the the order for full timers' work experience and shortens the text.
print ('\n\n')
array = np.unique(full_timer_exp_years)
for i, val in enumerate(array):
	array[i] = val[:-6]
labels_exp = list(array)
print (labels_exp)
print ('\n\n')


## Plots the salary versus work experience heatmap.
plt.imshow( Z, origin = 'lower' )
plt.colorbar()
plt.yticks( list(range(7)), labels_sal )
plt.xticks( list(range(4)), labels_exp )
plt.ylabel("Full-timers' salaries [Indian Rupees]")
plt.xlabel("Full-timers' work experience [years]", labelpad=10)
plt.tight_layout()
plt.savefig('./../plots/correlation--salary_vs_experience.pdf')
plt.clf()
plt.close()
#plt.show()



print ( '\n' )
