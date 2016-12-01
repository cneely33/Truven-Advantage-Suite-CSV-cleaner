
import csv, os

os.makedirs('headerRemoved', exist_ok=True)


# Loop through every file in the current workign directory and only grab csv's

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('csv'):
        continue  #skip non-csv files by returning to top of outer loop
    print('Removing header from ' + csvFilename + '...')

# Read the CSV files

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        
                # Grab the metric column names from the first row 
            if readerObj.line_num == 1:
                    #Dynamically assign the starting position of the headers on
                    # the first row of the csv. 
                for element in row:
                    if element != '':
                      Header = row[row.index(element):]
                continue #Return to top of the outer loop
                
                #Append the Metric names into row two
            if readerObj.line_num == 2:
                row[row.index(element):] = Header
                
            csvRows.append(row)
    csvFileObj.close()
    
    # Write out the CSV file.
            #write the new files with the same names in another folder
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
    
