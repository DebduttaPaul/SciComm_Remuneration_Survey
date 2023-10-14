## Import required libraries.
from astropy.io import ascii
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt


## Reads data from the original .csv file downloaded from GoogleSheets.
data = ascii.read('./../data/Freelance_Writing.csv' )

## Defines the different columns of data into different arrays.
col1  =  data['col1'].data
col2  =  data['col2'].data
col3  =  data['col3'].data
col4  =  data['col4'].data
col5  =  data['col5'].data
col6  =  data['col6'].data
col7  =  data['col7'].data

### Prints the number of rows in each column.
#print ( '\nNumber: ', len(col1), '\n' )


## Uses the knowledge that the first six entires were dummy-entires, to select only the rest.
full_data       =  col1[1:]
remuneration    =  col2[1:]
number_of_words =  col3[1:]
perword_pay     =  col4[1:]
News_flag       =  col5[1:]
English_flag    =  col6[1:]
Indian_flag     =  col7[1:]


## Prints the number of rows in each column. This is the final number of data-points.
print ( '\nNumber: ', len(full_data), '\n' )


## Tabulates the column with shorter, identifiable header names.
table = Table( [ remuneration, number_of_words, perword_pay, News_flag, English_flag, Indian_flag ],
names =  ['Remuneration', 'Number of words', 'Average (INR)', 'News', 'English', 'Indian' ] )

### Prints the table to check.
#print ( '\n' )
#print ( table )
#print ( '\n' )

## Writes the data into a file that will be used by the data-processing code.
ascii.write( table, './../outputs/Freelance_Writing--cleaned.csv', format = 'csv', overwrite = True )



## Selects only the non-blank data from the string array and converts that into float.
def remove_blanks( array ):
    '''
    Parameters:
    array: The string array whose blank data needs to be removed.
    
    Returns:
    array: The float array with the empty data removed.
    '''
    
    array = np.array( [i for i in array if i != ''] )
    array = np.asarray(array, dtype=float)
    return array

## Selects only the non-blank data from the string array and converts that into float, while simultaneously choosing the corresponding elements of another input array.
def select_nonblanks( array1, array2 ):
    '''
    Parameters:
    array1: The string array whose blank data needs to be removed.
    array2: The array whose correspinding data needs to be removed.
    
    Returns:
    x: The float array with the empty data removed.
    y: The corresponding array with the empty data removed.
    '''
    
    x = []
    y = []
    for j, val in enumerate(array1):
        if val != '':
            x.append(val)
            y.append(array2[j])
    x = np.array(x)
    y = np.array(y)
    x = np.asarray(x, dtype=float)
    return (x, y)






# ~ ## Removes blank data from the pay_per_word array.
# ~ perword_pay = remove_blanks( perword_pay )

# ~ ## Tests authenticity, checks outliers, and prints some required numbers.
# ~ print ('\n')
# ~ print ( len(perword_pay) )
# ~ #print ( perword_pay )
# ~ print ( np.sort( np.round(perword_pay, 2) ), '\n' )
# ~ #print ( (perword_pay < 0).any() )
# ~ print ( 'Min   : ', np.min(   perword_pay) )
# ~ print ( 'Max   : ', np.max(   perword_pay) )
# ~ print ( 'Mean  : ', np.mean(  perword_pay) )
# ~ print ( 'Median: ', np.median(perword_pay) )
# ~ print ('\n')

# ~ ## Plots histogram of the non-outliers.
# ~ plt.hist( perword_pay, range = (0, 13), rwidth = 0.7, color = 'r', alpha = 0.6, align = 'left' )
# ~ x_ticks = np.arange(0, 13)
# ~ y_ticks = np.arange(0, 13)
# ~ plt.xticks( x_ticks, x_ticks )
# ~ plt.yticks( y_ticks, y_ticks )
# ~ plt.xlabel( "Freelance writers' pay per word [Indian Rupees]", labelpad=7 )
# ~ plt.ylabel( "Number of instances" )
# ~ plt.text( 8, 9, "Ignores outliers (INR):\n25.0, 56.3, 141.7." )
# ~ plt.tight_layout()
# ~ plt.savefig( './../plots/freelance_writerS_per_word--histogram.pdf' )
# ~ plt.clf()
# ~ plt.close()



# ~ ## Removes blank data from the lump_sum_pay array.
# ~ remuneration = remove_blanks( remuneration )

# ~ ## Tests feasibility.
# ~ print ('\n')
# ~ print ( len(remuneration) )
# ~ print ( (remuneration < 0).any() )
# ~ print ('\n')


# ~ ## Plots histogram of the non-outliers.
# ~ plt.hist( remuneration, range = (0, 60000), bins = 20, rwidth = 0.7, color = 'r', alpha = 0.6, align = 'left' )
# ~ x_ticks = np.arange(0, 65000, 5000 )
# ~ y_ticks = np.arange(0, 29, 2)
# ~ plt.xticks( x_ticks, (x_ticks/1000).astype(int) )
# ~ plt.yticks( y_ticks, y_ticks )
# ~ plt.xlabel( "Freelance writers' lump sum remuneration [in 1000 Indian Rupees]", labelpad=7 )
# ~ plt.ylabel( "Number of instances" )
# ~ plt.grid()
# ~ plt.tight_layout()
# ~ plt.savefig( './../plots/freelance_writerS_lump_sum--histogram.pdf' )
# ~ plt.clf()
# ~ plt.close()









# ~ ## Selects the non-blank pay_per_word data and the corresponding Indian flags.
# ~ X1, Indian_flag_pwPay = select_nonblanks( perword_pay, Indian_flag )

# ~ ## Segregates the pay_per_word data into Indian and foreign clients.
# ~ inds1 = np.where( Indian_flag_pwPay == 'Yes' )[0]
# ~ pwPay_Indian  = X1[inds1]
# ~ pwPay_foreign = np.delete( X1, inds1 )


# ~ ## Selects the non-blank pay_per_word data and the corresponding English flags.
# ~ X2, English_flag_pwPay = select_nonblanks( perword_pay, English_flag )

# ~ ## Segregates the pay_per_word data into English and non-English work.
# ~ inds2 = np.where( English_flag_pwPay == 'No' )[0]
# ~ pwPay_regional = X2[inds2]
# ~ pwPay_English  = np.delete( X2, inds2 )

# ~ ## Checks authenticity and prints some required numbers.
# ~ print ('\n')
# ~ print ( len(pwPay_Indian), '\n' )
# ~ print ( (X1 == X2).all(), '\n' )
# ~ print ( len(pwPay_English), '\n' )
# ~ print ( inds1, '\n')
# ~ print ( inds2, '\n')
# ~ print ( 'Median, Indian  : ', np.median( pwPay_Indian ) )
# ~ print ( 'Median, Foreign : ', np.median( pwPay_foreign) )
# ~ print ( '\n' )
# ~ print ( pwPay_foreign )
# ~ print ( 'Number      of Indian clients paying <  5.0/word: ', len(np.where( pwPay_Indian <   5.0 )[0]) )
# ~ print ( 'Perecentage of Indian clients paying <  5.0/word: ', 100 * len( np.where( pwPay_Indian <  5.0 )[0] ) / len(pwPay_Indian)  )
# ~ print ( 'Number      of Indian clients paying < 10.0/word: ', len(np.where( pwPay_Indian <  10.0 )[0]) )
# ~ print ( 'Perecentage of Indian clients paying < 10.0/word: ', 100 * len( np.where( pwPay_Indian < 10.0 )[0] ) / len(pwPay_Indian)  )
# ~ print ( 'Number of non-English clients paying >  5.0/word: ', len( np.where( pwPay_regional >5.0 )[0] )  )
# ~ print ( 'Highest paid Indian client paid how much        ? ', np.max(pwPay_Indian)  )
# ~ print ( '\n' )

## Plots pay_per_word scatter plot with three different categories.
# ~ plt.tick_params( axis='x', which='both', bottom=False, top=False, labelbottom=False )
# ~ y_ticks = np.arange( 0, 155, 10 )
# ~ plt.ylim( -4, 150 )
# ~ plt.yticks( y_ticks, y_ticks )
# ~ plt.ylabel( "Freelance writers' pay per word [Indian Rupees]", labelpad=7 )
# ~ plt.plot( pwPay_foreign , 'o', color = 'dodgerblue', label = 'Foreign client, English'    )
# ~ plt.plot( pwPay_Indian  , 'o', color = 'darkgreen' , label = 'Indian client, English'     )
# ~ plt.plot( pwPay_regional, 'o', color = 'r'         , label = 'Indian client, non-English' )
# ~ plt.legend()
# ~ plt.grid()
# ~ plt.tight_layout()
# ~ #plt.show()
# ~ plt.savefig( './../plots/freelance_writerS_per_word--scatter_plot.pdf' )
# ~ plt.clf()
# ~ plt.close()

## Plots vertical plot of pay_per_word. Later discarded.
#Indian_x_array  = 2 * np.ones(len(pwPay_Indian ))
#foreign_x_array = 3 * np.ones(len(pwPay_foreign))
#plt.xlim(1, 4)
#plt.tick_params( axis='x', which='both', bottom=False, top=False, labelbottom=False)
#plt.ylabel( "Freelance writers' pay per word [Indian Rupees]", labelpad=7 )
#plt.plot( Indian_x_array , pwPay_Indian , 'ko', label = 'Indian'     )
#plt.plot( foreign_x_array, pwPay_foreign, 'ro', label = 'non-Indian' )
#plt.legend()
#plt.tight_layout()
#plt.savefig( './../plots/freelancer_writerS_per_word--vertical_plot.pdf' )
#plt.clf()
#plt.close()






# ~ ## Selects the non-blank lump_sum_pay data and the corresponding Indian flags.
# ~ X3, Indian_flag_lumpsum = select_nonblanks( remuneration, Indian_flag )

# ~ ## Segregates the lump_sum_pay data into Indian and foreign clients.
# ~ inds3 = np.where( Indian_flag_lumpsum == 'Yes' )[0]
# ~ lumpsum_Indian  = X3[inds3]
# ~ lumpsum_foreign = np.delete( X3, inds3 )


# ~ ## Selects the non-blank lump_sum_pay data and the corresponding English flags.
# ~ X4, English_flag_lumpsum = select_nonblanks( remuneration, English_flag )

# ~ ## Segregates the lump_sum_pay data into English and non-English.
# ~ inds4 = np.where( English_flag_lumpsum == 'No' )[0]
# ~ lumpsum_regional = X4[inds4]
# ~ lumpsum_English  = np.delete( X4, inds4 )

# ~ ## Tests consistency check and prints required indices.
# ~ print ('\n')
# ~ print ( len(lumpsum_Indian), '\n' )
# ~ print ( (X3 == X4).all(), '\n' )
# ~ print ( len(lumpsum_English), '\n' )
# ~ print ( inds3, '\n')
# ~ print ( inds4, '\n')
# ~ print ( '\n' )

# ~ ## Plots lump_sum_pay scatter plot with three different categories.
# ~ plt.tick_params( axis='x', which='both', bottom=False, top=False, labelbottom=False )
# ~ y_ticks = np.arange( 0, 70, 5 )
# ~ plt.ylim( -3, 65 )
# ~ plt.yticks( y_ticks, y_ticks )
# ~ plt.ylabel( "Freelance writers' lump sum remuneration [in 1000 Indian Rupees]", labelpad=7 )
# ~ plt.plot( lumpsum_foreign *1e-3, 'o', color = 'dodgerblue', label = 'Foreign client, English'    )
# ~ plt.plot( lumpsum_Indian  *1e-3, 'o', color = 'darkgreen' , label = 'Indian client, English'     )
# ~ plt.plot( lumpsum_regional*1e-3, 'o', color = 'r'         , label = 'Indian client, non-English' )
# ~ plt.legend( loc = 'upper center' )
# ~ plt.grid()
# ~ plt.tight_layout()
# ~ #plt.show()
# ~ plt.savefig( './../plots/freelance_writerS_lump_sum--scatter_plot.pdf' )
# ~ plt.clf()
# ~ plt.close()






# ~ ## Selects the non-blank pay_per_word data and the corresponding News flags.
# ~ X5, News_flag_pwPay = select_nonblanks( perword_pay, News_flag )

# ~ ## Selects the pay_per_word data only for News.
# ~ inds5 = np.where( News_flag_pwPay == 'Yes' )[0]
# ~ pwPay_News  = X5[inds5]

# ~ ## Selects the non-blank remuneration data and the corresponding News flags.
# ~ X6, News_flag_lumpsum = select_nonblanks( remuneration, News_flag )

# ~ ## Selects the remuneration data only for News.
# ~ inds6 = np.where( News_flag_lumpsum == 'Yes' )[0]
# ~ lumpsum_News  = X6[inds6]

# ~ ## Tests authenticity and checks outliers.
# ~ print ('\n')
# ~ print ( len(pwPay_News), '\n' )
# ~ print ( (pwPay_News < 0).any(), '\n' )
# ~ print ( pwPay_News, '\n' )
# ~ print ( len(lumpsum_News), '\n' )
# ~ print ( (lumpsum_News < 0).any(), '\n' )
# ~ print ( np.sort(lumpsum_News), '\n' )
# ~ print ( 'Min   : ', np.min(   pwPay_News) )
# ~ print ( 'Max   : ', np.max(   pwPay_News) )
# ~ print ( 'Mean  : ', np.mean(  pwPay_News) )
# ~ print ( 'Median: ', np.median(pwPay_News) )
# ~ print ('\n')

# ~ ## Plots histogram of news reports' pay per word.
# ~ x_ticks = np.arange( 0, 13, 1 )
# ~ y_ticks = np.arange( 0, 11, 1 )
# ~ plt.xlim( -0.5, 12 )
# ~ plt.ylim(    0, 10 )
# ~ plt.xticks( x_ticks, x_ticks )
# ~ plt.yticks( y_ticks, y_ticks )
# ~ plt.hist( pwPay_News, rwidth = 0.7, color = 'r', alpha = 0.6, align = 'left' )
# ~ plt.text( 10.1, 8.5, 'News' )
# ~ plt.xlabel( "Freelance news writers' pay per word [Indian Rupees]", labelpad=7 )
# ~ plt.ylabel( "Number of instances" )
# ~ plt.grid()
# ~ plt.tight_layout()
# ~ plt.savefig( './../plots/freelance_news_writerS_per_word--histogram.pdf' )
# ~ plt.clf()
# ~ plt.close()

# ~ ## Plots histogram of news reports' lump sum pay.
# ~ x_ticks = np.arange( 0, 16, 1 )
# ~ y_ticks = np.arange( 0, 15, 1 )
# ~ plt.xlim( -1, 16 )
# ~ plt.ylim(  0, 15 )
# ~ plt.xticks( x_ticks, x_ticks )
# ~ plt.yticks( y_ticks, y_ticks )
# ~ plt.hist( lumpsum_News *1e-3, range = (0, 17), rwidth = 0.7, color = 'r', alpha = 0.6, align = 'left' )
# ~ plt.text( 12.0, 13.3, 'News' )
# ~ plt.xlabel( "Freelance news writers' lump sum remuneration [in 1000 Indian Rupees]", labelpad=7 )
# ~ plt.ylabel( "Number of instances" )
# ~ plt.text( 9.0, 7.35, "Ignores outlier (INR): 40.0 K.", color='navy', bbox=dict(boxstyle='round', facecolor='wheat', edgecolor='y', alpha=0.7) )
# ~ plt.grid()
# ~ plt.tight_layout()
# ~ plt.savefig( './../plots/freelance_news_writerS_lump_sum--histogram.pdf' )
# ~ plt.clf()
# ~ plt.close()
