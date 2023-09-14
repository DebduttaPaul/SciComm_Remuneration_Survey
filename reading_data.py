## Import required libraries.
from astropy.io import ascii
from astropy.table import Table


## Reads data from the original .csv file downloaded from GoogleSheets.
data = ascii.read('./../data/Form_Responses.csv' )
print ( '\n', data, '\n' )


## Defines the different columns of data into different arrays.
col1  =  data['col1'].data
col2  =  data['col2'].data
col3  =  data['col3'].data
col4  =  data['col4'].data
col5  =  data['col5'].data
col6  =  data['col6'].data
col7  =  data['col7'].data
col8  =  data['col8'].data
col9  =  data['col9'].data
col10 = data['col10'].data
col11 = data['col11'].data
col12 = data['col12'].data
col13 = data['col13'].data
col14 = data['col14'].data
col15 = data['col15'].data
col16 = data['col16'].data
col17 = data['col17'].data
col18 = data['col18'].data


## Prints the number of rows in each column.
print ( '\n Number: ', len(col1), '\n' )


## Tabulates the data into standard astropy table.
table = Table( [ col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 ] )
ascii.write( table, './../outputs/full.csv', format = 'csv', overwrite = True )


## Uses the knowledge that the first six entires were dummy-entires, to select only the rest.
col1  =  col1[7:]
col2  =  col2[7:]
col3  =  col3[7:]
col4  =  col4[7:]
col5  =  col5[7:]
col6  =  col6[7:]
col7  =  col7[7:]
col8  =  col8[7:]
col9  =  col9[7:]
col10 = col10[7:]
col11 = col11[7:]
col12 = col12[7:]
col13 = col13[7:]
col14 = col14[7:]
col15 = col15[7:]
col16 = col16[7:]
col17 = col17[7:]
col18 = col18[7:]


## Prints the number of rows in each column. This is the final number of data-points.
print ( '\n Number: ', len(col1), '\n' )

## Test print
# ~ print ('\n', col1, '\n' )


## Tabulates the column with shorter, identifiable header names.
table = Table( [ col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16, col17, col18 ],
names =  ['Time', 'Gender', 'Educational Qualification', 'Years of Experience', 'Current Work', 'Full-timerS salary', 'Full-timerS organisation', 'Freelance projectS details', 'Roles', 'Current salary commensurate?', 'Negotiate current salary?', 'Negotiate first salary?', 'Details of first role', 'Feedback', 'Further engagement', 'Email address', 'Science or SciComm', 'India or Abroad' ] )


## Writes the data into a file that will be used by the data-processing code.
ascii.write( table, './../outputs/selected.csv', format = 'csv', overwrite = True )


