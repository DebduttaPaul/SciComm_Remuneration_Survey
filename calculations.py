## Imports required libraries.
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
print ( '\n', 'All data...' )
# ~ print ( '\n',        gender, '\n' )
print ( '\n',      edu_qual, '\n' )
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
print ( '\n\n\n', 'Unique data...' )
# ~ print ( '\n', np.unique(       gender), '\n' )
print ( '\n', np.unique(     edu_qual), '\n' )
# ~ print ( '\n', np.unique(   edu_detail), '\n' )
# ~ print ( '\n', np.unique(    exp_years), '\n' )
# ~ print ( '\n', np.unique(    curr_work), '\n' )
# ~ print ( '\n', np.unique(  full_salary), '\n' )
# ~ print ( '\n', np.unique(     full_org), '\n' )
# ~ print ( '\n', np.unique(    org_funds), '\n' )
# ~ print ( '\n', np.unique(  curr_sal_ok), '\n' )
# ~ print ( '\n', np.unique(curr_sal_nego), '\n' )
# ~ print ( '\n', np.unique(frst_sal_nego), '\n' )


## Defines the number that calculates the required number and percentage of a selected column of data, given the sample size is defined.
## Returns the numbers array containing the frequency of each unique entry in that column, and the respective percentages in another array.
def percentage( array, total ):
	'''
	Parameters:
	array: The array of data that needs the analysis.
	total: The sample size against which percentages need to be calculated.
	
	Returns:
	numbers_array   : Array containing individual frequency of each unique element in 'array'.
	percentage_array: The corresponding percentages when calculated against 'total'.
	
	'''
	
	l = len( np.unique(array) )
	numbers_array    = np.zeros(l)
	percentage_array = np.zeros(l)
	for k, val in enumerate( np.unique(array) ):
		print ('\n', val)
		num = len( np.where( array == val )[0] )
		numbers_array[k] = int(num)
		print ('Number:', num)
		per = np.round( 100*num / total, 1 )
		print ('Percentage:', per)
		percentage_array[k] = per
	numbers_array = np.asarray(numbers_array, dtype = 'int')
	return (numbers_array, percentage_array)


## Analyses the data by running the 'percentage' function over the column and stores it in an array of two arrays: numbers array, percentages array.
# ~ results = percentage( edu_qual     , Total )
# ~ results = percentage( edu_detail   , Total )
# ~ results = percentage( exp_years    , Total )
# ~ results = percentage( curr_work    , Total )
# ~ results = percentage( full_salary  , Total )
# ~ results = percentage( full_org     , Total )
# ~ results = percentage( curr_sal_ok  , Total )
# ~ results = percentage( curr_sal_nego, Total )
results = percentage( frst_sal_nego, Total )
# ~ results = percentage( gender       , Total )


## Extracts the numbers array and forces it to be an integer array, and the percentages array.
numbers_array    = results[0]
percentage_array = results[1]

## Prints the two arrays.
print ( '\n')
print ( 'Numbers    : ', numbers_array )
print ( 'Percentages: ', percentage_array)
print ( 'Total      : ', np.sum(numbers_array) ) ## Consistency check
print ( '\n\n\n\n' )



# ~ ## Plots piecharts given the labels, with the percentages correct upto one place of decimal.
# ~ #labels = '0-2 years', '2-5 years', '5-8 years', '8+ years'
# ~ #labels  = 'Maybe', 'No', 'Yes'
# ~ #labels  = 'I did not get an \nopportunity to negotiate', 'Perhaps I could have, \nbut I was not \naware/interested \nin negotiating', 'Yes'
# ~ labels  = 'I did not get an \nopportunity to negotiate', 'Perhaps I could have, \nbut I was not aware/interested \nin negotiating', 'Yes'
# ~ sizes   = percentage_array
# ~ fig, ax = plt.subplots()
# ~ ax.pie( sizes, labels=labels, autopct = '%1.1f%%' )
# ~ ax.axis('equal')
# ~ plt.tight_layout()
# ~ #plt.savefig('./../plots/experience--piechart.pdf')
# ~ #plt.savefig('./../plots/remuneration_OK--piechart.pdf')
# ~ #plt.savefig('./../plots/negotiation_now--piechart.pdf')
# ~ #plt.savefig('./../plots/negotiation_first--piechart.pdf')
# ~ #plt.clf()
# ~ #plt.close()
# ~ plt.show()



## Selects those elements of all the input arrays depending on the conditional indices input.
def select( ind ):
    '''
    Parameters:
    ind: The array of indices with the full dataset needs to be sliced.
    
    Returns:
    ...sliced arrays for all datasets...
    
    '''
    
    return ( gender[ind], edu_qual[ind], edu_detail[ind], exp_years[ind], curr_work[ind], full_salary[ind], full_org[ind], org_funds[ind], curr_sal_ok[ind], curr_sal_nego[ind], frst_sal_nego[ind] )



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


## Runs the function 'percentage' to calulate the numbers and percentages on the sliced data.
results = percentage( full_timer_full_salary, l )
#results = percentage( full_timer_full_org   , l )

## Captures the data into two separate arrays.
numbers_array    = results[0]
percentage_array = results[1]
## Prints them.
print ( '\n')
print ( 'Numbers    : ', numbers_array )
print ( 'Percentages: ', percentage_array)
print ( 'Total      : ', np.sum(numbers_array) )
print ( '\n' )


# ~ ## Plots histogram of full-timers' salaries.
# ~ labels, counts = np.unique( full_timer_full_salary, return_counts=True )
# ~ inds = [6, 2, 3, 4, 1, 0, 5]
# ~ labels = labels[inds]; labels[0] = '<25 K'; labels[-1] = '>2 Lacs'
# ~ counts = counts[inds]
# ~ yticks = np.arange(1, 20, 2)
# ~ plt.bar( labels, counts )
# ~ plt.gca().set_xticks(labels)
# ~ plt.gca().set_yticks(yticks)
# ~ plt.grid()
# ~ plt.xlabel('[Indian Rupees]', labelpad=5)
# ~ plt.ylabel('Number of respondents')
# ~ plt.tight_layout()
# ~ plt.savefig('./../plots/full_timerS_salaries--histogram.pdf')
# ~ plt.clf()
# ~ plt.close()
# ~ #plt.show()


# ~ ## Plotting histogram of full-timers' funding agency types.
# ~ labels, counts = np.unique( full_timer_full_org, return_counts=True )
# ~ inds = [2, 6, 0, 3, 5, 1, 4]
# ~ counts = counts[inds]
# ~ labels = np.array([ 'Government', 'Public institution', 'Non-profit', 'Journalistic', 'Private institution', 'For-profit', 'NA' ])
# ~ yticks = np.arange(2, 24, 2)
# ~ plt.bar( labels, counts )
# ~ plt.gca().set_xticks(labels)
# ~ plt.gca().set_yticks(yticks)
# ~ plt.grid()
# ~ plt.ylabel('Number of respondents')
# ~ plt.tight_layout()
# ~ plt.show()






print ( '\n' )
